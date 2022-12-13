def konsonanOnly(value):
    kalimatbaru = ""
    hurufvokal = ["a","i","u", "e","o", " "]
    for i in value:
        if i not in hurufvokal:
            kalimatbaru += i
    print(kalimatbaru)

konsonanOnly("NurulFikri")
