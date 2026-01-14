def uzemanyag():
    fogy = float(input("Fogyasztás (l/100km): "))
    ar = float(input("Benzin ára (Ft/l): "))
    ut = float(input("Út hossza (km): "))

    liter = (fogy / 100) * ut
    koltseg = liter * ar
    print("Üzemanyagköltség:", koltseg, "Ft")