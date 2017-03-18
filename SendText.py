from twilio.rest import TwilioRestClient

#Your Account Sid and Auth Toek from
account_sid = "AC93a2e316f4d18071c0412e31eb6fdb86"
auth_token = "208c6e028eed432c42177912105f0edb"
client = TwilioRestClient (account_sid, auth_token)

message = client.sms.messages.create(
        body="This is me texting me from a computer?",
        to="+12604400664",
        from_="+13172458864")
print message.sid
