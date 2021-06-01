import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('legend.eleve@gmail.com','legend2002')
server.sendmail('legend.eleve@gmail.com','abdobella977@gmail.com','hello from fuck')
