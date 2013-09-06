from google.appengine.ext import endpoints
import datetime
import pledges
import services
import webapp2


class CsvHandler(webapp2.RequestHandler):

  def get(self):
    filename = str(datetime.datetime.now())
    filename = filename.replace(' ', '_').replace(':', '-').split('.')[0]
    filename = 'pledges-{}.csv'.format(filename)
    disposition = 'attachment;filename={}'.format(filename)
    self.response.headers['Content-Type'] = 'text/csv'
    self.response.headers['Content-Disposition'] = disposition
    self.response.out.write(pledges.Pledge.to_csv())


all_services = (
    services.PledgeService(),
)
endpoints_application = endpoints.api_server(all_services, restricted=False)


routes = (
      ('/public/csv', CsvHandler),
)
application = webapp2.WSGIApplication(routes)
