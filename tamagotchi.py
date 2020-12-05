class Tamagotchi:
    animo=0
    hambre=0
    energia=0

    def __init__(self,animo,hambre,energia):
        self.animo=animo
        self.hambre=hambre
        self.energia=energia

    def __jugar__(self):
        if self.energia<=0:
            print("Game Over")
        else:
            print("Jugar")
            self.animo+=1
            self.energia-=1

    def __alimentar__(self):
        if self.energia<=0:
            print("Game Over")
        else:
            print("Alimentar")
            self.energia+=1
            self.hambre-=1

    def __dormir__(self):
        if self.energia<=0:
            print("Game Over")
        else:
            print("Dormir")
            self.energia+=1
            self.hambre+=1

    def __pasar__(self):
        if self.energia<=0:
            print("Game Over")
        else:
            print("Pasar tiempo")
            self.energia-=1
            self.hambre+=1
            self.animo-=1

t1 = Tamagotchi(20,0,82)
t2 = Tamagotchi(25,10,60)