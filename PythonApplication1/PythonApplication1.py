import math
import random

#CLASSES
class Player:
    def __init__(self,name,race):
        self.hp=100
        self.name=name
        self.race=race
        self.state='alive'

    def introduce(self):
        print('I am {name}, and I am of {race} descent'.format(name=self.name,race=self.race))

    def disp_stats(self):
        return 'I am {state} and I have {hp} hp'.format(state=self.state, hp=self.hp)

class Warrior(Player):
    def __init__(self,name,race,weap,dmg):
        super().__init__(name,race)
        self.weapon=weap
        self.dmg=dmg

    def disp_stats(self):
        print(super().disp_stats(),'and I use a {weapon}, that deals {dmg} dmg'.format(weapon=self.weapon, dmg=self.dmg))

    def atk(self,enemy):
        enemy.hp=enemy.hp-self.dmg
        if enemy.hp <=0 :
            enemy.state='dead'
        print("Ouch!!")


        
class Mage(Player):
    def __init__(self,name,race):
        super().__init__(name,race)
        self.mp=50

    def atk_fireball(self,enemy):
        enemy.hp=enemy.hp-10
        self.mp=self.mp-15
        print("Ouch!!")

    def atk_iceball(self,enemy):
        enemy.hp=enemy.hp-self-5
        self.mp=self.mp-10
        print("Ouch!!")


#MAIN
skurczybyk=Warrior('Skurczybyk','Dwarf','Axe', 15)
skurczysyn=Warrior('Skruczysyn','Ork','Sword',10)
jebaniutki=Warrior('Jebaniutki','Human','Mace',20)
mondry=Mage('Mondry','Elf')
inteligent=Mage('Inteligent','Elf')

Team1=[skurczybyk,skurczysyn,mondry]
Team2=[jebaniutki,inteligent]

print('We are Team 1')
for i in Team1:
    i.introduce()
    i.disp_stats()

print("")

print('We are Team 2')
for i in Team2:
    i.introduce()
    i.disp_stats()

print("")








        