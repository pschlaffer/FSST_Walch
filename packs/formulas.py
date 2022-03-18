# --------- Philip Schlaffer & Benedikt Mangott
# --------- 21.02.2022
# --------- FSST - Walch

# ------------------------------------------- Libarys
from tkinter import *

def formula(rechner, user_select):
    # ------------------------------------------- Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    # ------------------------------------------- Formeln GUI
    nt1   = Label(rechner, text="On the following page are the formulas and explenations on how to calculate all\n the highpasses, lowpasses and resistor circuits yourself!", bg="white",font=("Calibri", 12, "bold"), justify = LEFT)
    nt1.place(x=25, y=5)

    res1  = Label(rechner, text="Resistor serial and parallel: ", bg = "white", font=("Calibri", 10, "bold"))
    res1.place(x=40, y=60)

    calc1 = Label(rechner, text="The resistor calculations are simple and can mostly be done by hand!\n For serial resistors you only add up there resistor values [Ohm].\n To calculate TWO parallel resistors you can use the following formula: ", bg = "white", justify = LEFT)
    calc1.place(x=40, y=90)

    rc2   = Label(rechner, text="RC highpass and lowpass: ", bg="white", font=("Calibri", 10, "bold"))
    rc2.place(x=40, y=240)

    calc2 = Label(rechner, text="The RC passes frequencys are a little bit more complicated to calculate.\n (might require a calculator) Regardless of whether you want to calculate\n the high or lowpass you will need this formula for both: ", bg="white", justify = LEFT)
    calc2.place(x=40, y=270)

    rl3   = Label(rechner, text="RC highpass and lowpass: ", bg="white", font=("Calibri", 10, "bold"))
    rl3.place(x=40, y=420)

    calc3 = Label(rechner, text="The RL passes frequency calculations are very similar to the ones above.\n (might require a calculator) The formula is again the same for both\n high and lowpass as follows below: ", bg="white", justify = LEFT)
    calc3.place(x=40, y=450)

    sdnt  = Label(rechner, text="Note: In case a bandpass filter (mix of a high and lowpass filter) has to\n be used or calculated, we recommend to google for a solution. For example\n Electronicbase.net can be usefull here!", bg="white", justify = LEFT)
    sdnt.place(x=40, y=620)
    
    # ------------------------------------------- Formeln
    rc_calc_image = PhotoImage(file=r'images/rPar.png')
    rcc_img = Label(rechner, image=rc_calc_image, bg="white")
    rcc_img.place(x=250, y=150)
    
    rc_pass_image = PhotoImage(file= r'images/rcFormula.png')
    rc_img = Label(rechner, image=rc_pass_image, bg="white")
    rc_img.place(x=250, y=330)
    
    Lc_pass_image = PhotoImage(file = r'images/rlFormula.png')
    Lc_img = Label(rechner, image=Lc_pass_image, bg="white")
    Lc_img.place(x=250, y=510)
    
    # ------------------------------------------- Zurück Option
    switch = "white"
    back_b = Button(rechner, bg="white", text="Close", command=lambda:user_select(switch))
    back_b.place(x=561, y=675)

    # ------------------------------------------- Darkmode
    if rechner['bg'] == "#3C4145":
        for widgets in rechner.winfo_children():
            widgets.configure(bg="#3C4145", fg="white")
        switch="black"
    else:
        switch="white"
    
    # ------------------------------------------- Tkinter Geometry erhöhen
    rechner.geometry("600x700")
    rechner.mainloop()