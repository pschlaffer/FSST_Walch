# --------- Philip Schlaffer & Benedikt Mangott
# --------- 14.03.2022
# --------- FSST - Walch

# ------------------------------------------------------ Libarys
from tkinter import *
import math as m

# ------------------------------------------------------ Klassen
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
        # ------------------------------------------------------ Parralel Schaltung Berechnung
        if (R.select == "P"):
            R12 = (R.ohm_valueR1 * R.ohm_valueR2)/(R.ohm_valueR1 + R.ohm_valueR2)
            R12_round = round(R12, 1)
            if R12_round < 1000:
                R12_new = R12_round, "Ω"
            if R12_round >= 1000:
                R12_new = R12_round * m.pow(10, -3), "kΩ"
            # ------------------------------------------------------ Anzeige
            iResult = Label(rechner, text=R12_new, bg="white")
            iResult.place(x=120, y=90)
        
        # ------------------------------------------------------ Reihen Schaltung Berechnung
        else:
            R12 = R.ohm_valueR1 + R.ohm_valueR2
            if R12 < 1000:
                R12_new = R12, "Ω"
            if R12 >= 1000:
                R12_new = R12 * m.pow(10, -3), "kΩ"
            # ------------------------------------------------------ Anzeige
            iResult = Label(rechner, text=R12_new, bg="white")
            iResult.place(x=120, y=90)
        
        # ------------------------------------------------------ Darkmode
        if rechner['bg'] == "#3C4145":
            switch = "black"
            iResult['bg']  = "#3C4145"
            iResult['fg']  = "white"
        else:
            switch = "white"
class capacitor(components):
    def __init__(self, LCselect, farad_value1, ohm_valueR1, henry_value1, tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self, tolerance, impedance, voltage, frequenz, phi)
        self.LCselect     = LCselect
        self.farad_value1 = farad_value1
        self.ohm_valueR1  = ohm_valueR1
        self.henry_value1 = henry_value1

    def current(self, C, rechner):
        # ------------------------------------------------------ RC Glied
        switch = "white"
        if (C.LCselect == "RC" or C.LCselect == "rc"):
            # ------------------------------------------------------ Berechnung
            nanofarad = (m.pow(10, -9)*C.farad_value1)
            fg = 1/(2*m.pi*C.ohm_valueR1*nanofarad)
            fg_round = round(fg, 0)
            if fg_round < 1000:
                fg_round_new = fg_round, "Hz"
            if fg_round >= 1000:
                fg_round_new = fg_round * m.pow(10, -3), "kHz"
            
            # ------------------------------------------------------ Anzeige
            iResult = Label(rechner, text=fg_round_new, bg="white")
            iResult.place(x=120, y=90)
   
        # ------------------------------------------------------ LC Glied
        else:
            # ------------------------------------------------------ Berechnung
            mHenry    = (m.pow(10, -3)*C.henry_value1)
            nanofarad = (m.pow(10, -9)*C.farad_value1)
            fg = 1/(2*m.pi*m.sqrt(mHenry*nanofarad))
            fg_round = round(fg, 0)
            if fg_round < 1000:
                fg_round_new = fg_round, "Hz"
            if fg_round >= 1000:
                fg_round_new = fg_round * m.pow(10, -3), "kHz"
            
            # ------------------------------------------------------ Anzeige
            iResult = Label(rechner, text=fg_round_new, bg="white")
            iResult.place(x=120, y=90)
            
        # ------------------------------------------------------ Darkmode
        if rechner['bg'] == "#3C4145":
            switch = "black"
            iResult['bg']  = "#3C4145"
            iResult['fg']  = "white"
        else:
            switch = "white"

class spool(components):
    def __init__(self, LCselect, henry_value1, ohm_valueR1, farad_value1,tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self,tolerance, impedance, voltage, frequenz, phi)
        self.LCselect      = LCselect
        self.henry_value1  = henry_value1
        self.ohm_valueR1   = ohm_valueR1
        self.farad_value1  = farad_value1

    def current(self, L, rechner):
        # ------------------------------------------------------ LC Glied
        switch = "white"
        if (L.LCselect == "LC" or L.LCselect == "lc"):
            # ------------------------------------------------------ Berechnung
            mHenry    = (m.pow(10, -3)*L.henry_value1)
            nanofarad = (m.pow(10, -9)*L.farad_value1)
            fg = 1/(2*m.pi*m.sqrt(mHenry*nanofarad))
            fg_round = round(fg, 0)
            if fg_round < 1000:
                fg_round_new = fg_round, "Hz"
            if fg_round >= 1000:
                fg_round_new = fg_round * m.pow(10, -3), "kHz"
            
            # ------------------------------------------------------ Anzeige
            iResult = Label(rechner, text=fg_round_new, bg="white")
            iResult.place(x=120, y=90)
            
        # ------------------------------------------------------ RL Glied
        else:
            # ------------------------------------------------------ Berechnung
            mHenry = (m.pow(10, -3)*L.henry_value1)
            fg = L.ohm_valueR1/(2*m.pi*mHenry)
            fg_round = round(fg, 0)
            if fg_round < 1000:
                fg_round_new = fg_round, "Hz"
            if fg_round >= 1000:
                fg_round_new = fg_round * m.pow(10, -3), "kHz"
            
            # ------------------------------------------------------ Anzeige
            iResult = Label(rechner, text=fg_round_new, bg ="white")
            iResult.place(x=120, y=90)

        # ------------------------------------------------------ Darkmode
        if rechner['bg'] == "#3C4145":
            switch = "black"
            iResult['bg']  = "#3C4145"
            iResult['fg']  = "white"
        else:
            switch = "white"