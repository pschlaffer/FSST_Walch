# Philip Schlaffer & Benedikt Mangott
# 09.03.2022
# FSST - Walch

# Libarys
import elektronische_bauteile

# Widerstandsschaltung Berechnung
def widerstand():
    # Parallel Schaltung
    def parallel():
        # Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # Schaltungsbild einfügen
        parallel_image = PhotoImage(file = r"images/Resistor_par.png")
        img_label = Label(image=parallel_image)
        img_label.place(x=130, y=140)
        img_label.configure(background='white')
        
        # Berechnungs GUI
        cSelect1 = Label(rechner, text="Parallel Schaltung Rechner")
        cSelect1.configure(bg="white")
        cSelect1.place(x=120, y=20)

        result = Label(rechner, text="Berechnet:")
        result.configure(bg="white")
        result.place(x=40, y=90)
        
        ohm_text1 = Label(rechner, text="1. Widerstand:")
        ohm_text1.configure(bg="white")
        ohm_text1.place(x=40, y=50)
        ohm_valueR1 = Entry(rechner)
        ohm_valueR1.place(x=120, y=50)

        ohm_text2 = Label(rechner, text="2. Widerstand:")
        ohm_text2.configure(bg="white")
        ohm_text2.place(x=40, y=70)
        ohm_valueR2 = Entry(rechner)
        ohm_valueR2.place(x=120, y=70)

        # Werte einlesen und an Klassen übergeben
        def get():
            ohm_valuegetR1 = ohm_valueR1.get()
            int_ohm_valueR1 = int(ohm_valuegetR1)
            ohm_valuegetR2 = ohm_valueR2.get()
            int_ohm_valueR2 = int(ohm_valuegetR2)

            # Lösungsfeld wieder säubern
            iResult = Label(rechner, text="                           ")
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            if rechner['bg'] == "#3C4145":
                iResult['bg'] = "#3C4145"

            # Werte zur Berechnung in Klasse schicken
            R = resistor("P", int_ohm_valueR1, int_ohm_valueR2, 10, 100, 12, 50, 1)
            R.current(R, rechner)

        # Button bzw. Entertaste zur Berechnung
        def enter(event):
            get()
        calc_b = Button(rechner, text="Solve", command=get)
        calc_b.configure(bg="white")
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)
  
        # Zurück Option
        back_b = Button(rechner, text="Back", command=lambda:exec(open("packs/R_calc.py").read()))
        back_b.configure(bg='white')
        back_b.place(x=300, y=320)

        # Darkmode 
        if rechner['bg'] == "#3C4145":
            cSelect1['bg']    = "#3C4145"
            calc_b['bg']      = "#3C4145"
            back_b['bg']      = "#3C4145"
            ohm_text2['bg']   = "#3C4145"
            ohm_valueR1['bg'] = "#3C4145"
            ohm_text1['bg']   = "#3C4145"
            ohm_valueR2['bg'] = "#3C4145"
            result['bg']      = "#3C4145"

            ohm_valueR1['foreground'] = "white"
            ohm_valueR2['foreground'] = "white"
            ohm_text1['foreground']   = "white"
            ohm_text2['foreground']   = "white"
            result['foreground']      = "white"
            back_b['foreground']      = "white"
            calc_b['foreground']      = "white"
            cSelect1['foreground']    = "white"

        rechner.mainloop()

    # Serielle Schaltung
    def seriell():
        # Alle widgets / labels löschen
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # Schaltungsbild einfügen
        seriell_image = PhotoImage(file = r"images/Resistor_ser.png")
        img_label = Label(image=seriell_image)
        img_label.place(x=130, y=140)
        img_label.configure(background='white')

        # Berechnungs GUI
        cSelect1 = Label(rechner, text="Reihenschaltung Rechner")
        cSelect1.configure(bg="white")
        cSelect1.place(x=110, y=20)

        result = Label(rechner, text="Berechnet:")
        result.configure(bg="white")
        result.place(x=40, y=90)

        ohm_text1 = Label(rechner, text="1. Widerstand:")
        ohm_text1.configure(bg="white")
        ohm_text1.place(x=40, y=50)
        ohm_valueR1 = Entry(rechner)
        ohm_valueR1.place(x=120, y=50)

        ohm_text2 = Label(rechner, text="2. Widerstand:")
        ohm_text2.configure(bg="white")
        ohm_text2.place(x=40, y=70)
        ohm_valueR2 = Entry(rechner)
        ohm_valueR2.place(x=120, y=70)

        # Werte einlesen und an Klasse übergeben
        def get():
            ohm_valuegetR1 = ohm_valueR1.get()
            int_ohm_valueR1 = int(ohm_valuegetR1)
            ohm_valuegetR2 = ohm_valueR2.get()
            int_ohm_valueR2 = int(ohm_valuegetR2)

            # Lösungsfeld wieder säubern
            iResult = Label(rechner, text="                          ") 
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            if rechner['bg'] == "#3C4145":
                iResult['bg'] = "#3C4145"

            # Werte zur Berechnung in Klasse schicken
            R = resistor("S", int_ohm_valueR1, int_ohm_valueR2, 10, 100, 12, 50, 1)
            R.current(R, rechner)
        
        # Button bzw. Entertaste zur Berechnung
        def enter(event):
            get()
        calc_b = Button(rechner, text="Solve", command=get)
        calc_b.configure(bg="white")
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)

        # Zurück option
        back_b = Button(rechner, text="Back", command=exec(open("packs/R_calc.py").read()))
        back_b.configure(bg="white")
        back_b.place(x=300, y=320)

        # Darkmode 
        if rechner['bg'] == "#3C4145":
            cSelect1['bg']    = "#3C4145"
            calc_b['bg']      = "#3C4145"
            back_b['bg']      = "#3C4145"
            ohm_text2['bg']   = "#3C4145"
            ohm_valueR1['bg'] = "#3C4145"
            ohm_text1['bg']   = "#3C4145"
            ohm_valueR2['bg'] = "#3C4145"
            result['bg']      = "#3C4145"

            ohm_valueR1['foreground'] = "white"
            ohm_valueR2['foreground'] = "white"
            ohm_text1['foreground']   = "white"
            ohm_text2['foreground']   = "white"
            result['foreground']      = "white"
            back_b['foreground']      = "white"
            calc_b['foreground']      = "white"
            cSelect1['foreground']    = "white"

        rechner.mainloop()
    
    # Alle widgets / Labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    # Schaltungsart auswählen Frame
    cSelect1 = Label(rechner, text="Ihre Schaltungsart?")
    cSelect1.configure(bg="white")
    cSelect1.place(x=120, y=20)

    parrallel_b = Button(rechner, text="Parralel", command=parallel)
    parrallel_b.configure(bg="white")
    parrallel_b.place(x=100, y=50)

    seriell_b = Button(rechner, text="Seriell", command=seriell)
    seriell_b.configure(bg="white")
    seriell_b.place(x=180, y=50)

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
        cSelect1['bg']    = "#3C4145"
        back_b['bg']      = "#3C4145"
        seriell_b['bg']   = "#3C4145"
        parrallel_b['bg'] = "#3C4145"

        cSelect1['foreground']    = "white"
        back_b['foreground']      = "white"
        seriell_b['foreground']   = "white"
        parrallel_b['foreground'] = "white"

widerstand()