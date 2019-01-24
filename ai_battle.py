import random
import header
import player
import map

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

    def attack(self, hero, monster, knight_count):
        hero_attack_value = 0
        monster_agility_value = 0
        hero_agility_value = 0
        monster_attack_value = 0
        hero_attack_value += self.roll_dice(hero.attack)
        monster_agility_value += self.roll_dice(monster.agility)
        hero_agility_value += self.roll_dice(hero.agility)
        monster_attack_value += self.roll_dice(monster.attack)

        if hero_attack_value > monster_agility_value:
            if hero.name == "Thief":
                if player.Thief.ability(player):
                    print("Hero hit the target, double damage")
                    monster.endurance = self.damage(monster.endurance)
                    monster.endurance = self.damage(monster.endurance)
                else:
                    print("Hero hit the target")
                    monster.endurance = self.damage(monster.endurance)
            else:
                monster.endurance = self.damage(monster.endurance)
                print("Hero hit the target")
        else:
            print("Hero missed the target")

        if monster_attack_value > hero_agility_value:
            if knight_count == 0:
                print("Knight blocked the attack")
                knight_count += 1
                return knight_count
            else:
                hero.endurance = self.damage(hero.endurance)
                print("Monster hit the target")
                return knight_count
        else:
            print("Monster missed")
            return knight_count

    def fight(self, character, monster):
        header.Battle_design()
        print("You are battling a", monster.name)
        if character.hero.name == "Knight":
            knight_count = 0
        else:
            knight_count = 1
        if character.hero.endurance >= 1 and monster.endurance >= 1:
            self.health_check(character.hero, monster)
            self.attack(character.hero, monster, knight_count)
            header.Fight_Winnner()  # print("Battle ended")





