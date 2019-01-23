import random


class Battle:

    def roll_dice(self, roll):
        result = int(0)
        i = 0
        while i < roll:
            dice = random.randint(1, 6)
            i = i + 1
            result = result + dice
        return result

    def health_check(self, victim, health):
        print(victim.name, "has ", health, " HP")


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

    def attack(self, health, attack, agility):
        attack_value = 0
        agility_value = 0
        attack_value += self.roll_dice(self, attack)
        agility_value += self.roll_dice(self, agility)
        print(attack_value, agility_value)
        if attack_value > agility_value:
            self.damage(self, health)
        else:
            print("Attacker missed")

    def fight(self, hero, monster):
        current_hero_health = hero.endurance
        current_monster_health = monster.endurance

        while True:
            if current_hero_health > 0 and current_monster_health > 0:
                choice = int(input("You have entered a battle! \n[1] Fight \n[2] Escape\n"))
                self.health_check(self, monster, current_monster_health)
                if choice == 1:
                    self.attack(self, current_monster_health, hero.attack, monster.agility)
                elif choice == 2:
                    self.escape(self, hero.agility)

                else:
                    print("Invalid selection, try again")
            else:
                print("Battle ended")
                break

