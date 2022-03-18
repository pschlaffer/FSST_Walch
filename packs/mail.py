# ------- Philip Schlaffer & Benedikt Mangott
# ------- 09.03.2022
# ------- FSST - Walch

# ----------------------------------------------- Libarys
from tkinter import *
# ----------------------------- Mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ----------------------------------------------- Mail Einstellungen
smtpServer = "smtp.web.de"
smtpPort   = 587
username   = "htl_mangott-schlaffer"
password   = "nibnab02"
sender     = "htl_mangott-schlaffer@web.de"
reciever   = "pschlaffer@tsn.at"
reciever2  = "bmangott@tsn.at"

# ----------------------------------------------- Mail sende Fenster
def mail_send(rechner, user_select, sended_mail):
    # ----------------------------------------------- Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()

    # ----------------------------------------------- Kontakt GUI  
    bar = Label(rechner, width="300",text="Please enter details below", bg="orange", fg="white", font=("Calibri", 15, "bold"))
    bar.pack() 

    text1=Label(rechner, text="Reference:", bg ="white", font=("Calibri", 12, "bold"))
    text1.place(x=15, y=50)

    betreff = Entry(rechner, bg="#8A8A8A")
    betreff.insert(0, "*")
    betreff.place(x=110, y=55, width=200, height=25)

    text2 = Label(rechner, text="Message:", bg="white", font=("Calibri", 12, "bold"))
    text2.place(x=15, y=85)

    nachricht = Entry(rechner, bg="#8A8A8A")
    nachricht.insert(0,"*")
    nachricht.place(x=110, y=90, width=200, height=100)

    note = Label(rechner, text="Errors might occur when seding via HTL network!!", bg="white")
    note.place(x=10, y=322)

    # ----------------------------------------------- Wenn Mail gschickt wurde Nachricht ausgeben
    success = Label(rechner, text="Succesfull sended!", bg="white", fg="green")
    if sended_mail == "send":
        success.place(x=105, y=200)

    # ----------------------------------------------- Mail schreiben
    def get(sended_mail):
        # ----------------------------------------------- Betreff u. Nachricht aus Feld holen
        betreff_valueget   = betreff.get()
        nachricht_valueget = nachricht.get()

        # ----------------------------------------------- Error nachricht anzeigen
        def error_message(error):
            if error == "novalue" and sended_mail == "no":
                error = Label(rechner, text="Please enter Value!", bg="white", fg="red")
                error.place(x=105, y=200)
            if error == "max":
                error = Label(rechner, text="You have sent the maximum number of messages!", bg="white", fg="red", font=("Calibri", 10, "bold"))
                error.place(x=15, y=230)
                success.destroy()
            # ----------------------------------------------- Darkmode
            if rechner['bg'] == "#3C4145":
                for widgets in rechner.winfo_children():
                    widgets.configure(bg="#3C4145", fg="white")
                bar['bg'] = "orange"

        # ----------------------------------------------- Error falls nichts eingegebn wird
        if betreff_valueget == '*' or nachricht_valueget == '*':
            error_message("novalue")
        elif betreff_valueget == '' or nachricht_valueget == '':
            error_message("novalue")
        elif sended_mail == "send":
            error_message("max")
        else:
            # ----------------------------------------------- Nachricht an pschlaffer
            msg_philip = MIMEMultipart()
            msg_philip['Subject'] = betreff_valueget
            msg_philip['From'] = sender
            msg_philip['To'] = reciever
            part = MIMEText(nachricht_valueget, 'plain')
            msg_philip.attach(part)
            # ----------------------------------------------- Nachricht senden
            smtpObj = smtplib.SMTP(smtpServer, smtpPort)
            smtpObj.set_debuglevel(1)
            smtpObj.starttls()
            smtpObj.login(username, password)
            smtpObj.sendmail(sender, reciever, msg_philip.as_string())

            # ----------------------------------------------- Nachricht an bmangott
            msg_benni = MIMEMultipart()
            msg_benni['Subject'] = betreff_valueget
            msg_benni['From'] = sender
            msg_benni['To'] = reciever2
            part = MIMEText(nachricht_valueget, 'plain')
            msg_benni.attach(part)
            # ----------------------------------------------- Nachricht senden
            smtpObj = smtplib.SMTP(smtpServer, smtpPort)
            smtpObj.set_debuglevel(1)
            smtpObj.starttls()
            smtpObj.login(username, password)
            smtpObj.sendmail(sender, reciever2, msg_benni.as_string())

            # ----------------------------------------------- Bestätigung das Mail gesendet wurde
            mail_send(rechner, user_select, "send")
        
    # ----------------------------------------------- Button bzw. Entertaste zur Ausführung
    def enter(event):
        get(sended_mail)
    calc_b = Button(rechner, text="Send", bg="white", command=lambda:get(sended_mail))
    calc_b.place(x=275, y=200)
    rechner.bind('<Return>', enter)
    
    # ----------------------------------------------- Zurück Option
    switch = "white"
    back_b = Button(rechner, text="Back", command=lambda:user_select(switch), bg="white")
    back_b.place(x=300, y=320)

    # ----------------------------------------------- Darkmode 
    if rechner['bg'] == "#3C4145":
        for widgets in rechner.winfo_children():
            widgets.configure(bg="#3C4145", fg="white")
        bar['bg'] ="orange"
        success['fg'] = "green"
        switch="black"
    else:
        switch="white"
    
    rechner.mainloop()