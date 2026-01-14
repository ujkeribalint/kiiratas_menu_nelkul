def testtomegindex():
    tomeg = float(input("Tömeg (kg): "))
    magassag_cm = float(input("Magasság (cm): "))
    magassag_m = magassag_cm / 100
    tti = tomeg / (magassag_m ** 2)
    print("Testtömegindex:", tti)