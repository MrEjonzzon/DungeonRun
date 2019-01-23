import random
import header
import player

class Battle:
    def roll_dice(self, roll):
        result = int(0)
        i = 0
        while i < roll:
            dice = random.randint(1, 6)
            i = i + 1
            result = result + dice
        return result

    def health_check(self, hero, monster):
        print(hero.name, "has ", hero.endurance, " HP")
        print(monster.name, "has ", monster.endurance, " HP")

    def damage(self, health):
        new_health = health - 1
        return new_health

    def escape(self, agility, mage):
        if mage == 2:
            if player.Mage.ability(player):
                print("Hero escaped from battle")
                return True
            else:
                print("Hero can't escape!")
                return False
        elif (agility*10) <= random.randint(1, 100):
            print("Hero escaped from battle")
            return True
        else:
            print("Hero can't escape!")
            return False

    def attack(self, hero, monster, theif, knight_count):
        hero_attack_value = 0
        monster_agility_value = 0
        hero_agility_value = 0
        monster_attack_value = 0
        hero_attack_value += self.roll_dice(self, hero.attack)
        monster_agility_value += self.roll_dice(self, monster.agility)
        hero_agility_value += self.roll_dice(self, hero.agility)
        monster_attack_value += self.roll_dice(self, monster.attack)

        if hero_attack_value > monster_agility_value:
            if theif == 3:
                if player.Thief.ability(player):
                    print("Hero hit the target, dubble damage")
                    monster.endurance = self.damage(self, monster.endurance)
                    monster.endurance = self.damage(self, monster.endurance)
                else:
                    print("Hero hit the target")
                    monster.endurance = self.damage(self, monster.endurance)
            else:
                monster.endurance = self.damage(self, monster.endurance)
                print("Hero hit the target")
        else:
            print("Hero missed the target")

        if monster_attack_value > hero_agility_value:
            if knight_count == 0:
                print("Knight blocked the attack")
                knight_count += 1
                return knight_count
            else:
                hero.endurance = self.damage(self, hero.endurance)
                print("Monster hit the target")
                return knight_count
        else:
            print("Monster missed")
            return knight_count

    def fight(self, hero, monster):
        header.Battle_design()
        print("You are battling a", monster.name)
        if hero.character == 1:
            knight_count = 0
        else:
            knight_count = 1
        while True:
            if hero.endurance >= 0 and monster.endurance >= 0:
                self.health_check(self, hero, monster)
                print("[1] Fight \n[2] Escape\n")
                choice = int(input())
                if choice == 1:
                    knight_count = self.attack(self, hero, monster, hero.character)
                elif choice == 2:
                    self.escape(self, hero.agility, hero.character)
                else:
                    print("Invalid selection, try again")
            else:
                header.Fight_Winnner()  # print("Battle ended")
                break