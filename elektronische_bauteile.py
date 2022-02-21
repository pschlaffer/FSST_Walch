# Philip Schlaffer
# 21.02.2022
# FSST - Walch

import math as m
class components:
    def __init__(self,tolerance, impedance, voltage,frequenz, phi):
        self.tolerance    = tolerance
        self.impedance    = impedance
        self.voltage      = voltage
        self.frequenz     = frequenz
        self.phi          = phi
        
class resistor(components): 
    def __init__(self, select, ohm_valueR1, ohm_valueR2, tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self, tolerance, impedance, voltage,frequenz, phi)
        self.select = select
        self.ohm_valueR1   = ohm_valueR1
        self.ohm_valueR2   = ohm_valueR2

    def current(self,R):
        iMathI = R.voltage/R.impedance
        iMathI_mA = round((iMathI*1000),3)

        print("Widerstandsstrom I:", iMathI_mA, "[mA]\n")

        if (R.select == "P"):
            R12 = (R.ohm_valueR1 * R.ohm_valueR2)/(R.ohm_valueR1 + R.ohm_valueR2)
            print("Parellelwiederstand: ", R12)
        else:
            R12 = R.ohm_valueR1 + R.ohm_valueR2
            print("Seriellerwiederstand: ", R12)
        user_select()

class capacitor(components):
    def __init__(self, select, farad_valueR1, farad_ValueR2, tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self, tolerance, impedance, voltage, frequenz, phi)
        self.faradvalue = faradvalue

    def current(self, C):
        iMathC = (C.voltage * C.faradvalue * (2*m.pi*C.frequenz))
        iMathC_mA = round((iMathC*1000),3)
        iMathPHIC = C.phi + (m.pi/2)
        iMathPHIC_round = round(iMathPHIC, 3)

        print("Kondensatorstrom I: ", iMathC_mA, "[mA]")
        print("Leistungsfaktor PhiC:", iMathPHIC_round, "\n")

        user_select()
    
    def tiefpass(self, C):
        d 
    def hochpass(self, C):
        d

class spool(components):
    def __init__(self, select, henry_valueR1, henry_ValueR2, tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self,tolerance, impedance, voltage, frequenz, phi)
        self.henry    = henry

    def current(self, L):
        iMathL = L.voltage/((2*m.pi*L.frequenz)*L.henry)
        iMathL_mA = round((iMathL*1000), 3)
        iMathPHIL = L.phi - (m.pi/2)
        iMathPHIL_round = round(iMathPHIL, 3)

        print("Spulentrom I: ", iMathL_mA, "[mA]")
        print("Leistungsfaktor PhiL:", iMathPHIL_round, "\n")

        user_select()

def user_select():
    cSelect = input("Was wollen sie berechen (R, C, L)?: ")
    cPSelect = input("Parallel (P) o. Seriell (S) Schaltung?: ")
    # Resistor
    if (cSelect == "R" or cSelect == "r"):
            resistor_calc(cPSelect)

    # Capacitator
    if (cSelect == "C" or cSelect == "c"):
        if (cPSelect == "P" or cPSelect == "p"):
            capacitor_calc()

    # Spool
    if (cSelect == "L" or cSelect == "l"):
        if (cPSelect == "P" or cPSelect == "p"):
            spool_calc()

def resistor_calc(cPSelect):
    if (cPSelect == "P" or cPSelect == "p"):
        print("\nFür Exit: [Enter]")
        print("Resistor Calculator")
        
        ohm_valueR1 = int(input("Geben sie zwei Widerstandwerte ein 1.: "))
        ohm_ValueR2 = int(input("Geben sie zwei Widerstandwerte ein 2.: "))

        R = resistor("P", ohm_valueR1, ohm_valueR2, 10, 100, 12, 50, 1)
        R.current(R)
    else:
        print("Serielle Schaltung:")
        ohm_valueR1 = int(input("Geben sie zwei Widerstandwerte ein 1.: "))
        ohm_valueR2 = int(input("Geben sie zwei Widerstandwerte ein 2.: "))
        R = resistor("S", ohm_valueR1, ohm_valueR2, 10, 100, 12, 50, 1)
        R.current(R)

def capacitor_calc():
    if (cPSelect == "P" or cPSelect == "p"):
        print("Für Exit: [Enter]\n")
        print("Capacitor Calculator")

        farad_valueR1 = int(input("Geben sie zwei Kondensatorwerte ein 1.: "))
        farad_ValueR2 = int(input("Geben sie zwei Kondensatorwerte ein 2.: "))

        C = capacitor("P",farad_valueR1, farad_ValueR2, 10, 350, u_valueC ,f_valueC , 1)
        C.current(C)
    else:
        farad_valueR1 = int(input("Geben sie zwei Kondensatorwerte ein 1.: "))
        farad_ValueR2 = int(input("Geben sie zwei Kondensatorwerte ein 2.: "))

        C = capacitor("S",farad_valueR1, farad_ValueR2, 10, 350, u_valueC ,f_valueC , 1)
        C.current(C)

def spool_calc():
    if (cPSelect == "P" or cPSelect == "p"):
        print("Für Exit: [Enter]\n")
        print("Spool Calculator")

        henry_valueR1 = int(input("Geben sie zwei Henrywerte ein 1.: "))
        henry_ValueR2 = int(input("Geben sie zwei Henrywerte ein 2.: "))

        L = spool("P",henry_valueR1, henry_valueR2, 15, 400, 12, 60, 1)
        L.current(L)
    else:
        henry_valueR1 = int(input("Geben sie zwei Henrywerte ein 1.: "))
        henry_ValueR2 = int(input("Geben sie zwei Henrywerte ein 2.: "))

        L = spool("P",henry_valueR1, henry_valueR2, 15, 400, 12, 60, 1)
        L.current(L)

user_select()