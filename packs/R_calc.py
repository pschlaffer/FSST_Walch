# ------- Philip Schlaffer & Benedikt Mangott
# ------- 09.03.2022
# ------- FSST - Walch

# ------------------------------------------- Libarys
from tkinter import *
from packs.calc import resistor

# ------------------------------------------- Widerstandsschaltung Berechnung
def widerstand(rechner, user_select):
    error=0
    # ------------------------------------------- Parallel Schaltung
    def parallel(error):
        # ------------------------------------------- Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()
        
        # ------------------------------------------- Error nachricht
        if error == "E":
            cError = Label(rechner, text="Please enter value!", bg="white")
            cError.place(x=120, y=120)

        # ------------------------------------------- Schaltungsbild einfügen
        parallel_image = PhotoImage(file = r"images/Resistor_par.png")
        img_label = Label(image=parallel_image, bg="white")
        img_label.place(x=130, y=140)
        
        # ------------------------------------------- Berechnungs GUI
        cSelect1 = Label(rechner, text="Parallel circuit calculator", bg="white")
        cSelect1.place(x=120, y=20)

        result = Label(rechner, text="Calculated:", bg="white",font=("Calibri", 10, "bold"))
        result.place(x=40, y=100)
        
        ohm_text1 = Label(rechner, text="1. Resistor:", bg="white")
        ohm_text1.place(x=40, y=50)
        ohm_valueR1 = Entry(rechner)
        ohm_valueR1.place(x=120, y=50)

        ohm_text2 = Label(rechner, text="2. Resistor:", bg="white")
        ohm_text2.place(x=40, y=70)
        ohm_valueR2 = Entry(rechner)
        ohm_valueR2.place(x=120, y=70)

        # ------------------------------------------- Werte einlesen und an Klassen übergeben
        def get():
            ohm_valuegetR1 = ohm_valueR1.get()
            ohm_valuegetR2 = ohm_valueR2.get()

            if ohm_valuegetR1 == '' or ohm_valuegetR2 == '':
                parallel("E")
            elif ohm_valuegetR1 == '0' or ohm_valuegetR2 == '0':
                parallel("E")
            else:
                if error == "E":
                    cError.destroy()
                int_ohm_valueR2 = int(ohm_valuegetR2)
                int_ohm_valueR1 = int(ohm_valuegetR1)

            # ------------------------------------------- Lösungsfeld wieder säubern
            iResult = Label(rechner, text="                           ", bg="white")
            iResult.place(x=120, y=90)

            if rechner['bg'] == "#3C4145":
                iResult['bg'] = "#3C4145"

            # ------------------------------------------- Werte zur Berechnung in Klasse schicken
            R = resistor("P", int_ohm_valueR1, int_ohm_valueR2, 10, 100, 12, 50, 1)
            R.current(R, rechner)

        # ------------------------------------------- Button bzw. Entertaste zur Berechnung
        def enter(event):
            get()
        calc_b = Button(rechner, text="Solve", bg="white",command=get)
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)
  
        # ------------------------------------------- Zurück Option
        back_b = Button(rechner, text="Back", bg="white",command=lambda:widerstand(rechner, user_select))
        back_b.place(x=300, y=320)

        # ------------------------------------------------------ Rechner Neustarten
        new_calc = Button(rechner, text="New", command=lambda:user_select(switch), bg="white")
        new_calc.place(x=250, y=118)

        # ------------------------------------------- Darkmode 
        if rechner['bg'] == "#3C4145":
            for widgets in rechner.winfo_children():
                widgets.configure(bg="#3C4145", fg="white")

        rechner.mainloop()

    # ------------------------------------------- Serielle Schaltung
    def seriell(error):
        # ------------------------------------------- Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # ------------------------------------------- Error nachricht
        if error == "E":
            cError = Label(rechner, text="Please enter value!", bg="white")
            cError.place(x=120, y=120)

        # ------------------------------------------- Schaltungsbild einfügen
        seriell_image = PhotoImage(file = r"images/Resistor_ser.png")
        img_label = Label(image=seriell_image, bg="white")
        img_label.place(x=130, y=140)

        # ------------------------------------------- Berechnungs GUI
        cTitle = Label(rechner, text="Serial circuit calculator", bg="white")
        cTitle.place(x=110, y=20)

        result = Label(rechner, text="Calculated:", bg="white",font=("Calibri", 10, "bold"))
        result.place(x=40, y=100)

        ohm_text1 = Label(rechner, text="1. Resistor:", bg="white")
        ohm_text1.place(x=40, y=50)
        ohm_valueR1 = Entry(rechner)
        ohm_valueR1.place(x=120, y=50)

        ohm_text2 = Label(rechner, text="2. Resistor:", bg="white")
        ohm_text2.place(x=40, y=70)
        ohm_valueR2 = Entry(rechner)
        ohm_valueR2.place(x=120, y=70)

        # ------------------------------------------- Werte einlesen und an Klasse übergeben
        def get():
            # ------------------------------------------- char aus entry auslesen und in integer umwandeln
            ohm_valuegetR1 = ohm_valueR1.get()
            ohm_valuegetR2 = ohm_valueR2.get()

            if ohm_valuegetR1 == '' or ohm_valuegetR2 == '':
                seriell("E")
            elif ohm_valuegetR1 == '0' or ohm_valuegetR2 == '0':
                seriell("E")
            else:
                if error == "E":
                    cError.destroy()
                int_ohm_valueR2 = int(ohm_valuegetR2)
                int_ohm_valueR1 = int(ohm_valuegetR1)

            # ------------------------------------------- Lösungsfeld wieder säubern
            iResult = Label(rechner, text="                          ", bg="white") 
            iResult.place(x=120, y=90)

            if rechner['bg'] == "#3C4145":
                iResult['bg'] = "#3C4145"

            # ------------------------------------------- Werte zur Berechnung in Klasse schicken
            R = resistor("S", int_ohm_valueR1, int_ohm_valueR2, 10, 100, 12, 50, 1)
            R.current(R, rechner)
        
        # ------------------------------------------- Button bzw. Entertaste zur Berechnung
        def enter(event):
            get()
        calc_b = Button(rechner, text="Solve", bg="white", command=get)
        calc_b.place(x=250, y=90)
        rechner.bind('<Return>', enter)

        # ------------------------------------------- Zurück option
        back_b = Button(rechner, text="Back", bg="white", command=lambda:widerstand(rechner, user_select))
        back_b.place(x=300, y=320)
        
        # ------------------------------------------------------ Rechner Neustarten
        new_calc = Button(rechner, text="New", command=lambda:user_select(switch), bg="white")
        new_calc.place(x=250, y=118)

        # ------------------------------------------- Darkmode 
        if rechner['bg'] == "#3C4145":
            for widgets in rechner.winfo_children():
                widgets.configure(bg="#3C4145", fg="white")
        
        rechner.mainloop()
    
    # ------------------------------------------- Alle widgets / Labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    # ------------------------------------------- Schaltungsart auswählen Frame
    cSelect1 = Label(rechner, text="Circuit type?", bg="white")
    cSelect1.place(x=120, y=20)

    parrallel_b = Button(rechner, text="Parallel", command=lambda:parallel(error), bg="white")
    parrallel_b.place(x=100, y=50)

    seriell_b = Button(rechner, text="Serial", command=lambda:seriell(error), bg="white")
    seriell_b.place(x=180, y=50)

    # ------------------------------------------- Zurück Option
    switch = "white"
    back_b = Button(rechner, text="Back", command=lambda:user_select(switch), bg="white")
    back_b.place(x=300, y=320)

    # ------------------------------------------- Darkmode 
    if rechner['bg'] == "#3C4145":
        for widgets in rechner.winfo_children():
            widgets.configure(bg="#3C4145", fg="white")
        switch = "black"
    else:
        switch = "white"
    
    rechner.mainloop()