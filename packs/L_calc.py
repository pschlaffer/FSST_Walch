# Philip Schlaffer & Benedikt Mangott
# 09.03.2022
# FSST - Walch

# Libarys
import elektronische_bauteile

# Grenzfrequenz Berechnung Kondensator
def capacitor_calc():
    # LC Glied
    def LCglied():
        # Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # Schaltungsbild einfügen
        lcPass_image = PhotoImage(file = r"images/LC-pass.png")
        img_label = Label(image=lcPass_image)
        img_label.place(x=40, y=155)
        img_label.configure(background='white')

        # Berechnungs GUI
        cSelect1 = Label(rechner, text="Grenzfrequenz LC Glied")
        cSelect1.configure(bg="white")
        cSelect1.place(x=120, y=20)

        result = Label(rechner, text="Berechnet:")
        result.configure(bg="white")
        result.place(x=58, y=90)
        
        text1 = Label(rechner, text="Spule (mH):")
        text1.configure(bg="white")
        text1.place(x=51, y=50)
        henry_value1 = Entry(rechner)
        henry_value1.place(x=120, y=50)

        text2 = Label(rechner, text="Kondensator (nF):")
        text2.configure(bg="white")
        text2.place(x=20, y=70)
        farad_value1 = Entry(rechner)
        farad_value1.place(x=120, y=70)
        ohm_valueR1 = 0

        # Werte einlesen und an Klasse übergeben
        def get():
            henry_valueget = henry_value1.get()
            int_henry_value = int(henry_valueget)
            farad_valueget = farad_value1.get()
            int_farad_value = int(farad_valueget)

            # Lösungsfeld wieder säubern
            iResult = Label(rechner, text="                       ") 
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            if rechner['bg'] == "#3C4145":
                iResult['bg'] = "#3C4145"

            # Werte zur Berechnung in Klasse schicken
            C = capacitor("LC", int_farad_value, ohm_valueR1, int_henry_value, 10, 350, 12 ,60 , 1)
            C.current(C, rechner)

        # Button bzw. Entertaste zur Berechnung
        def enter(event):
            get()
        calc_b = Button(rechner, text="Solve", command=get)
        calc_b.configure(bg="white")
        calc_b.place(x=250, y=90)
        rechner.bind('<Return>', enter)

        # Zurück Option
        back_b = Button(rechner, text="Back", command=lambda:exec(open("packs/L_calc.py").read()))
        back_b.configure(bg="white")
        back_b.place(x=300, y=320)

        # Darkmode 
        if rechner['bg'] == "#3C4145":
            cSelect1['bg']     = "#3C4145"
            calc_b['bg']       = "#3C4145"
            back_b['bg']       = "#3C4145"
            text2['bg']        = "#3C4145"
            henry_value1['bg'] = "#3C4145"
            text1['bg']        = "#3C4145"
            farad_value1['bg'] = "#3C4145"
            result['bg']       = "#3C4145"

            henry_value1['foreground'] = "white"
            farad_value1['foreground'] = "white"
            text1['foreground']        = "white"
            text2['foreground']        = "white"
            result['foreground']       = "white"
            back_b['foreground']       = "white"
            calc_b['foreground']       = "white"
            cSelect1['foreground']     = "white"

        rechner.mainloop()

    # RC Glied
    def RCglied():
        # Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # Schaltungsbild einfügen
        rcPass_image = PhotoImage(file = r"images/RC-Tiefpass.png")
        img_label = Label(image=rcPass_image)
        img_label.place(x=40, y=155)
        img_label.configure(background='white')

        # Berechnungs GUI
        cSelect1 = Label(rechner, text="Grenzfrequenz RC Glied")
        cSelect1.configure(bg="white")
        cSelect1.place(x=120, y=20)

        result = Label(rechner, text="Berechnet:")
        result.configure(bg="white")
        result.place(x=58, y=90)
        
        text1 = Label(rechner, text="Widerstand (Ohm):")
        text1.configure(bg="white")
        text1.place(x=13, y=50)
        ohm_value1 = Entry(rechner)
        ohm_value1.place(x=120, y=50)

        text2 = Label(rechner, text="Kondensator (nF):")
        text2.configure(bg="white")
        text2.place(x=20, y=70)
        farad_value1 = Entry(rechner)
        farad_value1.place(x=120, y=70)
        henry = 0

        # Werte einlesen und an Klasse übergeben
        def get():
            ohm_valueget = ohm_value1.get()
            int_ohm_value = int(ohm_valueget)
            farad_valueget = farad_value1.get()
            int_farad_value = int(farad_valueget)

            # Lösungsfeld wieder säubern
            iResult = Label(rechner, text="                          ") 
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            if rechner['bg'] == "#3C4145":
                iResult['bg'] = "#3C4145"

            # Werte zur Berechnung in Klasse schicken
            C = capacitor("RC", int_farad_value, int_ohm_value, henry, 10, 350, 12 ,60 , 1)
            C.current(C, rechner)

        # Button bzw. Entertaste zur Berechnung
        def enter(event):
            get()
        calc_b = Button(rechner, text="Solve", command=get)
        calc_b.configure(bg="white")
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)

        # Zurück Option
        back_b = Button(rechner, text="Back", command=lambda:exec(open("packs/L_calc.py").read()))
        back_b.configure(bg="white")
        back_b.place(x=300, y=320)

        # Darkmode 
        if rechner['bg'] == "#3C4145":
            cSelect1['bg']     = "#3C4145"
            calc_b['bg']       = "#3C4145"
            back_b['bg']       = "#3C4145"
            text2['bg']        = "#3C4145"
            ohm_value1['bg']   = "#3C4145"
            text1['bg']        = "#3C4145"
            farad_value1['bg'] = "#3C4145"
            result['bg']       = "#3C4145"

            ohm_value1['foreground']   = "white"
            farad_value1['foreground'] = "white"
            text1['foreground']        = "white"
            text2['foreground']        = "white"
            result['foreground']       = "white"
            back_b['foreground']       = "white"
            calc_b['foreground']       = "white"
            cSelect1['foreground']     = "white"
        
        rechner.mainloop()

    # Alle widgets / Labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    # Schaltungsart auswählen Frame
    cSelect = Label(rechner, text="Ihre Schaltungsart?")
    cSelect.configure(bg="white")
    cSelect.place(x=120, y=20)

    LC_b = Button(rechner, text="LC Glied", command=LCglied)
    LC_b.configure(bg="white")
    LC_b.place(x=100, y=50)

    RC_b = Button(rechner, text="RC Glied", command=RCglied)
    RC_b.configure(bg="white")
    RC_b.place(x=180, y=50)

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
        cSelect['bg'] = "#3C4145"
        back_b['bg']  = "#3C4145"
        LC_b['bg']    = "#3C4145"
        RC_b['bg']    = "#3C4145"

        cSelect['foreground'] = "white"
        back_b['foreground']  = "white"
        LC_b['foreground']    = "white"
        RC_b['foreground']    = "white"

capacitor_calc()