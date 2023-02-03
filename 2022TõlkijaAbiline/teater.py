def loe_saal(failinimi):
    fail = open(failinimi)
    tabel = []
    for rida in fail:
        rida = rida.split(";")
        kohad = []
        for el in rida:
            el = el.strip()
            kohad.append(el)
        tabel.append(kohad)
    return tabel

print(loe_saal("saal.txt"))

faili_nimi = input("Sisestage faili nimi: ")

järjend = loe_saal(faili_nimi)

loendid = []
for rida in järjend:
    print(rida)
    loend = 0
    for el in rida:
        if el == "0":
            loend += 1
    loendid.append(loend)

max_reas = max(loendid)
mitmes_rida = loendid.index(max_reas)

print("Kõige rohkem vabu kohti on " + str(mitmes_rida + 1) + ". reas.")
print(str(mitmes_rida + 1) + ". reas on " + str(max_reas) + " vaba kohta.")
