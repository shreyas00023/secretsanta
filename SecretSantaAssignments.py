import csv
import smtplib
import random

names = []
data = []
assignments = []

with open('SampleCSV.csv',encoding='ISO-8859-1') as file:
    reader = csv.reader(file, dialect='excel')
    for row in reader:
        header = row
        break
    for row in reader:
        data.append(row[1:7])
        names.append(row[1])
copynames = names.copy()
for name in copynames:
    random.shuffle(names)
    while names[0] == name:
        random.shuffle(names)
    assignments.append((name,names.pop(0)))
#print(assignments)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("emailid","password")

print("got past login")

for ass in assignments:
   persondata = data[copynames.index(ass[0])]
   personname = persondata[0]
   personemail = persondata[2]
   assdata = data[copynames.index(ass[1])]
   assname,assgender,asspref,assdislike,assallergy = assdata[0],assdata[1],assdata[3],assdata[4],assdata[5]
   text = "Hello "+personname+",\n\nHappy Holidays! Keep this email secret because it's time for Secret Santa!\n\nYour assignment is to find a gift for: "+assname+"\n\nShe/He said for their preferences:\n"+asspref+"\n\nShe/He would not like:\n"+assdislike+"\n\nHe/She is allergic to:\n"+assallergy+"\n\nHave a great winter break,\nShreyas Angara"
   message = 'Subject: {}\n\n{}'.format("Secret Santa Information", text)
   server.sendmail("email@gmail.com",personemail,message.encode('utf-8'))
   #  print(message)
print("Sent Emails")
server.quit()
