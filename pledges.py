from google.appengine.ext import ndb
import messages
import csv
import cStringIO


class Error(Exception):
  pass


class PledgeExistsError(Error):
  pass


class Pledge(ndb.Model):
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()

  @classmethod
  def create(cls, email, first_name, last_name):
    if cls.get_by_id(email):
      raise PledgeExistsError('Pledge for {} already exists.'.format(email))
    ent = cls(id=email, first_name=first_name, last_name=last_name)
    ent.put()
    return ent

  @classmethod
  def count(cls):
    query = cls.query()
    return query.count()

  @classmethod
  def list(cls):
    query = cls.query()
    return query.fetch()

  @property
  def email(self):
    return self.key.string_id()

  def to_message(self):
    message = messages.PledgeMessage()
    message.email = self.email
    message.first_name = self.first_name
    message.last_name = self.last_name
    return message

  @classmethod
  def to_csv(cls):
    fp = cStringIO.StringIO()
    writer = csv.writer(fp)
    writer.writerow(['first_name', 'last_name', 'email'])
    for pledge in cls.list():
      writer.writerow([pledge.first_name, pledge.last_name, pledge.email])
    fp.seek(0)
    return fp.getvalue()
