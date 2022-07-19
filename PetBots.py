from Bots import Bots


class PetBots:
    def main():
        nam = input("Name your pet?\n")
        your_pet = Bots(nam, 10)
        enemy = Bots("Enemy", 10)
        your_pet.get_stats()
        enemy.get_stats()
        while not your_pet.dead and not enemy.dead:
            enemy_turn_over = False
            if enemy.speed > your_pet.speed:
                enemy.action(your_pet)
                enemy_turn_over = True

            your_pet.enemy_def = enemy.base_armor
            enemy.enemy_def = your_pet.base_armor

            end_turn = False
            while not end_turn:
                end_turn = True
                act = int(input("What would you like to do? (type the number in)\n1. Attack\n" +
                                "2. Build Damage\n3. Build Armor\n" +
                                "4. Build Speed\n5. Decrease Attack\n6. Decrease Armor\n7. Decrease Speed\n8. Heal\n" +
                                "9. Get Stats\n"))
                if act == 1:
                    your_pet.attack(enemy)
                elif act == 2:
                    your_pet.build_damage()
                elif act == 3:
                    your_pet.build_armor()
                elif act == 4:
                    your_pet.build_speed()
                elif act == 5:
                    your_pet.decrease_damage(enemy)
                elif act == 6:
                    your_pet.decrease_armor(enemy)
                elif act == 7:
                    your_pet.decrease_speed(enemy)
                elif act == 8:
                    your_pet.heal()
                elif act == 9:
                    your_pet.get_stats()
                    enemy.get_stats()
                    end_turn = False
                else:
                    print("Not a Valid Input")
                    end_turn = False

            your_pet.enemy_def = enemy.base_armor
            enemy.enemy_def = your_pet.base_armor

            if not enemy_turn_over:
                enemy.action(your_pet)

            your_pet.enemy_def = enemy.base_armor
            enemy.enemy_def = your_pet.base_armor

            if your_pet.dead and enemy.dead:
                print("TIE")
                break
            elif your_pet.dead:
                print("YOU LOSE")
                break
            elif enemy.dead:
                print("YOU WIN")
                break

    if __name__ == "__main__":
        main()
