omonat = int(input("omonat: "))

if omonat < 100000:
    print(omonat, " 5%")
elif omonat < 500000:
    print(omonat, "7%")
elif omonat > 500000:
    print(omonat, "10%")