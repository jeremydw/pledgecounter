from protorpc import messages


class PledgeMessage(messages.Message):
  email = messages.StringField(1)
  first_name = messages.StringField(2)
  last_name = messages.StringField(3)


class CountPledgesRequest(messages.Message):
  pass


class CountPledgesResponse(messages.Message):
  pledge_count = messages.IntegerField(1)


class CreatePledgeRequest(messages.Message):
  pledge = messages.MessageField(PledgeMessage, 1, required=True)


class CreatePledgeResponse(messages.Message):
  pledge = messages.MessageField(PledgeMessage, 1, required=True)
  pledge_count = messages.IntegerField(2)


class ListPledgesRequest(messages.Message):
  pass


class ListPledgesResponse(messages.Message):
  pledges = messages.MessageField(PledgeMessage, 1, repeated=True)
  pledge_count = messages.IntegerField(2)
