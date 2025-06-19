a = float(input("1-tomon uzunligini kiriting: "))
b = float(input("2-tomon uzunligini kiriting: "))
c = float(input("3-tomon uzunligini kiriting: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Uchburchak teng tomonli.")
    elif a == b or a == c or b == c:
        print("Uchburchak teng yonli.")
    else:
        print("Uchburchak turli tomonli.")
else:
    print("Bunday uchburchak mavjud emas.")
