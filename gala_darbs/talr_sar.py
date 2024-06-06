# !!! Gala darbs !!!
# Izveidots elementārs konntaktu saraksts - tālruņu katalogs
# Tiek pieņemts, ka personai var būt vairāki unikāli tālruņu numuri
# Kontaktus var izveidot un dzēst, tālruņus var pievienot un dzēst
# Uz ekrāna var izdrukāt visu kontaktu sarakstu vai veikt personas meklēšanu
# Kontaktus var saglabāt datnē un no turienes ielādēt
# Ir paredzēts arī Demo režīms (aktīvs), kurš pievieno dažus kontaktus!

# Agris Ginters
# 06.06.2024

import json
import os

demo_mode=True # Demo režīma aktivizācija
json_datne='gala_darbs\\kontakti.json' # Definē kontaktu datnes atrašanās vietu

class Persona:
    def __init__(self, vards="", talrunis=[]):
        self.vards=vards.title()
        self.talrunis=list(set(talrunis)) # tiek pievienoti tikai unikāli tālruņi
    
    def __str__(self):
        if len(self.talrunis)==0:
            return f"Kontaktam {self.vards} nav tālruņa!"
        elif len(self.talrunis)==1:
            return f"Kontaktam {self.vards} ir tālrunis {self.talrunis[0]}"
        else:
            talr_sar=""
            for tel in self.talrunis:
                talr_sar+=tel + ", "

            talr_sar=talr_sar[:len(talr_sar)-2]
            return f"Kontaktam {self.vards} ir tālruņi {talr_sar}"

    def izdr_Kontakts(self):
        print(self.vards)
        return self

    def plus_talr(self, talrunis=[]):
        self.talrunis+=talrunis
        self.talrunis=list(set(self.talrunis)) # nodrošina unikālu tālruņu pievienošanu
        return self
    
    def dzest_talr(self, talrunis=""):
        try:
            self.talrunis.remove(talrunis)
        except:
            ValueError
        return self

    def personas_vards(self):
        return self.vards    
    

class katalogs:
    def __init__(self):
        self.Kontakts = []

    def plus(self, vards, talrunis=[]):
        i=self.__mekle_pers(vards=vards)
        if i == -1:
            self.Kontakts.append(Persona(vards=vards, talrunis=talrunis))
        else:
            self.Kontakts[i].plus_talr(talrunis=talrunis)
        return self

    def izdruka(self):
        for kont in self.Kontakts:
            if type(kont)!=type:
                print(kont)
        
        if len(self.Kontakts) == 0:
            print("Tālruņu saraksts ir tukšs!")
        return self
    
    def __mekle_pers(self, vards=""):
        i=0
        while i<len(self.Kontakts):
            if self.Kontakts[i].personas_vards().lower()==vards.lower():
                return i
            i+=1
        return -1
    
    def dzest_talr(self, vards="", talrunis=""):
        i=self.__mekle_pers(vards=vards)
        if i>0:
            self.Kontakts[i].dzest_talr(talrunis=talrunis)            
        return self
    
    def dzest_kontaktu(self, vards=""):
        i=self.__mekle_pers(vards=vards)
        if i>0:
            kont=self.Kontakts[i]
            self.Kontakts.remove(kont)
        return self

    def mekle_kontaktu(self, vards=""):
        i=self.__mekle_pers(vards=vards)
        if i>0:
            print(self.Kontakts[i])
        else:
            print(f"Kontakts {vards} netika atrasts!")
        return self
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, ensure_ascii=False)
    

def ierakstit_datus(datne, saraksts):
    with open(datne, 'w', encoding='utf-8') as file:
        file.writelines(saraksts.toJSON())

    print(f"Kontaktu saraksts ir saglabāts [{json_datne}]!")


def nolasit_datus(datne):
    dati=katalogs()
    
    if os.path.isfile(json_datne) == True:
        with open(json_datne, 'r', encoding='utf-8') as file:
            json_kontakti = json.load(file)
        
        for kont in json_kontakti["Kontakts"]:
            dati.plus(kont["vards"], kont["talrunis"])

        print(f"Kontaktu saraksts ir ielādēts no [{json_datne}]!")
    else:
        print(f"Nav atrasta datne [{json_datne}]!")
    return dati


def Demo():
    demo=katalogs()
    demo.plus("Vilis")
    demo.plus("Anita", ['123'])
    demo.plus("Kārlis", ['456', '789'])
    demo.plus("Kārlis", ['0000'])
    demo.plus("Anita", ['123'])
    return demo


kat=katalogs()

if demo_mode == True:
    kat=Demo()

izv=""
while izv.lower() !="q":
    print("----------------------------------------------------------------------------------------------------")
    print("Tālruņu katalogs - izvēlieties darbību: ")
    izv=input("1 - Visi kontakti; 2 - Meklēt; 3 - Pievienot; 4 - Dzēst; 5 - Saglabāt; 6 - Ielādēt; q - Iziet :")
    print("----------------------------------------------------------------------------------------------------")

    if izv == "1":
        kat.izdruka()
    elif izv == "2":
        vards = input("Ievadiet kontakta vārdu: ")
        kat.mekle_kontaktu(vards)
    elif izv == "3":
        talr=[]
        vards = input("Ievadiet kontakta vārdu: ")
        talr.append(input(f"Ievadiet kontakta {vards} tālruni: "))
        kat.plus(vards=vards, talrunis=list(talr))
    elif izv == "4":
        izv=input("1 - Dzēst tālruni; 2 - Dzēst kontaktu :")
        if izv == "1" or izv == "2":
            vards = input("Ievadiet kontakta vārdu: ")
            if izv == "1":
                talr = input(f"Ievadiet kontakta {vards} tālruni: ")
            if izv == "2":
                izv = input(f"Vai tiešām dzēst {vards} visus kontaktus? (Y - Jā): ")
                if izv.lower() == "y":
                    kat.dzest_kontaktu(vards=vards)
            else:
                kat.dzest_talr(vards=vards, talrunis=talr)
        izv="0"
    elif izv == "5":
        ierakstit_datus(json_datne, kat)        
    elif izv == "6":
        kat=nolasit_datus(json_datne)
        


