

class Persona:
    tests="11"
    def __init__(self, vards="", talrunis=[]):
        self.vards=vards
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
    

class kat_sar:
    def __init__(self):
        self.Kontakts = [Persona]

    def plus(self, vards, talrunis=[]):
        i=self.mekle_pers(vards=vards)
        if i == -1:
            self.Kontakts.append(Persona(vards=vards, talrunis=talrunis))
        else:
            self.Kontakts[i].plus_talr(talrunis=talrunis)
        return self

    def izdruka(self):
        for kont in self.Kontakts:
            if type(kont)!=type:
                print(kont)
        return self
    
    def mekle_pers(self, vards=""):
        i=1
        while i<len(self.Kontakts):
            if self.Kontakts[i].personas_vards().lower()==vards.lower():
                return i
            i+=1
        return -1
    
    def dzest_talr(self, vards="", talrunis=""):
        i=self.mekle_pers(vards=vards)
        if i>0:
            self.Kontakts[i].dzest_talr(talrunis=talrunis)
        return self
    
    def dzest_kontaktu(self, vards=""):
        i=self.mekle_pers(vards=vards)
        if i>0:
            kont=self.Kontakts[i]
            self.Kontakts.remove(kont)
        return self
    

tt=kat_sar()
tt.plus("Vilis")
tt.plus("Anita", ['123'])
tt.plus("Kārlis", ['456', '789'])
tt.plus("Kārlis", ['0000'])
tt.plus("Anita", ['123'])

tt.izdruka()

tt.dzest_talr("Kārlis", '0000')
tt.dzest_talr("Kārlis", '0000')

tt.izdruka()

tt.dzest_kontaktu("Vilis")

tt.izdruka()

# katalogs = [Persona]


# katalogs.append(Persona(vards='Līga'))
# katalogs.append(Persona(vards='Pēteris', talrunis=['1111']))
# katalogs.append(Persona(vards='Juris', talrunis=['2364', '12345']))

# print(katalogs[0])
# print(katalogs[1])
# print(katalogs[2])
# print(katalogs[1].personas_vards())

# kat=Persona(vards="Dita", talrunis=['789'])

# katalogs[2].Kontakts()



