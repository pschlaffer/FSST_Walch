# Philip Schlaffer & Benedikt Mangott
# 09.03.2022
# FSST - Walch

# Imports
import elektronische_bauteile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
    
def mail():
    # Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()

    # Kontakt GUI
    cSelect1 = Label(rechner, text="Kontakt")
    cSelect1.configure(bg="white")
    cSelect1.place(x=120, y=20)
    
    text1 = Label(rechner, text="Betreff:")
    text1.configure(bg="white")
    text1.place(x=51, y=50)
    betreff = Entry(rechner)
    betreff.place(x=120, y=50, width=150, height=20)

    text2 = Label(rechner, text="Nachricht:")
    text2.configure(bg="white")
    text2.place(x=51, y=70)
    nachricht = Entry(rechner)
    nachricht.place(x=120, y=80, width=150, height=100)

    # Mail schreiben
    def get():
        # Betreff u. Nachricht aus Feld holen
        betreff_valueget = betreff.get()
        nachricht_valueget = nachricht.get()
        
        # Nachricht erstellen
        msg = MIMEMultipart()
        msg['Subject'] = betreff_valueget
        msg['From'] = sender
        msg['To'] = reciever1
        part = MIMEText(nachricht_valueget, 'plain')
        msg.attach(part)

        # Nachricht senden
        smtpObj = smtplib.SMTP(smtpServer, smtpPort)
        smtpObj.set_debuglevel(1)
        smtpObj.starttls()
        smtpObj.login(username, password)
        smtpObj.sendmail(sender, reciever1, msg.as_string())

    # Button bzw. Entertaste zur Berechnung
    def enter(event):
        get()
    calc_b = Button(rechner, text="Senden", command=get)
    calc_b.configure(background="white")
    calc_b.place(x=280, y= 80)
    rechner.bind('<Return>', enter)

    # Zurück Option
    if rechner['bg'] == "#3C4145":
        back_b = Button(rechner, text="Back", command=lambda:user_select("black"))
        back_b.configure(bg="white")
        back_b.place(x=300, y=320)

    if rechner['bg'] == "white":
        back_b = Button(rechner, text="Back", command=lambda:user_select("white"))
        back_b.configure(bg="white")
        back_b.place(x=300, y=320)
    
    # Darkmode 
    if rechner['bg'] == "#3C4145":
        cSelect1['bg']  = "#3C4145"
        calc_b['bg']    = "#3C4145"
        back_b['bg']    = "#3C4145"
        text2['bg']     = "#3C4145"
        betreff['bg']   = "#3C4145"
        text1['bg']     = "#3C4145"
        nachricht['bg'] = "#3C4145"

        betreff['foreground']   = "white"
        nachricht['foreground'] = "white"
        text1['foreground']     = "white"
        text2['foreground']     = "white"
        back_b['foreground']    = "white"
        cSelect1['foreground']  = "white"
        calc_b['foreground']    = "white"

    rechner.mainloop()

mail()