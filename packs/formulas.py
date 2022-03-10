def calculation():
    # Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    # Formeln
    Lc_pass_image = PhotoImage(file = r'images/rlFormula.png')
    Lc_img = Label(rechner, image=Lc_pass_image, bg="white")
    Lc_img.place(x=40, y=50)

    # Zurück Option
    if rechner['bg'] == "#3C4145":
        back_b = Button(rechner,bg="white", text="Back", command=lambda:user_select("black"))
        back_b.place(x=300, y=320)
    else:
        back_b = Button(rechner,bg="white", text="Back", command=lambda:user_select("black"))
        back_b.place(x=300, y=320)

    # Darkmode
    if rechner['bg'] == "#3C4145":
        Lc_img['bg'] = "#3C4145"
        back_b['bg'] = "#3C4145"

        Lc_img['foreground'] = "white"
        back_b['foreground'] = "white"
 
    rechner.mainloop()

calculation()