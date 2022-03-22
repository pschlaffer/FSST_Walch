# -------- Philip Schlaffer & Benedikt Mangott
# -------- 09.03.2022
# -------- FSST - Walch

# ------------------------------------------- Libarys
from tkinter import *
from packs.calc import spool

# ------------------------------------------- Grenzfrequenz Berechnung Spule
def spool_calc(rechner, user_select):
    error=0
    # ------------------------------------------- LC Glied
    def LCglied(error):
        # ------------------------------------------- Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # ------------------------------------------- Error nachricht
        if error == "E":
            cError = Label(rechner, text="Please enter value!", bg="white")
            cError.place(x=120, y=120)

        # ------------------------------------------- Schaltungsbild einfügen
        lcPass_image = PhotoImage(file = r"images/LC-pass.png")
        img_label = Label(image=lcPass_image, bg="white")
        img_label.place(x=40, y=155)

        # ------------------------------------------- Berechnungs GUI
        cSelect1 = Label(rechner, text="Cut-Off frequency LC-Pass", bg="white")
        cSelect1.place(x=120, y=20)

        result = Label(rechner, text="Calculated:", bg="white",font=("Calibri", 10, "bold"))
        result.place(x=39, y=100)
        
        text1 = Label(rechner, text="Coil (mH):", bg="white")
        text1.place(x=43, y=50)
        henry_value1 = Entry(rechner)
        henry_value1.place(x=120, y=50)

        text2 = Label(rechner, text="Capacitor (nF):", bg="white")
        text2.place(x=20, y=70)
        farad_value1 = Entry(rechner)
        farad_value1.place(x=120, y=70)
        ohm_valueR1 = 0

        # ------------------------------------------- Werte einlesen und an Klasse übergeben
        def get():
            henry_valueget = henry_value1.get()
            farad_valueget = farad_value1.get()

            if henry_valueget == '' or farad_valueget == '':
                LCglied("E")
            elif henry_valueget == '0' or farad_valueget == '0':
                LCglied("E")
            else:
                if error == "E":
                    cError.destroy()
                int_henry_value = int(henry_valueget)
                int_farad_value = int(farad_valueget)

            # ------------------------------------------- Lösungsfeld wieder säubern
            iResult = Label(rechner,bg="white", text="                            ")
            iResult.place(x=120, y=100)

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
        back_b = Button(rechner, text="Back", bg="white",command=lambda:spool_calc(rechner, user_select))
        back_b.place(x=300, y=320)
        
        # ------------------------------------------------------ Bei Escape schließen
        rechner.bind('<Escape>', lambda el: spool_calc(rechner, user_select))


        # ------------------------------------------------------ Rechner Neustarten
        new_calc = Button(rechner, text="New", command=lambda:user_select(switch), bg="white")
        new_calc.place(x=250, y=118)

        # ------------------------------------------- Darkmode 
        if rechner['bg'] == "#3C4145":
            for widgets in rechner.winfo_children():
                widgets.configure(bg="#3C4145", fg="white")

        rechner.mainloop()

    # ------------------------------------------- RL Glied
    def RLglied(error):
        # ------------------------------------------- Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # ------------------------------------------- Error nachricht
        if error == "E":
            cError = Label(rechner, text="Please enter value!", bg="white")
            cError.place(x=120, y=120)

        # ------------------------------------------- Schaltungsbild einfügen
        rlPass_image = PhotoImage(file = r"images/rl-Tiefpass.png")
        img_label = Label(image=rlPass_image, bg="white")
        img_label.place(x=40, y=155)

        # ------------------------------------------- Berechnugs GUI
        cSelect1 = Label(rechner, text="Cut-Off frequency RL-Pass", bg="white")
        cSelect1.place(x=120, y=20)

        result = Label(rechner, text="Calculated:", bg="white",font=("Calibri", 10, "bold"))
        result.place(x=39, y=100)
        
        text1 = Label(rechner, text="Resistor (Ohm):", bg="white")
        text1.place(x=15, y=50)
        ohm_value1 = Entry(rechner)
        ohm_value1.place(x=120, y=50)

        text2 = Label(rechner, text="Coil (mH):", bg="white")
        text2.place(x=43, y=70)
        henry_value = Entry(rechner)
        henry_value.place(x=120, y=70)
        farad=0
        
        # ------------------------------------------- Werte einlesen und an Klasse übergeben
        def get():
            ohm_valueget = ohm_value1.get()
            henry_valueget = henry_value.get()
            
            if henry_valueget == '' or ohm_valueget == '':
                RLglied("E")
            elif henry_valueget == '0' or ohm_valueget == '0':
                RLglied("E")
            else:
                if error == "E":
                    cError.destroy()
                int_ohm_value = int(ohm_valueget)
                int_henry_value = int(henry_valueget)

            # ------------------------------------------- Lösungsfeld wieder säubern
            iResult = Label(rechner, bg="white",text="                                 ")
            iResult.place(x=120, y=100)

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
        back_b = Button(rechner, text="Back", bg="white",command=lambda:spool_calc(rechner, user_select))
        back_b.place(x=300, y=320)

        # ------------------------------------------------------ Bei Escape schließen
        rechner.bind('<Escape>', lambda el: spool_calc(rechner, user_select))

        # ------------------------------------------------------ Rechner Neustarten
        new_calc = Button(rechner, text="New", command=lambda:user_select(switch), bg="white")
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
    cSelect = Label(rechner, text="Circuit type?", bg="white")
    cSelect.place(x=120, y=20)

    LC_b = Button(rechner, text="LC-Pass", command=lambda:LCglied(error), bg="white")
    LC_b.place(x=100, y=50)

    RL_b = Button(rechner, text="RL-Pass", command=lambda:RLglied(error), bg="white")
    RL_b.place(x=180, y=50)
    
    # ------------------------------------------- Zurück Option
    switch = "white"
    back_b = Button(rechner, text="Back", bg="white",command=lambda:user_select(switch))
    back_b.place(x=300, y=320)

    # ------------------------------------------------------ Bei Escape schließen
    rechner.bind('<Escape>', lambda el: user_select(switch))

    # ------------------------------------------- Darkmode 
    if rechner['bg'] == "#3C4145":
        for widgets in rechner.winfo_children():
            widgets.configure(bg="#3C4145", fg="white")
        switch = "black"
    else:
        switch = "white"
