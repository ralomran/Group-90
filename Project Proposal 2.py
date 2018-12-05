IST 256 Python Project
Proposal 2
Zach Smith and Rashed AlOmran

We will be developing an application program using multiple python APIs which will help execute the task the program is intended to do. The program is designed to make repeated pizza ordering simpler from restaurants lacking an online ordering interface. The program calls the pizzeria and orders your usual order by converting your input from text to speech.



Code Sample:

account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+15558675310',
                        from_='+15017122661'
                    )

print(call.sid)



OUTPUT
{
  "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "annotation": null,
  "answered_by": null,
  "api_version": "2010-04-01",
  "caller_name": null,
  "date_created": "Tue, 31 Aug 2010 20:36:28 +0000",
  "date_updated": "Tue, 31 Aug 2010 20:36:44 +0000",
  "direction": "inbound",
  "duration": "15",
  "end_time": "Tue, 31 Aug 2010 20:36:44 +0000",
  "forwarded_from": "+141586753093",
  "from": "+15017122661",
  "from_formatted": "(501) 712-2661",
  "group_sid": null,
  "parent_call_sid": null,
  "phone_number_sid": "PNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "price": -0.03000,
  "price_unit": "USD",
  "sid": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "start_time": "Tue, 31 Aug 2010 20:36:29 +0000",
  "status": "completed",
  "subresource_uris": {
    "notifications": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Notifications.json",
    "recordings": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Recordings.json",
    "feedback": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Feedback.json",
    "feedback_summaries": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/FeedbackSummary.json"
  },
  "to": "+15558675310",
  "to_formatted": "(555) 867-5310",
  "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Calls/CAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"
}



Inputs:
-Pizzeria's Phone number
-the order in a line of text
-Delivery or carryout
-Address of Delivery
	-or carryout time

Output:
-Successfull or Unsucessfull

Algorithm:
-User inputs pizzeria's Phone number
-Inputs his usual order in a string of text
-inputs his address or carryout time

-program converts string of text and adress to speach
-Places phone call using the service from Twillo to the pizzeria
-Outputs the text in voice to the pizzeria

-If phone call connects program prints success
-Elif print not successfull



Both Memebers of our team equally contributed in terms of the effort they put in, the reaserch they have done, and the ideas brought to the table. We did not meet as regularly as we did, but when we did we were able to cover a lot.
