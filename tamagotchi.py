class Tamagotchi:
    animo=0
    hambre=0
    energia=0

    def __init__(self,animo,hambre,energia):
        self.animo=animo
        self.hambre=hambre
        self.energia=energia

    def jugar(self):
        if self.energia<=0:
            print("Game Over")
        else:
            print("Jugar")
            self.animo+=1
            self.energia-=1

    def alimentar(self):
        if self.energia<=0:
            print("Game Over")
        else:
            print("Alimentar")
            self.energia+=1
            self.hambre-=1

    def dormir(self):
        if self.energia<=0:
            print("Game Over")
        else:
            print("Dormir")
            self.energia+=1
            self.hambre+=1

    def pasar(self):
        if self.energia<=0:
            print("Game Over")
        else:
            print("Pasar tiempo")
            self.energia-=1
            self.hambre+=1
            self.animo-=1

    def __str__(self):
        return ("Animo: %d Hambre: %d Energia: %d" %(self.animo,self.hambre,self.energia))

    def mostrarEstado(self):
        print ("Animo: %d Hambre: %d Energia: %d" %(self.animo,self.hambre,self.energia))

t1 = Tamagotchi(20,0,82)
t2 = Tamagotchi(25,10,60)


print(t1)
# t1.mostrarEstado()
# ambos hacen lo mismo, mostar el estado del tamagotchi

t1.jugar()
print(t1)
t1.pasar()
t1.pasar()
t1.dormir()
t1.pasar()
print(t1)
