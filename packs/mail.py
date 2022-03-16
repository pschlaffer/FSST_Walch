# ------- Philip Schlaffer & Benedikt Mangott
# ------- 09.03.2022
# ------- FSST - Walch

# ----------------------------------------------- Libarys
import elektronische_bauteile

# ---------------------------------------------------------- Mail sende Fenster
def mail():
    # ----------------------------------------------- Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()

    # ----------------------------------------------- Kontakt GUI  
    bar = Label(rechner,width="300", text="Please enter details below", bg="orange",fg="white",font=("Calibri", 15, "bold"))
    bar.pack() 

    text1=Label(rechner, text="Betreff:", bg ="white",font=("Calibri", 12, "bold"))
    text1.place(x=15, y=50)

    betreff = Entry(rechner, bg="#8a8a8a")
    betreff.insert(0, "*")
    betreff.place(x=110, y=55, width=200, height=25)

    text2 = Label(rechner, text="Nachricht:", bg="white", font=("Calibri", 12, "bold"))
    text2.place(x=15, y=85)

    nachricht = Entry(rechner, bg="#8A8A8A")
    nachricht.insert(0,"*")
    nachricht.place(x=110, y=90, width=200, height=100)

    # ----------------------------------------------- Mail schreiben
    def get():
        # ----------------------------------------------- Betreff u. Nachricht aus Feld holen
        betreff_valueget = betreff.get()
        nachricht_valueget = nachricht.get()
        success = Label(rechner, text="")
        
        # ----------------------------------------------- Error nachricht anzeigen
        def error_message():
            error = Label(rechner, text="Please enter Value!")
            error.place(x=105, y=200)
            # ----------------------------------------------- Darkmode
            if rechner['bg'] == "#3C4145":
                error['bg']     = "#3C4145"
                error['fg']     = "white"

        # ----------------------------------------------- Error falls nichts eingegebn wird
        if betreff_valueget =='*' or nachricht_valueget=='*':
            error_message()
        elif betreff_valueget =='' or nachricht_valueget=='':
            error_message()
        elif betreff_valueget =='*' or nachricht_valueget=='':
            error_message()
        elif betreff_valueget =='' or nachricht_valueget=='*':
            error_message()
        else:
            # ----------------------------------------------- Nachricht erstellen
            msg = MIMEMultipart()
            msg['Subject'] = betreff_valueget
            msg['From'] = sender
            msg['To'] = reciever
            part = MIMEText(nachricht_valueget, 'plain')
            msg.attach(part)
            # ----------------------------------------------- Nachricht senden
            smtpObj = smtplib.SMTP(smtpServer, smtpPort)
            smtpObj.set_debuglevel(1)
            smtpObj.starttls()
            smtpObj.login(username, password)
            smtpObj.sendmail(sender, reciever, msg.as_string())
            # ----------------------------------------------- Falls erfolgreich, gesendet nachricht einblenden
            success = Label(rechner, text="Succesfull sended!", fg="green")
            success.place(x=105, y=200)
            # ----------------------------------------------- Darkmode
            if rechner['bg'] == "#3C4145":
                success['bg']   = "#3C4145"
                success['fg']   = "white"
        
    # ----------------------------------------------- Button bzw. Entertaste zur Ausführung
    def enter(event):
        get()
    calc_b = Button(rechner, text="Senden", bg="white",command=get)
    calc_b.place(x=260, y= 200)
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
        switch="black"
    else:
        switch="white"
    
    rechner.mainloop()
mail()