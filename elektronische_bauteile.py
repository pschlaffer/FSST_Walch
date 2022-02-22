# Philip Schlaffer
# 21.02.2022
# FSST - Walch

import math as m
class components:
    def __init__(self,tolerance, impedance, voltage,frequenz, phi):
        self.tolerance = tolerance
        self.impedance = impedance
        self.voltage   = voltage
        self.frequenz  = frequenz
        self.phi       = phi
        
class resistor(components): 
    def __init__(self, select, ohm_valueR1, ohm_valueR2, tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self, tolerance, impedance, voltage,frequenz, phi)
        self.select = select
        self.ohm_valueR1 = ohm_valueR1
        self.ohm_valueR2 = ohm_valueR2

    def current(self,R):
        iMathI = R.voltage/R.impedance
        iMathI_mA = round((iMathI*1000),3)
        # print("Widerstandsstrom I:", iMathI_mA, "[mA]\n")

        if (R.select == "P"):
            R12 = (R.ohm_valueR1 * R.ohm_valueR2)/(R.ohm_valueR1 + R.ohm_valueR2)
            print("Parellelwiederstand: ", R12, "Ohm")
        else:
            R12 = R.ohm_valueR1 + R.ohm_valueR2
            print("Seriellerwiederstand: ", R12, "Ohm")
        user_select()

class capacitor(components):
    def __init__(self, select, LCselect, farad_value1, ohm_valueR1, henry_value1, tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self, tolerance, impedance, voltage, frequenz, phi)
        self.select = select
        self.LCselect = LCselect
        self.farad_value1 = farad_value1
        self.ohm_valueR1  = ohm_valueR1
        self.henry_value1 = henry_value1

    def current(self, C):
        iMathC = (C.voltage * C.farad_value1 * (2*m.pi*C.frequenz))
        iMathC_mA = round((iMathC*1000),3)
        iMathPHIC = C.phi + (m.pi/2)
        iMathPHIC_round = round(iMathPHIC, 3)
        # print("Kondensatorstrom I: ", iMathC_mA, "[mA]")
        # print("Leistungsfaktor PhiC:", iMathPHIC_round, "\n")
    
        # RC Glied
        if (C.LCselect == "RC" or C.LCselect == "rc"):
            if (C.select == "H"):
                nanofarad = (m.pow(10, -9)*C.farad_value1)
                fg = 1/(2*m.pi*C.ohm_valueR1*nanofarad)
                fg_round = round(fg, 3)
                print("Die Grenzfrequenz beträgt: ", fg_round," Hz")
            else:
                nanofarad = (m.pow(10, -9)*C.farad_value1)
                fg = 1/(2*m.pi*C.ohm_valueR1*nanofarad)
                fg_round = round(fg, 3)
                print("Die Grenzfrequenz beträgt: ", fg_round," Hz")
        
        # LC Glied
        else:
            if (C.select == "H"):
                mHenry    = (m.pow(10, -3)*C.henry_value1)
                nanofarad = (m.pow(10, -9)*C.farad_value1)
                fg = 1/(2*m.pi*m.sqrt(mHenry*nanofarad))
                fg_round = round(fg, 3)
                print("Die Grenzfrequenz beträgt: ", fg_round," Hz")
            else:
                mHenry    = (m.pow(10, -3)*C.henry_value1)
                nanofarad = (m.pow(10, -9)*C.farad_value1)
                fg = 1/(2*m.pi*m.sqrt(mHenry*nanofarad))
                fg_round = round(fg, 3)
                print("Die Grenzfrequenz beträgt: ", fg_round," Hz")
        user_select()

class spool(components):
    def __init__(self, select, LCselect,henry_value1, ohm_valueR1, farad_value1,tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self,tolerance, impedance, voltage, frequenz, phi)
        self.select = select
        self.LCselect = LCselect
        self.henry_value1 = henry_value1
        self.ohm_valueR1  = ohm_valueR1
        self. farad_value1 = farad_value1

    def current(self, L):
        iMathL = L.voltage/((2*m.pi*L.frequenz)*L.henry_value1)
        iMathL_mA = round((iMathL*1000), 3)
        iMathPHIL = L.phi - (m.pi/2)
        iMathPHIL_round = round(iMathPHIL, 3)
        # print("Spulentrom I: ", iMathL_mA, "[mA]")
        # print("Leistungsfaktor PhiL:", iMathPHIL_round, "\n")

        # LC Glied
        if (L.LCselect == "LC" or L.LCselect == "lc"):
            if (L.select == "H"):
                mHenry    = (m.pow(10, -3)*L.henry_value1)
                nanofarad = (m.pow(10, -9)*L.farad_value1)
                fg = 1/(2*m.pi*m.sqrt(mHenry*nanofarad))
                fg_round = round(fg, 3)
                print("Die Grenzfrequenz beträgt: ", fg_round," Hz")
            else:
                mHenry    = (m.pow(10, -3)*L.henry_value1)
                nanofarad = (m.pow(10, -9)*L.farad_value1)
                fg = 1/(2*m.pi*m.sqrt(mHenry*nanofarad))
                fg_round = round(fg, 3)
                print("Die Grenzfrequenz beträgt: ", fg_round," Hz")
        # RC Glied
        else:
            if (L.select == "H"):
                mHenry = (m.pow(10, -3)*L.henry_value1)
                fg = L.ohm_valueR1/(2*m.pi*mHenry)
                fg_round = round(fg, 3)
                print("Die Grenzfrequenz beträgt: ", fg_round," Hz")
            else:
                mHenry = (m.pow(10, -3)*L.henry_value1)
                fg = L.ohm_valueR1/(2*m.pi*mHenry)
                fg_round = round(fg, 3)
                print("Die Grenzfrequenz beträgt: ", fg_round," Hz")

        user_select()

def user_select():
    cSelect = input("Was wollen sie berechen (R, C, L)?: ")

    # Capacitator
    if (cSelect == "C" or cSelect == "c"):
        cpassSelect = input("Hoch (H) o. Tiefpass (T)?: ")
        LCselect = input("LCpass (LC) o. RCpass (RC)?: ")
        capacitor_calc(cpassSelect, LCselect)

    # Resistor
    if (cSelect == "R" or cSelect == "r"):
        cPSelect = input("Parallel (P) o. Seriell (S) Schaltung?: ")
        resistor_calc(cPSelect)

    # Spool
    if (cSelect == "L" or cSelect == "l"):
        spassselect = input("Hoch (H) o. Tiefpass (T)?: ")
        LCselect = input("LCpass (LC) o. RCpass (RC)?: ")
        spool_calc(spassselect, LCselect)

# Widerstandsschaltung Berechnung
def resistor_calc(cPSelect):
    # Parallel Schaltung
    if (cPSelect == "P" or cPSelect == "p"):
        print("\nFür Exit: [Enter]")
        print("Resistor Calculator")
        
        ohm_valueR1 = int(input("Widerstandswert 1: "))
        ohm_valueR2 = int(input("Widerstandswert 2: "))

        R = resistor("P", ohm_valueR1, ohm_valueR2, 10, 100, 12, 50, 1)
        R.current(R)
    
    # Seriell Schaltung
    else:
        print("Serielle Schaltung:")
        ohm_valueR1 = int(input("Widerstandswert 1: "))
        ohm_valueR2 = int(input("Widerstandswert 2: "))
        R = resistor("S", ohm_valueR1, ohm_valueR2, 10, 100, 12, 50, 1)
        R.current(R)

# Hoch u. Tiefpass Berechnung Kondensator
def capacitor_calc(cpassSelect, LCselect):
    # Hochpass
    if (cpassSelect == "H" or cpassSelect == "h"):
        # LC Glied
        if (LCselect == "LC" or LCselect == "lc"):
            print("Für Exit: [Enter]\n")
            print("Capacitor Calculator")

            henry_value1 = int(input("Geben sie den Henrywert ein (mH): "))
            farad_value1 = int(input("Geben sie den Kondensatorwert ein (nF): "))
            ohm_valueR1 = 0

            C = capacitor("H", LCselect, farad_value1, ohm_valueR1, henry_value1, 10, 350, 12 ,60 , 1)
            C.current(C)
        # RC Glied
        else:
            print("Für Exit: [Enter]\n")
            print("Capacitor Calculator")

            farad_value1 = int(input("Geben sie den Kondensatorwert ein (nF): "))
            ohm_valueR1  = int(input("Geben sie den Widerstandswert ein (Ohm): "))
            henry_value1 = 0

            C = capacitor("H", LCselect, farad_value1, ohm_valueR1, henry_value1, 10, 350, 12 ,60 , 1)
            C.current(C)

    # Tiefpass
    else:
        # LC Glied
        if (LCselect == "LC" or LCselect == "lc"):
            print("Für Exit: [Enter]\n")
            print("Capacitor Calculator")

            henry_value1 = int(input("Geben sie den Henrywert ein (mH): "))
            farad_value1 = int(input("Geben sie den Kondensatorwert ein (nF): "))
            ohm_valueR1 = 0

            C = capacitor("H", LCselect, farad_value1, ohm_valueR1, henry_value1, 10, 350, 12 ,60 , 1)
            C.current(C)
        
        # RC Glied
        else:
            print("Für Exit: [Enter]\n")
            print("Capacitor Calculator")

            ohm_valueR1  = int(input("Geben sie den Widerstandswert ein (Ohm): "))
            farad_value1 = int(input("Geben sie den Kondensatorwert ein (nF): "))
            henry_value1 = 0

            C = capacitor("T", LCselect, farad_value1, ohm_valueR1, henry_value1, 10, 350, 12 ,60 , 1)
            C.current(C)

# Hoch u. Tiefpass Berechnung Spule
def spool_calc(spassselect, LCselect):
    # LC Glied
    if (LCselect == "LC" or LCselect == "lc"):
        # Hochpass
        if (spassselect == "H" or spassselect == "h"):
            print("Für Exit: [Enter]\n")
            print("Spool Calculator")

            henry_value1 = int(input("Geben sie den Henrywert ein (mH): "))
            farad_value1 = int(input("Geben sie den Kondensatorwert ein (nF): "))
            ohm_valueR1 = 0

            L = spool("H", LCselect, henry_value1, ohm_valueR1, farad_value1, 15, 400, 12, 60, 1)
            L.current(L)
        # Tiefpass
        else:
            farad_value1 = int(input("Geben sie den Kondensatorwert ein (nF): "))
            henry_value1 = int(input("Geben sie den Henrywert ein (mH): "))
            ohm_valueR1 = 0

            L = spool("T", LCselect, henry_value1, ohm_valueR1, farad_value1 ,15, 400, 12, 60, 1)
            L.current(L)

    # RC Glied
    else:
        # Hochpass
        if (spassselect == "H" or spassselect == "h"):
            print("Für Exit: [Enter]\n")
            print("Spool Calculator")

            henry_value1 = int(input("Geben sie den Henrywert ein (mH): "))
            ohm_valueR1 = int(input("Geben sie den Widerstandswert ein (Ohm): "))
            farad_value1 = 0

            L = spool("H", LCselect, henry_value1, ohm_valueR1, farad_value1, 15, 400, 12, 60, 1)
            L.current(L)
        # Tiefpass
        else:
            henry_value1 = int(input("Geben sie den Henrywert ein (mH): "))
            ohm_valueR1 = int(input("Geben sie den Widerstandswert ein (Ohm): "))
            farad_value1 = 0

            L = spool("T", LCselect, henry_value1, ohm_valueR1, farad_value1 ,15, 400, 12, 60, 1)
            L.current(L)

user_select()