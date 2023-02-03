def hinded_sõnastikku(õppeained, hinded):
    sõnastik = {}
    for i in range(len(õppeained)):
        sõnastik[õppeained[i]] = hinded[i]
    return sõnastik

õppeained1 = ["matemaatika", "emakeel", "keemia", "bioloogia", "inglise keel"]
hinded1 = [3, 4, 3, 5, 4]

sõnastik = hinded_sõnastikku(õppeained1, hinded1)

keskmine_hinne = sum(sõnastik.values()) / len(sõnastik)

print("Kõikide ainete keskmine hinna on " + str(keskmine_hinne))
print("Millse hindega õppeaineid soovid näha? ")
hinne = int(input())

if hinne in sõnastik.values():
    for key, value in sõnastik.items():
        if value == hinne:
            print(key)
    else:
        print("Selliseid õppeaineid ei ole.")
