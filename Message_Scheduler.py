# 1.) TWILIO SETUP
# 2.) USER INPUT
# 3.) SCHEDULING
# 4.) SEND MESSAGE
#  STEP-1 [install the required library] 

from twilio.rest import Client
from datetime import timedelta,datetime
import time

# STEP-2 [twilio credential]
account_sid=#Enter Your account_sid
auth_token=#Enter Your token number
clients = Client(account_sid, auth_token)

#STEP-3 [SEND MESSAGE FUNCTION]
def send_message(number,message_body):
    try:
        message=clients.messages.create(
            from_=# twilio whatsapp number 
            body=message_body,
            to=f'whatsapp:{number}'
        )
        print(f'Message sent Succesfully')
    except Exception as e:
        print("An Error Occured")

# STEP-4 [User input]
name=input("Enter the recipient name=")
number=input("Enter the recipient whatsapp number (with country code):")
message_body=input("Enter the message you want to send to=")

# STEP-4 [time,date and calculate delay]
date_str=input("Enter date to send the message[YYYY-MM-DD]=")
time_str=input("Enter time to send the message[HH:MM IN 24 HOURS FORMAT]=")

# date-time
schedule_datetime=datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")
current_datetime=datetime.now()

# Calculate delay
time_difference=schedule_datetime-current_datetime
delay_seconds=time_difference.total_seconds()

if delay_seconds<=0:
    print("SPECIFIED TIME IS THE PAST ")
else:
    print("Message is scheduled at",schedule_datetime,"and soon sent it to",name)
    # Wait for the schedule time
    time.sleep(delay_seconds)
    # send the message 
    send_message(number,message_body)
        

