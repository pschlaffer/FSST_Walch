# --------- Philip Schlaffer & Benedikt Mangott
# --------- 21.02.2022
# --------- FSST - Walch

def calculation():
    # ------------------------------------------- Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    # ------------------------------------------- Formeln
    Lc_pass_image = PhotoImage(file = r'images/rlFormula.png')
    Lc_img = Label(rechner, image=Lc_pass_image, bg="white")
    Lc_img.place(x=40, y=50)
    
    # ------------------------------------------- Zurück Option
    switch = "white"
    back_b = Button(rechner,bg="white", text="Back", command=lambda:user_select(switch))
    back_b.place(x=300, y=320)

    # ------------------------------------------- Darkmode
    if rechner['bg'] == "#3C4145":
        for widgets in rechner.winfo_children():
            widgets.configure(bg="#3C4145", fg="white")
        switch="black"
    else:
        switch="white"
    
    rechner.mainloop()
calculation()