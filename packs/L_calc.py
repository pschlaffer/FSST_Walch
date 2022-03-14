# -------- Philip Schlaffer & Benedikt Mangott
# -------- 09.03.2022
# -------- FSST - Walch

# ------------------------------------------- Grenzfrequenz Berechnung Spule
def spool_calc():
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
            iResult = Label(rechner,bg="white", text="                            ")
            iResult.place(x=120, y=90)

            if rechner['bg'] == "#3C4145":
                iResult['bg'] = "#3C4145"

            # ------------------------------------------- Werte zur Berechnung in Klasse schicken
            L = spool("LC", int_farad_value, ohm_valueR1, int_henry_value, 10, 350, 12 ,60 , 1)
            L.current(L, rechner)

        # ------------------------------------------- Button zur Berechnung bzw. Entertaste
        def enter(event):
            get()
        calc_b = Button(rechner, text="Solve", bg="white",command=get)
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)

        # ------------------------------------------- Zurück Option
        back_b = Button(rechner, text="Back", bg="white",command=lambda:exec(open("packs/L_calc.py").read()))
        back_b.place(x=300, y=320)

        # ------------------------------------------------------ Rechner Neustarten
        new_calc = Button(rechner, text="Neu", command=lambda:user_select(switch), bg="white")
        new_calc.place(x=250, y=118)

        # ------------------------------------------- Darkmode 
        if rechner['bg'] == "#3C4145":
            for widgets in rechner.winfo_children():
                widgets.configure(bg="#3C4145", fg="white")

        rechner.mainloop()

    # ------------------------------------------- RL Glied
    def RLglied():
        # ------------------------------------------- Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # ------------------------------------------- Schaltungsbild einfügen
        rlPass_image = PhotoImage(file = r"images/rl-Tiefpass.png")
        img_label = Label(image=rlPass_image, bg="white")
        img_label.place(x=40, y=155)

        # ------------------------------------------- Berechnugs GUI
        cSelect1 = Label(rechner, text="Grenzfrequenz RL Glied", bg="white")
        cSelect1.place(x=120, y=20)

        result = Label(rechner, text="Berechnet:", bg="white")
        result.place(x=58, y=90)
        
        text1 = Label(rechner, text="Widerstand (Ohm):", bg="white")
        text1.place(x=13, y=50)
        ohm_value1 = Entry(rechner)
        ohm_value1.place(x=120, y=50)

        text2 = Label(rechner, text="Spule (mH):", bg="white")
        text2.place(x=51, y=70)
        henry_value = Entry(rechner)
        henry_value.place(x=120, y=70)
        farad=0
        
        # ------------------------------------------- Werte einlesen und an Klasse übergeben
        def get():
            ohm_valueget = ohm_value1.get()
            int_ohm_value = int(ohm_valueget)
            henry_valueget = henry_value.get()
            int_henry_value = int(henry_valueget)

            # ------------------------------------------- Lösungsfeld wieder säubern
            iResult = Label(rechner, bg="white",text="                                 ")
            iResult.place(x=120, y=90)

            if rechner['bg'] == "#3C4145":
                iResult['bg'] = "#3C4145"

            # ------------------------------------------- Werte zur Berechnung in Klasse schicken
            L = spool("RL", int_henry_value, int_ohm_value, farad, 10, 350, 12 ,60 , 1)
            L.current(L, rechner)

        # ------------------------------------------- Button bzw. Entertaste zur Berechnung
        def enter(event):
            get()
        calc_b = Button(rechner, text="Solve", bg="white",command=get)
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)

        # ------------------------------------------- Zurück Option
        back_b = Button(rechner, text="Back", bg="white",command=lambda:exec(open("packs/L_calc.py").read()))
        back_b.place(x=300, y=320)

        # ------------------------------------------------------ Rechner Neustarten
        new_calc = Button(rechner, text="Neu", command=lambda:user_select(switch), bg="white")
        new_calc.place(x=250, y=118)
        
        # ------------------------------------------- Darkmode 
        if rechner['bg'] == "#3C4145":
            for widgets in rechner.winfo_children():
                widgets.configure(bg="#3C4145", fg="white")

        rechner.mainloop()

    # ------------------------------------------- Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    # ------------------------------------------- Schaltungsart auswählen Frame
    cSelect = Label(rechner, text="Ihre Schaltungsart?", bg="white")
    cSelect.place(x=120, y=20)

    LC_b = Button(rechner, text="LC Glied", command=LCglied, bg="white")
    LC_b.place(x=100, y=50)

    RL_b = Button(rechner, text="RL Glied", command=RLglied, bg="white")
    RL_b.place(x=180, y=50)
    
    # ------------------------------------------- Zurück Option
    switch = "white"
    back_b = Button(rechner, text="Back", bg="white",command=lambda:user_select(switch))
    back_b.place(x=300, y=320)

    # ------------------------------------------- Darkmode 
    if rechner['bg'] == "#3C4145":
        for widgets in rechner.winfo_children():
            widgets.configure(bg="#3C4145", fg="white")
        switch = "black"
    else:
        switch = "white"

spool_calc()