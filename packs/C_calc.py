# --------- Philip Schlaffer & Benedikt Mangott
# --------- 09.03.2022
# --------- FSST - Walch

# ------------------------------------------- Grenzfrequenz Berechnung Kondensator
def capacitor_calc():
    # ------------------------------------------- LC Glied
    def LCglied():
        # ------------------------------------------- Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # ------------------------------------------- Schaltungsbild einfügen
        lcPass_image = PhotoImage(file = r"images/LC-pass.png")
        img_label = Label(image=lcPass_image, bg="white")
        img_label.place(x=40, y=155)

        # ------------------------------------------- Berechnungs GUI
        cSelect1 = Label(rechner, text="Grenzfrequenz LC Glied", bg="white")
        cSelect1.place(x=120, y=20)

        result = Label(rechner, text="Berechnet:", bg="white")
        result.place(x=58, y=90)
        
        text1 = Label(rechner, text="Spule (mH):", bg="white")
        text1.place(x=51, y=50)
        henry_value1 = Entry(rechner)
        henry_value1.place(x=120, y=50)

        text2 = Label(rechner, text="Kondensator (nF):", bg="white")
        text2.place(x=20, y=70)
        farad_value1 = Entry(rechner)
        farad_value1.place(x=120, y=70)
        ohm_valueR1 = 0

        # ------------------------------------------- Werte einlesen und an Klasse übergeben
        def get():
            henry_valueget = henry_value1.get()
            int_henry_value = int(henry_valueget)
            farad_valueget = farad_value1.get()
            int_farad_value = int(farad_valueget)

            # ------------------------------------------- Lösungsfeld wieder säubern
            iResult = Label(rechner, bg="white",text="                       ") 
            iResult.place(x=120, y=90)

            if rechner['bg'] == "#3C4145":
                iResult['bg'] = "#3C4145"

            # ------------------------------------------- Werte zur Berechnung in Klasse schicken
            C = capacitor("LC", int_farad_value, ohm_valueR1, int_henry_value, 10, 350, 12 ,60 , 1)
            C.current(C, rechner)

        # ------------------------------------------- Button bzw. Entertaste zur Berechnung
        def enter(event):
            get()
        calc_b = Button(rechner, text="Solve", command=get, bg="white")
        calc_b.place(x=250, y=90)
        rechner.bind('<Return>', enter)

        # ------------------------------------------- Zurück Option
        back_b = Button(rechner, text="Back", bg="white",command=lambda:exec(open("packs/C_calc.py").read()))
        back_b.place(x=300, y=320)

        # ------------------------------------------- Darkmode 
        if rechner['bg'] == "#3C4145":
            for widgets in rechner.winfo_children():
                widgets.configure(bg="#3C4145", fg="white")

        rechner.mainloop()

    # ------------------------------------------- RC Glied
    def RCglied():
        # ------------------------------------------- Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # ------------------------------------------- Schaltungsbild einfügen
        rcPass_image = PhotoImage(file = r"images/RC-Tiefpass.png")
        img_label = Label(image=rcPass_image, bg="white")
        img_label.place(x=40, y=155)

        # ------------------------------------------- Berechnungs GUI
        cSelect1 = Label(rechner, text="Grenzfrequenz RC Glied", bg="white")
        cSelect1.place(x=120, y=20)

        result = Label(rechner, text="Berechnet:", bg="white")
        result.place(x=58, y=90)
        
        text1 = Label(rechner, text="Widerstand (Ohm):", bg="white")
        text1.place(x=13, y=50)
        ohm_value1 = Entry(rechner)
        ohm_value1.place(x=120, y=50)

        text2 = Label(rechner, text="Kondensator (nF):", bg="white")
        text2.place(x=20, y=70)
        farad_value1 = Entry(rechner)
        farad_value1.place(x=120, y=70)
        henry = 0

        # ------------------------------------------- Werte einlesen und an Klasse übergeben
        def get():
            ohm_valueget = ohm_value1.get()
            int_ohm_value = int(ohm_valueget)
            farad_valueget = farad_value1.get()
            int_farad_value = int(farad_valueget)

            # ------------------------------------------- Lösungsfeld wieder säubern
            iResult = Label(rechner, bg="white",text="                          ")
            iResult.place(x=120, y=90)

            if rechner['bg'] == "#3C4145":
                iResult['bg'] = "#3C4145"

            # Werte zur Berechnung in Klasse schicken
            C = capacitor("RC", int_farad_value, int_ohm_value, henry, 10, 350, 12 ,60 , 1)
            C.current(C, rechner)

        # ------------------------------------------- Button bzw. Entertaste zur Berechnung
        def enter(event):
            get()
        calc_b = Button(rechner, text="Solve", bg="white",command=get)
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)

        # ------------------------------------------- Zurück Option
        back_b = Button(rechner, text="Back", bg="white", command=lambda:exec(open("packs/C_calc.py").read()))
        back_b.place(x=300, y=320)

        # ------------------------------------------- Darkmode 
        if rechner['bg'] == "#3C4145":
            for widgets in rechner.winfo_children():
                widgets.configure(bg="#3C4145", fg="white")
        
        rechner.mainloop()

    # ------------------------------------------- Alle widgets / Labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    # ------------------------------------------- Schaltungsart auswählen Frame
    cSelect = Label(rechner, text="Ihre Schaltungsart?", bg="white")
    cSelect.place(x=120, y=20)

    LC_b = Button(rechner, text="LC Glied", bg="white", command=LCglied)
    LC_b.place(x=100, y=50)

    RC_b = Button(rechner, text="RC Glied", bg="white", command=RCglied)
    RC_b.place(x=180, y=50)

    # ------------------------------------------- Zurück Option
    switch = "white"
    back_b = Button(rechner, text="Back", bg="white",command=lambda:user_select("black"))
    back_b.place(x=300, y=320)

    # ------------------------------------------- Darkmode 
    if rechner['bg'] == "#3C4145":
        for widgets in rechner.winfo_children():
            widgets.configure(bg="#3C4145", fg="white")
        switch = "black"
    else:
        switch = "white"

capacitor_calc()