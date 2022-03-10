# Philip Schlaffer & Benedikt Mangott
# 09.03.2022
# FSST - Walch

# Imports
import elektronische_bauteile

# Mail Einstellungen
smtpServer = "smtp.web.de"
smtpPort   = 587
username   = "htl_mangott-schlaffer"
password   = "nibnab01"

sender    = "htl_mangott-schlaffer@web.de"
reciever1 = "philip@schlaffers.at"
reciever2 = "bmangott@tsn.at"
reciever3 = "mangottbenni@gmail.com"

def mail():
    iX=random.randint(0,100)
    subject = "Programm Fehler"
    body = "Das Programm elektronische Bauteile weisd einen kritischen Fehler auf. \n Negger."

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = reciever3
    part = MIMEText(body, 'plain')
    msg.attach(part)

    smtpObj = smtplib.SMTP(smtpServer, smtpPort)
    smtpObj.set_debuglevel(1)
    smtpObj.starttls()
    smtpObj.login(username, password)
    smtpObj.sendmail(sender, reciever3, msg.as_string())