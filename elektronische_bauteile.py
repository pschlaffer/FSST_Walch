# Philip Schlaffer & Benedikt Mangott
# 21.02.2022
# FSST - Walch

# Libarys
from tkinter import *
from PIL import ImageTk, Image
import math as m
import webbrowser
import packs.mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Mail Einstellungen
smtpServer = "smtp.web.de"
smtpPort   = 587
username   = "htl_mangott-schlaffer"
password   = "nibnab01"

sender    = "htl_mangott-schlaffer@web.de"
reciever1 = "philip@schlaffers.at"
reciever2 = "bmangott@tsn.at"
reciever3 = "mangottbenni@gmail.com"

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
            
            # Rechner Neustarten
            if rechner['bg'] == "#3C4145":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("black"))
                new_calc.configure(bg="white")
                new_calc.place(x=250, y=118)
            
            if rechner['bg'] == "white":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("white"))
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

            # Rechner Neustarten
            if rechner['bg'] == "#3C4145":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("black"))
                new_calc.configure(bg="white")
                new_calc.place(x=250, y=118)
            
            if rechner['bg'] == "white":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("white"))
                new_calc.configure(bg="white")
                new_calc.place(x=250, y=118)
        
        # Darkmode
        if rechner['bg'] == "#3C4145":
            iResult['bg']  = "#3C4145"
            new_calc['bg'] = "#3C4145"

            iResult['foreground']  = "white"
            new_calc['foreground'] = "white"

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
   
            # Rechner Neustarten
            if rechner['bg'] == "#3C4145":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("black"))
                new_calc.configure(bg="white")
                new_calc.place(x=250, y=118)
            
            if rechner['bg'] == "white":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("white"))
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

            # Rechner Neustarten
            if rechner['bg'] == "#3C4145":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("black"))
                new_calc.configure(bg="white")
                new_calc.place(x=250, y=118)
            
            if rechner['bg'] == "white":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("white"))
                new_calc.configure(bg="white")
                new_calc.place(x=250, y=118)
        
        # Darkmode
        if rechner['bg'] == "#3C4145":
            iResult['bg']  = "#3C4145"
            new_calc['bg'] = "#3C4145"

            iResult['foreground']  = "white"
            new_calc['foreground'] = "white"

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
            
            # Rechner Neustarten
            if rechner['bg'] == "#3C4145":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("black"))
                new_calc.configure(bg="white")
                new_calc.place(x=250, y=118)
            
            if rechner['bg'] == "white":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("white"))
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

            # Rechner Neustarten
            if rechner['bg'] == "#3C4145":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("black"))
                new_calc.configure(bg="white")
                new_calc.place(x=250, y=118)
            
            if rechner['bg'] == "white":
                new_calc = Button(rechner, text="Neu", command=lambda:user_select("white"))
                new_calc.configure(bg="white")
                new_calc.place(x=250, y=118)
        
        # Darkmode 
        if rechner['bg'] == "#3C4145":
            iResult['bg']  = "#3C4145"
            new_calc['bg'] = "#3C4145"

            iResult['foreground']  = "white"
            new_calc['foreground'] = "white"

# Tkinter Fenster erstellen
rechner = Tk()
rechner.title("Schaltungs Berechner")
rechner.geometry("350x350")
rechner.configure(background="white")
rechner['bg'] = "white"
darkmode = "white"

# Auswahl fenster
def user_select(darkmode):
    # Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()

    # Webbroser öffnen mit HTL Seite
    def HTL_link():
        webbrowser.open_new(r"https://htlinn.ac.at/")

    # Set TK Fenster white
    rechner ['bg'] = "white"

    # Logo einfügen
    htl_img = PhotoImage(file = r"images/HTL.png")
    img_label = Button(image=htl_img, command=HTL_link)
    img_label.place(x=80, y=120)
    img_label.configure(background="white", pady=0, padx=0, bd=0, activebackground="white")
    
    lightmode_b = 0
    
    # Dark Mode
    dark_moon  = PhotoImage(file = r"images/darkmode.png")
    def dark_switch(lightmode_b):
        # Delete Lightmode Button
        if lightmode_b != 0:
            lightmode_b.destroy()
        
        # Set widget colors black
        resistor_b['bg']  = "#3C4145"
        capacitor_b['bg'] = "#3C4145"
        spool_b['bg']     = "#3C4145"
        img_label['bg']   = "#3C4145"
        rechner['bg']     = "#3C4145"
        cSelect['bg']     = "#3C4145"
        mail_b['bg']      = "#3C4145"

        # Set Button active background
        img_label['activebackground'] = "#3C4145"

        # Set text colors white
        cSelect['foreground']     = "white"
        resistor_b['foreground']  = "white"
        capacitor_b['foreground'] = "white"
        spool_b['foreground']     = "white"
        mail_b['foreground']      = "white"

        # Create Darkmode Button
        darkmode_b = Button(rechner, text="Dark Mode", image=dark_moon, command=lambda:user_select("white"))
        darkmode_b.configure(bg="#3C4145", bd=0, activebackground="#3C4145")
        darkmode_b.place(x=0,y=310)

    light_moon  = PhotoImage(file = r"images/lightmode.png")
    # Light Mode Button
    def light_switch():
        lightmode_b = Button(rechner, text="Light Mode", image=light_moon, command=lambda:dark_switch(lightmode_b))
        lightmode_b.configure(bg="white", bd=0)
        lightmode_b.place(x=0,y=310)

    # Auswahl menü
    cSelect = Label(rechner, text="Was wollen sie berechnen?", foreground="black")
    cSelect.configure(bg="white", font=("Calibri", 15, "bold"))
    cSelect.place(x=55, y=20)

    resistor_b = Button(rechner, text="Widerstand", foreground="black", command=lambda:exec(open("packs/R_calc.py").read()))
    resistor_b.configure(bg='white', bd=1)
    resistor_b.place(x=50, y=55)

    capacitor_b = Button(rechner, text="Kondensator", foreground="black", command=lambda:exec(open("packs/L_calc.py").read()))
    capacitor_b.configure(background="white", bd=1)
    capacitor_b.place(x=150, y=55)

    spool_b = Button(rechner, text="Spule", foreground="black", command=lambda:exec(open("packs/spool.py").read()))
    spool_b.configure(background="white", bd=1)
    spool_b.place(x=250, y=55)

    mail_b = Button(rechner, text="Kontakt", foreground="black", command=lambda:exec(open("packs/mail.py").read()))
    mail_b.configure(bg="white", bd=0)
    mail_b.place(x=150,y=320)

    if darkmode == "black":
        dark_switch(lightmode_b)
    else:
        light_switch()

    rechner.mainloop()

user_select(darkmode)