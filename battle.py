import random
import header

class Battle:

    def roll_dice(self, roll):
        result = int(0)
        i = 0
        while i < roll:
            dice = random.randint(1, 6)
            i = i + 1
            result = result + dice
        return result

    def health_check(self, attacker, victim):
        print(victim.name, "has ", victim.endurance, " HP")
        print(attacker.name, "has ", attacker.endurance, " HP")

    def damage(self, health):
        new_health = health - 1
        return new_health

    def escape(self, agility):
        if (agility*10) <= random.randint(1, 100):
            print("Hero escaped from battle")
            return True
        else:
            print("Hero can't escape!")
            return False

    def attack(self, hero, monster):
        attack_value = 0
        agility_value = 0
        attack_value += self.roll_dice(hero.attack)
        agility_value += self.roll_dice(monster.agility)
        print(attack_value, agility_value)
        if attack_value > agility_value:
            monster.endurance = self.damage(monster.endurance)
            print("Hero attacked")
            hero.endurance = self.damage(hero.endurance)
            print("Monster attacked")
        elif agility_value > attack_value:
            hero.endurance = self.damage(hero.endurance)
            print("Monster attacked")
            monster.endurance = self.damage(monster.endurance)
            print("Hero attacked")
        else:
            print("Attacker missed")

    def fight(self, hero, monster):
        header.Battle_design()
        while True:
            if hero.endurance >= 0 and monster.endurance >= 0:
                choice = int(input("You have entered a battle! \n[1] Fight \n[2] Escape\n"))
                self.health_check(hero, monster)
                if choice == 1:
                    self.attack(hero, monster)
                elif choice == 2:
                    self.escape(self, hero.agility)
                else:
                    print("Invalid selection, try again")
            else:
                header.Fight_Winnner()  # print("Battle ended")
                break