# We will used sys module in the front

import sys

if len(sys.argv) > 1 : # Here we look for the length of sys.argv since we will gonna use the [1] count
  subject = sys.argv[1] # PHP Variable $email_subj
  recipient = sys.argv[2] # PHP Variable $email_add
  body = sys.argv[3] # PHP Variable $body
  sender = sys.argv[4] # PHP Variable $email_sender

#After we call the variables in PHP we will now print it
print(subject)
print("From " + sender + " To " + recipient)
print("\n \n")
print(body)
print("\n")

#The output will be what string we sent in PHP to Python
