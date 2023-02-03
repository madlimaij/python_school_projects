# ÜLESANNE. Projekt on edasiarendus programmeerimise aluste aine esimese jao projektile.
# Eesmärk oli sama ülesannet lahendada uute teadmiste valguses ning parandada mõned probleemid.
# Programm oli mõeldud tekstide tõlkimise või toimetamisega tegelevale inimesele, ehkki sama asja
# saaks kasutada ka muudel eesmärkidel. Kasutajana soovisin, et saaksin lisada eesti keele
# grammatikareegleid oma valikul ja sõnastuses ning lisada neile töö käigus ette tulevaid näitelauseid.
# Kui peaks näiteks tekkima küsimus des- ja mata-lühendite komade kohta, saab programmi vastava laiema
# õigekeelsuskategooria alla sisestada reegli vabas vormis ja endale kergesti mõistetavalt. Sama lause saab
# lisada näitena. 
# Eelmine programm lõi iga reegli kohta tekstifaili, kus reegel ja näited ei olnud märgistatud ega eristatavad.
# Seekord kasutasin pandase DataFrame'e, kus reasiltideks olid reeglid ja väärtusteks näited. Programmiga käib
# kaasas üks tekstifail sisukorraga (seal on kirjas kategooriad; esimeses programmis oli see samamoodi)
# ning seekord ka tekstifailid eraldi viiele kategooriale*. Igas failis sisaldub tabel selle kategooria reeglitega.
# Tabelis on nõnda reegleid ja näiteid võimalik kergemini ekraanile kuvada.
# Programmis kasutasin lõpuks siiski EasyGUI-d , kuna võrreldes Tkinteriga oli seda kergem minu juba
# valmis kirjutatud programmiga sobitada.


#* Need viis faili on ette valmistatud. Lisatud on ka esimene tühi veerg.

#PROGRAMM
#1. Käskluse valik: sisesta reegel, sisesta näide või loe näiteid.
#2. Kasutaja sisestab sisukorrast vastava teema ehk kategooria numbri. Avame vastava faili ja tabeli. 
#3. Reeglite sisestamine. Kasutaja sisestab reegli valitud kategooria tabelisse.
#4. Näidete sisestamine valitud kategooria valitud reegli alla.
#5. Näidete lugemine.

# PROGRAMM
#1. Kasutaja teeb valiku, kas soovib reegli/näite lisada või seda ekraanile väljastada.
from easygui import *
import pandas as pd

fail_sisukord = open("Sisukord.txt", "r", encoding = "UTF-8") # Sisukord kategooriatega,
                                                            # mille vahel reeglid on jagatud.
                                                            # See on eelnevalt koostatud
                                                            # eesti keele käsiraamatu põhjal (https://www.eki.ee/books/ekk09/index.php?p=2).
sisukord = fail_sisukord.read()
fail_sisukord.close()

variandid = ["Sisestan reegli.", "Sisestan näite.", "Loen."] # Kasutaja valib toimingu.
vajutati = choicebox(sisukord, "Valige tegevus: ", choices = variandid)

#2. Kasutaja sisestab vastava teema ehk kategooria numbri ja avame tabeli.
kat = integerbox(sisukord, "Sisestage kategooria number: ")
# Avan sellele kategooriale vastava eelloodud csv-faili pandase DataFrame'ina.
nimi = "Kategooria" + str(kat) + "_tabel.csv"
tabel = pd.read_csv(nimi, delimiter=';', index_col = [0]) # Viimane argument teeb tabeli ilusamaks, kui eemaldab reasiltide veerult indeksi.

# Funktsioon, mille abil saame tabelist ja seega valitud kategooriast kõik reeglid.
def reeglid_kategoorias(tbl):
    reasildid = tbl.index # saan tabeli ridade sildid
    järjend = list(reasildid) # teen neist järjendi
    seeria = pd.Series(järjend)
    return seeria

#3. Reeglite sisestamine. Kasutaja sisestab reegli valitud kategooria tabelisse.    
if vajutati == "Sisestan reegli.":
    seeria = reeglid_kategoorias(tabel)
    reegel = enterbox("\n".join(seeria), "Reeglid selles kategoorias.", "Sisestage uus reegel siia.")
    tabel.loc[("- " + reegel)] = float("NaN") # lisan tabelisse näideteta rea
    tabel.to_csv(nimi, sep=';', encoding='utf-8') # ---> tabelisse tagasi
    uus_seeria = reeglid_kategoorias(tabel)
    lõpp = msgbox("\n".join(uus_seeria), "Reeglid selles kategoorias", "Lõpeta programmi töö")
    quit()
    
#4. Näidete sisestamine.'
    
if vajutati == "Sisestan näite.":    
    seeria = reeglid_kategoorias(tabel)
    järjend = list(seeria)
    if len(järjend) == 1:  # Choicebox eeldab vähemalt kaht valikut ehk siin kaht või enamat reeglit, millest ka tingimuslause.
        reegli_nr = 0
        näide = enterbox(järjend[0], "Valitud reegel: ", "Sisesta uus näide siia.")
        # Näite sisestamiseks reegli reas sobiva koha leidmine.
        rea_pikkus = len(tabel.iloc[int(reegli_nr)])
        tabel.insert(rea_pikkus, rea_pikkus, float("NaN"))   #Sisestan lisaveeru.
        veeru_indeks = 0
        while pd.isna(tabel.iloc[int(reegli_nr), veeru_indeks]) == False: # Otsib, millises veerus on esimene NaN, kuhu saab uue näite lisada.
            veeru_indeks += 1
        tabel.iloc[int(reegli_nr), veeru_indeks] = näide     #df.iloc[rida, veerg], et lisada väärtus indeksite abil; vs df.loc, mis kasutab silte
        tabel.to_csv(nimi, sep=';', encoding='utf-8')        # ---> tabelisse
        reegli_indx2 = int(reegli_nr)
        näidete_loend2 = list(tabel.iloc[reegli_indx2])
        uus_loend2 = []                                      # loon järjendi, kus poleks NaN-e, kuna .join keeldub neid sidumast.
        for el2 in näidete_loend2:
            if pd.isnull(el2):
                näidete_loend2.remove(el2)
            else:
                uus_loend2.append(el2)
        lõpp2 = msgbox("\n".join(uus_loend2), "Näited selle reegli kohta. ", "Lõpeta programmi töö")
        quit()
    elif len(järjend) > 1:
        reegli_valik = choicebox("Reeglid: ", "Valige reegel: ", choices = järjend)
        reegli_nr = järjend.index(reegli_valik)
        näide = enterbox(reegli_valik, "Valitud reegel: ", "Sisesta uus näide siia.")
        rea_pikkus = len(tabel.iloc[int(reegli_nr)])
        tabel.insert(rea_pikkus, rea_pikkus, float("NaN"))  
        veeru_indeks = 0
        while pd.isna(tabel.iloc[int(reegli_nr), veeru_indeks]) == False:
            veeru_indeks += 1
        tabel.iloc[int(reegli_nr), veeru_indeks] = näide
        tabel.to_csv(nimi, sep=';', encoding='utf-8')  # --->tabelisse
        reegli_indx2 = int(reegli_nr)
        näidete_loend2 = list(tabel.iloc[reegli_indx2])
        uus_loend2 = []
        for el2 in näidete_loend2:
            if pd.isnull(el2):
                näidete_loend2.remove(el2)
            else:
                uus_loend2.append(el2)
        lõpp2 = msgbox("\n".join(uus_loend2), "Näited selle reegli kohta. ", "Lõpeta programmi töö")
        quit()
    else:
        teade = msgbox("Selles kategoorias pole veel reegleid.", "", "Käivita programm uuesti ja lisa reegel.")
        quit()
        
#5. Näidete lugemine.
if vajutati == "Loen.":
    seeria3 = reeglid_kategoorias(tabel)
    järjend3 = list(seeria3)
    if len(järjend3) == 1:
        reegli_indx3 = 0
        näidete_loend3 = list(tabel.iloc[reegli_indx3])
        uus_loend3 = []
        for el3 in näidete_loend3:
            if pd.isnull(el3):
                näidete_loend3.remove(el3)
            else:
                uus_loend3.append(el3)
        lõpp3 = msgbox("\n".join(uus_loend3), "Näited selle reegli kohta. ", "Lõpeta programmi töö")
        quit()
    elif len(järjend3) > 1:
        reegli_valik3 = choicebox("Reeglid: ", "Valige reegel: ", choices = järjend3)
        reegli_nr3 = järjend3.index(reegli_valik3)
        reegli_indx3 = int(reegli_nr3)
        näidete_loend3 = list(tabel.iloc[reegli_indx3])
        uus_loend3 = []
        for el3 in näidete_loend3:
            if pd.isnull(el3):
                näidete_loend3.remove(el3)
            else:
                uus_loend3.append(el3)
        print(uus_loend3)
        lõpp3 = msgbox("\n".join(uus_loend3), "Näited selle reegli kohta. ", "Lõpeta programmi töö")
        quit()
    else:
        teade = msgbox("Selles kategoorias pole veel reegleid.", "", "Käivita programm uuesti ja lisa reegel.")
        quit()
