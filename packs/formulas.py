import elektronische_bauteile

def calculation():
    # Alle widgets / labels löschen
    for widgets in rechner.winfo_children():
        widgets.destroy()
    
    # Formeln
    Lc_pass_image = PhotoImage(file = r"images/LC-pass.png")
    img_label2 = Label(image=Lc_pass_image)
    img_label2.configure(background='white')
    img_label2.place(x=40, y=50)

    # Zurück Option
    back_b = Button(rechner, text="Back", command=lambda:user_select(darkmode))
    back_b.configure(bg="white")
    back_b.place(x=300, y=320)

calculation()