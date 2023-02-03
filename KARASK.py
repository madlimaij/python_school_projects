from easygui import *
def karaski_komponendid(karaski_kogus):
    keefir = 500*karaski_kogus
    print("KEEFIR: " + str(keefir) + " grammi ehk " + str(keefir / 1000) + " kilogrammi")
    if keefir >= 1000:
        print("    See on " + str(keefir / 1000) + " keefiripakki.")
    muna = 1*karaski_kogus
    print("MUNA: " + str(muna) + " tk")
    if muna >= 10:
        print("    See on " + str(muna / 10) + " karpi mune.")
    suhkrut = 1*karaski_kogus
    print("SUHKUR/ MESI: " + str(suhkrut) + " sl")
    odrajahu = 200*karaski_kogus
    print("ODRAJAHU: " + str(odrajahu) + " grammi ehk " + str(odrajahu / 1000) + " kilogrammi")
    if odrajahu >= 1000:
        print("    See on " + str(odrajahu / 1000) + " pakki odrajahu (1kg).")
    rukkijahu = 100*karaski_kogus
    print("TÄISTERA RUKKIJAHU: : " + str(rukkijahu) + " grammi ehk " + str(rukkijahu / 1000) + " kilogrammi")
    if rukkijahu >= 1000:
        print("    See on " + str(rukkijahu / 1000) + " pakki rukkijahu (1kg).")
    soola = 1*karaski_kogus
    print("SOOL: " + str(soola) + " tl")
    soodat = 1.5*karaski_kogus
    print("SOODA: " + str(soodat) + " tl")
    ürte = 2*karaski_kogus
    print("KUIVATATUD ÜRDID: " + str(ürte) + " tl")
    chia_seemneid = 1*karaski_kogus
    print("CHIA SEEMNED: " + str(chia_seemneid) + " sl")
    print("    See on vist " + str(chia_seemneid * 10.2) + " grammi.")
    

küs = input("Mitu karaskit? ")
print()
karaski_komponendid(int(küs))
print("Lisaks kreeka pähkleid")