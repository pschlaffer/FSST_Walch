# --------- Philip Schlaffer & Benedikt Mangott
# --------- 21.02.2022
# --------- FSST - Walch

# ------------------------------------------------------ Libarys
# ----------------------------- Tkinter
from tkinter import *
from PIL     import ImageTk, Image
# ----------------------------- Open URL
import webbrowser
# ----------------------------- Modules
from packs.mail      import mail_send
from packs.formulas  import formula
from packs.C_calc    import capacitor_calc
from packs.L_calc    import spool_calc
from packs.R_calc    import widerstand
from website.website import website_open

# ------------------------------------------------------ Tkinter Fenster erstellen
rechner = Tk()
rechner.title("Circuit Calculator")
rechner.configure(bg="white")
# ------------------------------------------------------ setzt Hintergrund weiß
darkmode = "white"
# ------------------------------------------------------ setzt Mail sende status null
sended_mail = "no"
# ------------------------------------------------------ leert letzte berechnungen
website_file_latest = open("website/calc_files/latest.txt", "w")

# ------------------------------------------------------ Auswahl fenster
def user_select(darkmode):
    rechner.geometry("350x350")
    # ------------------------------------------------------ Bei Escape schließen
    rechner.bind('<Escape>', lambda el: rechner.destroy())

    # ------------------------------------------------------ Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()

    # ------------------------------------------------------ Logo einfügen
    htl_img = PhotoImage(file = r"images/HTL.png")
    img_label = Button(image=htl_img, command=lambda:webbrowser.open_new(r"https://htlinn.ac.at/"))
    img_label.configure(bg="white", pady=0, padx=0, bd=0, activebackground="white")
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
        lightmode_b = Button(rechner, text="Light Mode", image=light_moon, bg="white", bd=0, command=lambda:dark_switch())
        lightmode_b.place(x=0,y=310)

    # ------------------------------------------------------ Auswahl GUI
    cSelect     = Label(rechner, text="What would you like to calculate?", fg="black", bg="white", font=("Calibri", 15, "bold"))
    cSelect.place(x=40, y=20)

    resistor_b  = Button(rechner, text="Resistor",  bg="white", bd=2, command=lambda:widerstand(rechner, user_select))
    resistor_b.place(x=50, y=55)

    capacitor_b = Button(rechner, text="Capacitor", bg="white", bd=2, command=lambda:capacitor_calc(rechner, user_select))
    capacitor_b.place(x=150, y=55)

    spool_b     = Button(rechner, text="Coil",      bg="white", bd=2, command=lambda:spool_calc(rechner, user_select))
    spool_b.place(x=250, y=55)

    mail_b      = Button(rechner, text="Support",   bg="white", bd=0, command=lambda:mail_send(rechner, user_select, sended_mail))
    mail_b.place(x=150,y=300)

    website_b   = Button(rechner, text="Website",   bg="white", bd=0, command=lambda:website_open())
    website_b.place(x=150,y=320)

    formula_b   = Button(rechner, text="Formulas",  bg='white', bd=0, command=lambda:formula(rechner, user_select))
    formula_b.place(x=292, y=320)

    # ------------------------------------------------------  Light/Darkmode Button Switch
    if darkmode == "black":
        dark_switch()
    else:
        light_switch()

    rechner.mainloop()
user_select(darkmode)