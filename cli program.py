
# Human Life Simulator - CLI Based
# Language: Python

import time
import random

def show_status(name, age, health, energy, money):
    print("\n----------------------------")
    print(f"Name   : {name}")
    print(f"Age    : {age}")
    print(f"Health : {health}")
    print(f"Energy : {energy}")
    print(f"Money  : {money}")
    print("----------------------------\n")

def life_simulator():
    print("Welcome to Human Life Simulator (CLI)")
    name = input("Enter your name: ")

    age = 18
    health = 100
    energy = 100
    money = 50

    while True:
        show_status(name, age, health, energy, money)

        print("Choose an action:")
        print("1. Work")
        print("2. Eat")
        print("3. Sleep")
        print("4. Exercise")
        print("5. Quit Life")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            print("You are working...")
            time.sleep(1)
            money += random.randint(10, 30)
            energy -= 20
            health -= 5

        elif choice == "2":
            print("You are eating food...")
            time.sleep(1)
            health += 10
            energy += 10
            money -= 5

        elif choice == "3":
            print("You are sleeping...")
            time.sleep(1)
            energy += 30
            age += 1

        elif choice == "4":
            print("You are exercising...")
            time.sleep(1)
            health += 15
            energy -= 15

        elif choice == "5":
            print("You quit life. Game Over.")
            break

        else:
            print("Invalid choice!")
            continue

        health = min(health, 100)
        energy = min(energy, 100)

        if health <= 0 or energy <= 0:
            print("\nYour health or energy dropped to zero.")
            print("Game Over.")
            break

        if age >= 60:
            print("\nYou lived a long life.")
            print("Congratulations!")
            break

life_simulator()
