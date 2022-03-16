# --------- Philip Schlaffer & Benedikt Mangott
# --------- 21.02.2022
# --------- FSST - Walch

# ------------------------------------------------------ Libarys
# ----------------------------- Tkinter
from tkinter import *
from PIL import ImageTk, Image
# ----------------------------- OPEN URL
import webbrowser
# ----------------------------- Modules
from packs.calc import *
# ----------------------------- Mail
import packs.mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ------------------------------------------------------ Mail Einstellungen
smtpServer = "smtp.web.de"
smtpPort   = 587
username   = "htl_mangott-schlaffer"
password   = "nibnab01"
sender     = "htl_mangott-schlaffer@web.de"
reciever   = "pschlaffer@tsn.at"

# ------------------------------------------------------ Tkinter Fenster erstellen
rechner = Tk()
rechner.title("Circuit Calculator")
rechner.geometry("350x350")
rechner.configure(bg="white")
darkmode = "white"

# ------------------------------------------------------ Auswahl fenster
def user_select(darkmode):
    # ------------------------------------------------------ Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()

    # ------------------------------------------------------ Logo einfügen
    htl_img = PhotoImage(file = r"images/HTL.png")
    img_label = Button(image=htl_img, command=lambda:webbrowser.open_new(r"https://htlinn.ac.at/"))
    img_label.configure(background="white", pady=0, padx=0, bd=0, activebackground="white")
    img_label.place(x=80, y=100)
    
    # ------------------------------------------------------ Darkmode
    dark_moon = PhotoImage(file = r"images/darkmode.png")
    def dark_switch():
        # ------------------------------------------------------ Set widget colors black
        rechner['bg'] = "#3C4145"
        for widgets in rechner.winfo_children():
            widgets.configure(bg="#3C4145", fg="white")
        img_label['activebackground'] = "#3C4145"

        darkmode_b = Button(rechner, text="Dark Mode", bg="#3C4145", bd=0, activebackground="#3C4145", image=dark_moon, command=lambda:user_select("white"))
        darkmode_b.place(x=0,y=310)

    # ------------------------------------------------------ Light Mode Button
    light_moon  = PhotoImage(file = r"images/lightmode.png")
    def light_switch():
        rechner['bg'] = "white"
        lightmode_b = Button(rechner, text="Light Mode", image=light_moon,bg="white", bd=0, command=lambda:dark_switch())
        lightmode_b.place(x=0,y=310)

    # ------------------------------------------------------ Auswahl menü
    cSelect = Label(rechner, text="What would you like to calculate?", foreground="black", bg="white", font=("Calibri", 15, "bold"))
    cSelect.place(x=40, y=20)

    resistor_b = Button(rechner, text="Resistor", foreground="black", background="white", bd=1, command=lambda:exec(open("packs/R_calc.py").read()))
    resistor_b.place(x=50, y=55)

    capacitor_b = Button(rechner, text="Capacitor", foreground="black", background="white", bd=1, command=lambda:exec(open("packs/C_calc.py").read()))
    capacitor_b.place(x=150, y=55)

    spool_b = Button(rechner, text="Coil", foreground="black", background="white", bd=1, command=lambda:exec(open("packs/L_calc.py").read()))
    spool_b.place(x=250, y=55)

    mail_b = Button(rechner, text="Contakt", foreground="black",background="white", bd=0 ,command=lambda:exec(open("packs/mail.py").read()))
    mail_b.place(x=150,y=320)

    formula_b = Button(rechner, text="Formulas", bg='white', bd=0,command=lambda:exec(open("packs/formulas.py").read()))
    formula_b.place(x=292, y=320)

    # ------------------------------------------------------  Light/Darkmode Button Switch
    if darkmode == "black":
        dark_switch()
    else:
        light_switch()

    rechner.mainloop()
user_select(darkmode)