#!/usr/bin/python

name = raw_input("Please enter your name: ")
answer1 = raw_input("Who are you? (e.g. software developer at iCrossing): ")
answer2 = raw_input("Do you support Open Source Software Development (A), Closed Source Software Development (B), Both (C), or Neither (D)? Please enter A, B, C, or D: ")
while 1:
	if answer2.lower() == 'a':
		answer3 = raw_input("Why do you support Open Source Software Development? ")
		answer4 = raw_input("What part of the open source process do you think is most beneficial to the development of software projects? ")
		answer5 = raw_input("What part of the open source process is most important to you? ")
		answer6 = raw_input("What part of the closed source process is least appealing to you? ")
		answer7 = raw_input("If your company/community strictly supported closed source, would you still choose to work there? If your company/community already strictly supports closed source, why did you choose to work there? ")
		break
	elif answer2.lower() == 'b':
		answer3 = raw_input("Why do you support Closed Source Software Development? ")
		answer4 = raw_input("What part of the closed source process do you think is most beneficial to the development of software projects? ")
		answer5 = raw_input("What part of the closed source process is most important to you? ")
		answer6 = raw_input("What part of the open source process is least appealing to you? ")
		answer7 = raw_input("If your company/community strictly supported open source, would you still choose to work there? If your company/community already strictly supports open source, why did you choose to work there? ")
		break
	elif answer2.lower() == 'c':
		answer3 = raw_input("Why do you support both Open and Closed Source Development? ")
		answer4 = raw_input("What part of the open source process is most important to you? ")
		answer5 = raw_input("What part of the open source process is least appealing to you? ")
		answer6 = raw_input("What part of the closed source process is most important to you? ")
		answer7 = raw_input("What part of the closed source process is least appealing to you? ")
		break
	elif answer2.lower() == 'd':
		answer3 = raw_input("Why do you support neither? ")
		answer4 = raw_input("What part of the open source process is least appealing to you? ")
		answer5 = raw_input("What part of the closed source process is least appealing to you? ")
		answer6 = raw_input("What might be a better system or process of software development? ")
		answer7 = ''
		break
	else:
		print ("Invalid input. Please try again.")
		answer2 = raw_input("Do you support Open Source Software Development (A), Closed Source Software Development (B), Both (C), or Neither (D)? Please enter A, B, C, or D: ")

answers = [name, answer1, answer2, answer3, answer4, answer5, answer6, answer7]
print ("Processing info...")
import smtplib

session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login("eric.hao.survey@gmail.com", "erichaosurvey")
headers = "\r\n".join(["from: " + name,
                       "subject: " + "survey result",
                       "to: " + "hao.awesome@gmail.com",
                       "mime-version: 1.0",
                       "content-type: text/html"])

# body_of_email can be plaintext or html!                    
content = headers + "\r\n\r\n" + "}{".join(answers)
print ("Processing info...")
session.sendmail("eric.hao.survey@gmail.com", "hao.awesome@gmail.com", content)
print ("Done")


