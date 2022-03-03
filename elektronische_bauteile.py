# Philip Schlaffer & Benedikt Mangott
# 21.02.2022
# FSST - Walch

# Libarys
from tkinter import *
from PIL import ImageTk, Image
import math as m
import webbrowser

# Klassen
class components:
    def __init__(self, tolerance, impedance, voltage, frequenz, phi):
        self.tolerance = tolerance
        self.impedance = impedance
        self.voltage   = voltage
        self.frequenz  = frequenz
        self.phi       = phi
        
class resistor(components): 
    def __init__(self, select, ohm_valueR1, ohm_valueR2, tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self, tolerance, impedance, voltage,frequenz, phi)
        self.select      = select
        self.ohm_valueR1 = ohm_valueR1
        self.ohm_valueR2 = ohm_valueR2

    def current(self, R, rechner):
        # Parralel Schaltung
        if (R.select == "P"):
            # Berechnung & rundung
            R12 = (R.ohm_valueR1 * R.ohm_valueR2)/(R.ohm_valueR1 + R.ohm_valueR2)
            R12_round = round(R12, 1)
            if R12_round < 1000:
                R12_new = R12_round, "Ω"
            if R12_round >= 1000:
                R12_new = R12_round * m.pow(10, -3), "kΩ"
            # Anzeige
            iResult = Label(rechner, text=R12_new)
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)
            
            def renew_calc():
                rechner.destroy()
                user_select()
            new_calc = Button(rechner, text="Neu", command=renew_calc)
            new_calc.configure(bg="white")
            new_calc.place(x=250, y=118)
        
        # Reihen Schaltung
        else:
            # Berechnung
            R12 = R.ohm_valueR1 + R.ohm_valueR2
            if R12 < 1000:
                R12_new = R12, "Ω"
            if R12 >= 1000:
                R12_new = R12 * m.pow(10, -3), "kΩ"
            # Anzeige
            iResult = Label(rechner, text=R12_new)
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            def renew_calc():
                rechner.destroy()
                user_select()
            new_calc = Button(rechner, text="Neu", command=renew_calc)
            new_calc.configure(bg="white")
            new_calc.place(x=250, y=118)

class capacitor(components):
    def __init__(self, LCselect, farad_value1, ohm_valueR1, henry_value1, tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self, tolerance, impedance, voltage, frequenz, phi)
        self.LCselect     = LCselect
        self.farad_value1 = farad_value1
        self.ohm_valueR1  = ohm_valueR1
        self.henry_value1 = henry_value1

    def current(self, C, rechner):
        # RC Glied
        if (C.LCselect == "RC" or C.LCselect == "rc"):
            # Berechnung
            nanofarad = (m.pow(10, -9)*C.farad_value1)
            fg = 1/(2*m.pi*C.ohm_valueR1*nanofarad)
            fg_round = round(fg, 0)
            if fg_round < 1000:
                fg_round_new = fg_round, "Hz"
            if fg_round >= 1000:
                fg_round_new = fg_round * m.pow(10, -3), "kHz"
            # Anzeige
            iResult = Label(rechner, text=fg_round_new)
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            def renew_calc():
                rechner.destroy()
                user_select()
            new_calc = Button(rechner, text="Neu", command=renew_calc)
            new_calc.configure(bg="white")
            new_calc.place(x=250, y=118)
    
        # LC Glied
        else:
            # Berechnung
            mHenry    = (m.pow(10, -3)*C.henry_value1)
            nanofarad = (m.pow(10, -9)*C.farad_value1)
            fg = 1/(2*m.pi*m.sqrt(mHenry*nanofarad))
            fg_round = round(fg, 0)
            if fg_round < 1000:
                fg_round_new = fg_round, "Hz"
            if fg_round >= 1000:
                fg_round_new = fg_round * m.pow(10, -3), "kHz"
            # Anzeige
            iResult = Label(rechner, text=fg_round_new)
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            def renew_calc():
                rechner.destroy()
                user_select()
            new_calc = Button(rechner, text="Neu", command=renew_calc)
            new_calc.configure(bg="white")
            new_calc.place(x=250, y=118)

class spool(components):
    def __init__(self, LCselect, henry_value1, ohm_valueR1, farad_value1,tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self,tolerance, impedance, voltage, frequenz, phi)
        self.LCselect      = LCselect
        self.henry_value1  = henry_value1
        self.ohm_valueR1   = ohm_valueR1
        self.farad_value1  = farad_value1

    def current(self, L, rechner):
        # LC Glied
        if (L.LCselect == "LC" or L.LCselect == "lc"):
            # Berechnung
            mHenry    = (m.pow(10, -3)*L.henry_value1)
            nanofarad = (m.pow(10, -9)*L.farad_value1)
            fg = 1/(2*m.pi*m.sqrt(mHenry*nanofarad))
            fg_round = round(fg, 0)
            if fg_round < 1000:
                fg_round_new = fg_round, "Hz"
            if fg_round >= 1000:
                fg_round_new = fg_round * m.pow(10, -3), "kHz"
            # Anzeige
            iResult = Label(rechner, text=fg_round_new)
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            def renew_calc():
                rechner.destroy()
                user_select()
            new_calc = Button(rechner, text="Neu", command=renew_calc)
            new_calc.configure(bg="white")
            new_calc.place(x=250, y=118)

        # RL Glied
        else:
            # Berechnung
            mHenry = (m.pow(10, -3)*L.henry_value1)
            fg = L.ohm_valueR1/(2*m.pi*mHenry)
            fg_round = round(fg, 0)
            if fg_round < 1000:
                fg_round_new = fg_round, "Hz"
            if fg_round >= 1000:
                fg_round_new = fg_round * m.pow(10, -3), "kHz"
            # Anzeige
            iResult = Label(rechner, text=fg_round_new)
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            def renew_calc():
                rechner.destroy()
                user_select()
            new_calc = Button(rechner, text="Neu", command=renew_calc)
            new_calc.configure(bg="white")
            new_calc.place(x=250, y=118)

# Widerstandsschaltung Berechnung
def resistor_calc(rechner):
    # Parallel Schaltung
    def parallel():
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # Schaltungsbild einfügen
        parallel_image = Image.open("images/Resistor_par.png")
        img_open = ImageTk.PhotoImage(parallel_image)
        img_label = Label(image=img_open)
        img_label.place(x=130, y=140)
        img_label.configure(background='white')

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

        def get():
            ohm_valuegetR1 = ohm_valueR1.get()
            int_ohm_valueR1 = int(ohm_valuegetR1)
            ohm_valuegetR2 = ohm_valueR2.get()
            int_ohm_valueR2 = int(ohm_valuegetR2)

            iResult = Label(rechner, text="                       ") # Berechnneten wert wieder auf null setzen
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            R = resistor("P", int_ohm_valueR1, int_ohm_valueR2, 10, 100, 12, 50, 1)
            R.current(R, rechner)

        def enter(event):
            get()

        calc_b = Button(rechner, text="Lösen", command=get)
        calc_b.configure(bg="white")
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)
        rechner.mainloop()

    # Serielle Schaltung
    def seriell():
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # Schaltungsbild einfügen
        seriell_image = Image.open("images/Resistor_ser.png")
        img_open = ImageTk.PhotoImage(seriell_image)
        img_label = Label(image=img_open)
        img_label.place(x=130, y=140)
        img_label.configure(background='white')

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

        def get():
            ohm_valuegetR1 = ohm_valueR1.get()
            int_ohm_valueR1 = int(ohm_valuegetR1)
            ohm_valuegetR2 = ohm_valueR2.get()
            int_ohm_valueR2 = int(ohm_valuegetR2)

            iResult = Label(rechner, text="                       ") # Berechnneten wert wieder auf null setzen
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            R = resistor("S", int_ohm_valueR1, int_ohm_valueR2, 10, 100, 12, 50, 1)
            R.current(R, rechner)
        
        def enter(event):
            get()

        calc_b = Button(rechner, text="Lösen", command=get)
        calc_b.configure(bg="white")
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)
        rechner.mainloop()
    
    # Widerstand auswählen Frame
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    cSelect1 = Label(rechner, text="Ihre Schaltungsart?")
    cSelect1.configure(bg="white")
    cSelect1.place(x=120, y=20)

    parrallel_b = Button(rechner, text="Parralel", command=parallel)
    parrallel_b.configure(bg="white")
    parrallel_b.place(x=100, y=50)

    seriell_b = Button(rechner, text="Seriell", command=seriell)
    seriell_b.configure(bg="white")
    seriell_b.place(x=180, y=50)

# Grenzfrequenz Berechnung Kondensator
def capacitor_calc(rechner):
    # LC Glied
    def LCglied():
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # Schaltungsbild einfügen
        lcPass_image = Image.open("images/LC-pass.png")
        img_open = ImageTk.PhotoImage(lcPass_image)
        img_label = Label(image=img_open)
        img_label.place(x=40, y=155)
        img_label.configure(background='white')

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

        def get():
            henry_valueget = henry_value1.get()
            int_henry_value = int(henry_valueget)
            farad_valueget = farad_value1.get()
            int_farad_value = int(farad_valueget)

            iResult = Label(rechner, text="                       ") # Berechnneten wert wieder auf null setzen
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            C = capacitor("LC", int_farad_value, ohm_valueR1, int_henry_value, 10, 350, 12 ,60 , 1)
            C.current(C, rechner)

        def enter(event):
            get()
        
        calc_b = Button(rechner, text="Lösen", command=get)
        calc_b.configure(bg="white")
        calc_b.place(x=250, y=90)
        rechner.bind('<Return>', enter)
        rechner.mainloop()

    # RC Glied
    def RCglied():
        for widgets in rechner.winfo_children():
            widgets.destroy()


        # Schaltungsbild einfügen
        rcPass_image = Image.open("images/RC-Tiefpass.png")
        img_open = ImageTk.PhotoImage(rcPass_image)
        img_label = Label(image=img_open)
        img_label.place(x=40, y=155)
        img_label.configure(background='white')

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

        def get():
            ohm_valueget = ohm_value1.get()
            int_ohm_value = int(ohm_valueget)
            farad_valueget = farad_value1.get()
            int_farad_value = int(farad_valueget)

            iResult = Label(rechner, text="                       ") # Berechnneten wert wieder auf null setzen
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            C = capacitor("RC", int_farad_value, int_ohm_value, henry, 10, 350, 12 ,60 , 1)
            C.current(C, rechner)

        def enter(event):
            get()

        calc_b = Button(rechner, text="Lösen", command=get)
        calc_b.configure(bg="white")
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)
        rechner.mainloop()

    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    cSelect = Label(rechner, text="Ihre Schaltungsart?")
    cSelect.configure(bg="white")
    cSelect.place(x=120, y=20)

    LC_b = Button(rechner, text="LC Glied", command=LCglied)
    LC_b.configure(bg="white")
    LC_b.place(x=100, y=50)

    RC_b = Button(rechner, text="RC Glied", command=RCglied)
    RC_b.configure(bg="white")
    RC_b.place(x=180, y=50)

# Grenzfrequenz Berechnung Spule
def spool_calc(rechner):
    # LC Glied
    def LCglied():
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # Schaltungsbild einfügen
        lcPass_image = Image.open("images/LC-pass.png")
        img_open = ImageTk.PhotoImage(lcPass_image)
        img_label = Label(image=img_open)
        img_label.place(x=40, y=155)
        img_label.configure(background='white')

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

        def get():
            henry_valueget = henry_value1.get()
            int_henry_value = int(henry_valueget)
            farad_valueget = farad_value1.get()
            int_farad_value = int(farad_valueget)

            iResult = Label(rechner, text="                       ") # Berechnneten wert wieder auf null setzen
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            C = capacitor("LC", int_farad_value, ohm_valueR1, int_henry_value, 10, 350, 12 ,60 , 1)
            C.current(C, rechner)

        def enter(event):
            get()

        calc_b = Button(rechner, text="Lösen", command=get)
        calc_b.configure(bg="white")
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)
        rechner.mainloop()

    # RL Glied
    def RLglied():
        for widgets in rechner.winfo_children():
            widgets.destroy()

        # Schaltungsbild einfügen
        rlPass_image = Image.open("images/rl-Tiefpass.png")
        img_open = ImageTk.PhotoImage(rlPass_image)
        img_label = Label(image=img_open)
        img_label.place(x=40, y=155)
        img_label.configure(background='white')

        rlPass_image = Image.open("images/rl-Tiefpass.png")
        img_open = ImageTk.PhotoImage(rlPass_image)
        img_label = Label(image=img_open)
        img_label.place(x=40, y=155)
        img_label.configure(background='white')

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

        text2 = Label(rechner, text="Spule (mH):")
        text2.configure(bg="white")
        text2.place(x=51, y=70)
        henry_value = Entry(rechner)
        henry_value.place(x=120, y=70)
        farad=0

        def get():
            ohm_valueget = ohm_value1.get()
            int_ohm_value = int(ohm_valueget)
            henry_valueget = henry_value.get()
            int_henry_value = int(henry_valueget)

            iResult = Label(rechner, text="                       ") # Berechnneten wert wieder auf null setzen
            iResult.configure(bg="white")
            iResult.place(x=120, y=90)

            C = capacitor("RC", int_henry_value, int_ohm_value, farad, 10, 350, 12 ,60 , 1)
            C.current(C, rechner)

        def enter(event):
            get()

        calc_b = Button(rechner, text="Lösen", command=get)
        calc_b.configure(background="white")
        calc_b.place(x=250, y= 90)
        rechner.bind('<Return>', enter)
        rechner.mainloop()
    
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    cSelect = Label(rechner, text="Ihre Schaltungsart?")
    cSelect.configure(background="white")
    cSelect.place(x=120, y=20)

    LC_b = Button(rechner, text="LC Glied", command=LCglied)
    LC_b.configure(background="white")
    LC_b.place(x=100, y=50)

    RL_b = Button(rechner, text="RL Glied", command=RLglied)
    RL_b.configure(background="white")
    RL_b.place(x=180, y=50)

# Auswahl fenster
def user_select():
    rechner = Tk()
    rechner.title("Schaltungs Berechner")
    rechner.geometry("350x350")
    rechner.configure(background='white')

    def HTL_link():
        webbrowser.open_new(r"https://htlinn.ac.at/")

    # Logo einfügen
    htl_image = Image.open("images/HTL.jpg")
    img_open = ImageTk.PhotoImage(htl_image)
    img_label = Button(image=img_open, command=HTL_link)
    img_label.place(x=80, y=120)
    img_label.configure(background='white', pady=0, padx=0, bd=0)
    
    cSelect = Label(rechner, text="Was wollen sie berechnen?")
    cSelect.configure(bg="white",font=("Calibri", 15, "bold"))
    cSelect.place(x=55, y=20)

    resistor_b = Button(rechner, text="Widerstand", command=lambda:resistor_calc(rechner))
    resistor_b.configure(bg="white", bd=1)
    resistor_b.place(x=50, y=55)

    capacitor_b = Button(rechner, text="Kondensator", command=lambda:capacitor_calc(rechner))
    capacitor_b.configure(background="white", bd=1)
    capacitor_b.place(x=150, y=55)

    spool_b = Button(rechner, text="Spule", command=lambda:spool_calc(rechner))
    spool_b.configure(background='white',bd=1)
    spool_b.place(x=250, y=55)

    rechner.mainloop()

user_select()