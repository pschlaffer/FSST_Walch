# Philip Schlaffer
# 16.11.2021
# FSST - Kaiser
import math as m
#test 2356cd
class components:
    def __init__(self,tolerance, impedance, voltage,frequenz, phi):
        self.tolerance    = tolerance
        self.impedance    = impedance
        self.voltage      = voltage
        self.frequenz     = frequenz
        self.phi          = phi

class resistor(components): 
    def __init__(self,ohmvalue, tolerance, impedance, voltage, frequenz, phi):
        components.__init__(self, tolerance, impedance, voltage,frequenz, phi)
        self.ohmvalue   = ohmvalue
    
    def current(self,R):
        iMathI = R.voltage/R.impedance
        iMathI_mA = round((iMathI*1000),3)

        print("Widerstandsstrom I:", iMathI_mA, "[mA]\n")

        user_select()

class capacitor(components):
    def __init__(self, faradvalue, tolerance, impedance, voltage, frequenz, phi):
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

class spool(components):
    def __init__(self, henry, tolerance, impedance, voltage, frequenz, phi):
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

    # Resistor
    if (cSelect == "R" or cSelect == "r"):
        print("Für Exit: [Enter]\n")
        print("Resistor Current Calculator")
        
        u_valueR   = int(input("Spannung in [V]: "))
        imp_valueR = int(input("Impedanz in [Ohm]: "))

        R = resistor(300, 10, imp_valueR, u_valueR, 50, 1)
        R.current(R)

    # Capacitator
    if (cSelect == "C" or cSelect == "c"):
        print("Für Exit: [Enter]\n")
        print("Capacitor Current Calculator")

        umn_sel  = input("Farad in u, n: ")
        if (umn_sel == "u" or umn_sel == "U"):
            farad    = int(input("Farad in [uF]: "))
            farad_n  = farad * 10**-6
        if (umn_sel == "n" or umn_sel == "N"):
            farad    = int(input("Farad in [nF]: "))
            farad_n  = farad * 10**-9   

        u_valueC = int(input("Spannung in [V]: "))
        f_valueC = int(input("Frequenz in [Hz]: "))

        C = capacitor(farad_n, 10, 350, u_valueC ,f_valueC , 1)
        C.current(C)

    # Spool
    if (cSelect == "L" or cSelect == "l"):
        print("Für Exit: [Enter]\n")
        print("Spool Current Calculator")

        henry    = int(input("Henry in [mH]: "))
        u_valueL = int(input("Spannung in [V]: "))
        f_valueL = int(input("Frequenz in [Hz]: "))

        henry_n = henry * 10**-3
        L = spool(henry_n, 15, 400, u_valueL, f_valueL, 1)
        L.current(L)
  
user_select()