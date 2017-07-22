import math
import random

#CLASSES
class Player:
    races=['human','ork','dwarf','elf']

    def __init__(self, name, race_nr):
        self.hp=100
        self.name=name
        self.race=self.races[race_nr]
        self.state='alive'

    def introduce(self):
        return ('{} : I am {}, and I am of {} descent'.format(self.name, self.name, self.race))

    def stats(self, class_name, add_stat, stat_points):
            return '{}({}) : HP={}, {}={}'.format(self.name, class_name, self.hp, add_stat, stat_points)

    def atk(self,team,enemy_nr,attack,dmg):
        team.members[enemy_nr].hp-=dmg
        print('{} attacks {} with {} for {} dmg'.format(self.name,team.members[enemy_nr].name,attack,dmg), end='')
        if team.members[enemy_nr].hp <=0 :
            print (' and {} dies!'.format(team.members[enemy_nr].name), end='')
            del team.members[enemy_nr]
            team.size-=1
        print('')
        


class Warrior(Player):
    class_name='warrior'
    weapons=[['axe','sword','mace'],[15,10,20],[15,10,20]]

    def __init__(self,name,race,weapon_nr):
        super().__init__(name,race)
        self.weapon=self.weapons[0][weapon_nr]
        self.dmg=self.weapons[1][weapon_nr]
        self.s_dmg=self.weapons[2][weapon_nr]
        self.sp=50

    def stats(self):
        return super().stats(self.class_name,'SP',self.sp)

    def atk(self, team, enemy_nr):
        self.sp-=self.s_dmg
        return super().atk(team,enemy_nr,self.weapon,self.dmg)


        
class Mage(Player):
    class_name='mage'
    spells=[['fireball','iceball'],[15,10],[15,10]]

    def __init__(self,name,race):
        super().__init__(name,race)
        self.mp=50

    def stats(self):
        return super().stats(self.class_name,'MP',self.mp)

    def atk(self,team,enemy_nr,spell_nr):
        self.mp-=self.spells[2][spell_nr]
        return super().atk(team,enemy_nr,self.spells[0][spell_nr],self.spells[1][spell_nr])

class Team:
    def __init__(self, name):
        self.name=name
        self.size=0
        self.members= []

    def add_member(self, member):
        self.members.append(member)
        self.size+=1

    def stats(self):
        alive=0
        dead=0
        for i in self.members:
            if i.state=='alive':
                alive+=1
            else:
                dead+=1
        return 'Team {} has {} members, {} are alive and {} are dead'.format(self.name,self.size,alive,dead)

    def show_members(self):
        _members='{}: '.format(self.name)
        for i in self.members:
            _members+=i.stats() +', '
        return _members



#MAIN
team1=Team('Mieczywoje')
team2=Team('Skurwiele')

team1.add_member(Warrior('Huj',0,1))
team1.add_member(Mage('Cipa',1))
team1.add_member(Warrior('Dupa',2,2))
team1.add_member(Mage('Cycki',1))

team2.add_member(Warrior('Swag',1,0))
team2.add_member(Mage('Yolo',1))



team1.members[1].atk(team2,0,0)
team2.members[1].atk(team1,1,1)

print(team1.show_members())
print(team2.show_members())










        