import pledges
import messages
from google.appengine.ext import endpoints
from protorpc import remote

api_class = endpoints.api(name='pledgecounter', version='v0.1').api_class


@api_class(resource_name='pledges')
class PledgeService(remote.Service):

  @endpoints.method(
      messages.CreatePledgeRequest, messages.CreatePledgeResponse,
      path='pledges', http_method='POST')
  def create(self, request):
    try:
      pledge = pledges.Pledge.create(
          request.pledge.email,
          request.pledge.first_name,
          request.pledge.last_name)
    except pledges.PledgeExistsError as e:
      raise endpoints.BadRequestException(str(e))

    message = messages.CreatePledgeResponse()
    message.pledge = pledge.to_message()
    message.pledge_count = pledges.Pledge.count() + 1
    return message

  @endpoints.method(
      messages.CountPledgesRequest, messages.CountPledgesResponse,
      path='pledges/count', http_method='GET')
  def count(self, request):
    message = messages.CountPledgesResponse()
    message.pledge_count = pledges.Pledge.count()
    return message

  @endpoints.method(
      messages.ListPledgesRequest, messages.ListPledgesResponse,
      path='pledges', http_method='GET')
  def list(self, request):
    all_pledges = pledges.Pledge.list()
    message = messages.ListPledgesResponse()
    message.pledges = [p.to_message() for p in all_pledges]
    message.pledge_count = len(all_pledges)
    return message
