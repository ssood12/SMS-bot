from twilio.rest import Client 
 
account_sid = 'ACbbf6bf27f49b9110bd4843bb5eb47366' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGeb71bf8299b8d389890b259567eb521b', 
                              body='Hi! I am a SMS bot',      
                              to='+1647xxxxxxx' 
                          ) 
 
print(message.sid)