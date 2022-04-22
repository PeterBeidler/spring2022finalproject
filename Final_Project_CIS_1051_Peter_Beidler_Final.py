import time
import random
from tkinter import *
from PIL import ImageTk,Image
def roulette_image():
    root = Tk()
    root.title("Roulette Image")
    roulette_image = ImageTk.PhotoImage(Image.open("roulette.jpg"))
    roulette_label = Label(image = roulette_image)
    roulette_label.pack()
    root.mainloop()
def roulette_table():
    final_result = random.randint(1,38)
    if final_result <= 18:
        print("Spinning...")
        time.sleep(0.75)
        print("Spinning...")
        time.sleep(0.75)
        print("Spinning...")
        time.sleep(0.75)
        print("Spinning...")
        time.sleep(0.75)
        print("Spinning...")
        time.sleep(1.75)
        print("\n\n\n\nYou won!!!")
        return 1
    else:
        print("Spinning...")
        time.sleep(0.75)
        print("Spinning...")
        time.sleep(0.75)
        print("Spinning...")
        time.sleep(0.75)
        print("Spinning...")
        time.sleep(0.75)
        print("Spinning...")
        time.sleep(1.75)
        print("\n\n\n\nYou lost :(")
        return 0
welcome_string = "Hello and welcome to the Las Vegas Trail! \nThis is a game developed by Peter Beidler. \nPlease close each pop-up image once you are done viewing to progress the game.\n\nThe objective of this game is simple. You and two friends are going on a Las Vegas roadtrip! \nHere is a picture of beautiful Las Vegas."
for letter in welcome_string:
    print(letter, end='')
    time.sleep(.010)
time.sleep(0.5)
def vegas_image():
    root = Tk()
    root.title("Vegas Image")
    vegas_image = ImageTk.PhotoImage(Image.open("Vegas_Image.jpg"))
    vegas_label = Label(image = vegas_image)
    vegas_label.pack()
    root.mainloop()

vegas_image()
temple_string = "\n\nYou will be starting from the bell tower at Temple University. Here is a picture of your starting point."
time.sleep(2)
for letter in temple_string:
    print(letter, end='')
    time.sleep(.010)
time.sleep(0.5)
def temple_image():
    root = Tk()
    root.title("Temple Image")
    temple_image = ImageTk.PhotoImage(Image.open("Temple_University_Image.jpg"))
    temple_label = Label(image= temple_image)
    temple_label.pack()
    root.mainloop()
temple_image()
time.sleep(2)
friend_string = "\n\nThroughout the trip, you must keep your friends from becoming too discouraged and keep morale high as you travel the country. \nThis is easier said than done.\nEach decision you make will impact the morale of your friends.\n"
for letter in friend_string:
    print(letter, end='')
    time.sleep(.010)
time.sleep(0.5)
car_string = "\nNow it is time to meet your mode of transportation. You will be driving a 2020 Ford Focus!\nLook at how beautiful she is."
for letter in car_string:
    print(letter, end='')
    time.sleep(.010)
time.sleep(0.5)
def car_image():
    root = Tk()
    root.title("Car Image")
    car_image = ImageTk.PhotoImage(Image.open("Ford_Focus_Image.jpg"))
    car_label = Label(image= car_image)
    car_label.pack()
    root.mainloop()
car_image()
time.sleep(2)
objective_string = "\n\nYou have been budgeted $700 for the three of you on this trip.\nThe 2020 Ford Focus can hold 12.4 gallons of gas and drive 450 miles before each refuel.\nIt is recommended that you spend $300 on gas due to a national average of $4.01 per gallon of gas.\nIf you run out of gas before the trip is complete, you will lose the game.\nAll hotels have been paid for.\nThe rest of your money must go towards food, snacks, and entertainment. At the beginning of each day, you will be given the option to get a \nnice meal for breakfast, lunch and dinner, or fast food for all meals.\nChoose wisely.\nFast food is $5 per person, a nice meal is $15 per person.\nSnacks and entertainment keep the morale of the group high.\nIf the morale gets too low and a friend leaves the trip, the game will end as you were unsuccessful in keeping everyone happy."
for letter in objective_string:
    print(letter, end='')
    time.sleep(.010)
time.sleep(0.5)
print("\n")
route_string = "It is time to choose your route. Which route would you like to choose? \n(Remember to close the pop-up image before proceeding)"
for letter in route_string:
    print(letter, end='')
    time.sleep(.010)
time.sleep(2)
def route_image():
    root = Tk()
    root.title("Route Image")
    route_image = ImageTk.PhotoImage(Image.open("Map_Of_Trip.png"))
    route_label = Label(image= route_image)
    route_label.pack()
    root.mainloop()
route_image()
time.sleep(2)
decision = False
while decision ==False:
    route_selection = input("\n\nSelect the route you want to go on(Enter '1' for Route 1, '2' for Route 2, and '3' for Route 3 and then hit Enter): ")
    if route_selection == "1":
        print("\n\nRoute 1 it is! Time to pack your bags and purchase your supplies!")
        decision = True
    elif route_selection =="2":
        print("\n\nRoute 2 it is! Time to pack your bags and purchase your supplies!")
        decision = True
    elif route_selection =="3":
        print("\n\nRoute 3 it is! Time to pack your bags and purchase your supplies!")
        decision = True
    else:
        pass
for _ in range(6):
    print("Packing...")
    time.sleep(1)
packing_string="Packing is complete! Time to get your friends and purchase supplies."
for letter in packing_string:
    print(letter, end='')
    time.sleep(.010)
def losemorale():
    return random.randint(1,350)
def roadtrip1():
    print("\n\n")
    player = input("What is your name? (Press Enter once done): ")
    friend1 = input("What is the name of your first friend? (Press Enter once done): ")
    friend2 = input("What is the name of your second friend? (Press Enter once done): ")
    begin_string = "\nAlright " + player+", " + friend1+", and " + friend2+", " + "it is time to get going! Good luck on your adventure!"
    for letter in begin_string:
        print(letter, end='')
        time.sleep(.010)
    time.sleep(2)
    morale1 = 125
    morale2 = 125
    money = 700
    time.sleep(1)
    tunes =True
    while tunes ==True:
        music = input('\n\nWould you like to purchase unlimited music for the trip for $15? (Type "Yes" for music, Type "No" for no music) ')
        if music == "Yes":
            money = money - 15
            print("Your total money left is: $",money)
            tunes =False
        elif music == "No":
            print("Your total money left is: $",money)
            morale1 = morale1 - 5
            morale2 = morale2 - 5
            tunes =False
        else:
            pass
    time.sleep(1)
    gas= 0
    snacks = 0
    movie = 0
    open = True
    while open:
        print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
        print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
        purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
        if purchase == "Yes":
            want_gas =True
            want_snacks = True
            want_movies = True
            type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
            if type_of_purchase == "1":
                while want_gas ==True:
                    gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                    if gas ==450:
                        print("\nYour tank is already full. You cannot purchase more gas.")
                        want_gas = False
                    elif gas_purchase =="1":
                        print("\nYou now have a full tank to drive.")
                        money = money - 50
                        gas = 450
                        print("Your total money left is: $", money)
                        want_gas = False
                    elif gas_purchase =="2":
                        print("\nYou cannot drive. Purchase gas before friends get angry.")
                        morale1 = morale1 - 5
                        morale2 = morale2 - 5
                        print("Your total money left is: $", money)
                    else:
                        pass
            if type_of_purchase == "2":
                while want_snacks ==True:
                    snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                    if snacks ==30:
                        print("\nNo more snacks can be purchased today.")
                        want_snacks = False
                    elif snack_purchase =="1":
                        print("\nGood Decision. Nobody will go hangry.")
                        money = money -30
                        snacks = 30
                        print("Your total money left is: $", money)
                        want_snacks =False
                    elif snack_purchase =="2":
                        print("\nLet's hope your friends do not go hangry.")
                        morale1 = morale1 - 5
                        morale2 = morale2 - 5
                        want_snacks = False
                    else:
                        pass
            if type_of_purchase =="3":
                while want_movies ==True:
                    movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                    if movie_purchase =="2":
                            print("\nYour total money left is: $", money)
                            want_movies = False
                    if movie_purchase =="1":
                        buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                        if movie ==5:
                            print("\nNo more movies can be purchased at the time.")
                            wnat_movies = False
                        elif buy_movie =="0":
                            print("\nYou just wasted your friends time. I am sure they are not happy.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_movies = False
                        elif buy_movie =="1":
                            print("\nGood choice.")
                            money = money -5
                            movie = movie +1
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="2":
                            print("\nGood choice.")
                            money = money -10
                            movie = movie +2
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="3":
                            print("\nGood choice.")
                            money = money -15
                            movie = movie +3
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="4":
                            print("\nGood choice.")
                            money = money -20
                            movie = movie +4
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="5":
                            print("\nLet's hope you bought some popcorn!")
                            money = money -25
                            movie = movie +5
                            print("Your total money left is: $", money)
                            want_movies = False
                        else:
                            pass
                    else:
                        pass
        elif purchase =="No":
                if gas != 450:
                    print("\nYou need to purchase gas before leaving.")
                    pass
                elif gas ==450:
                    open = False
                    print("\n\nThank you for visiting the store! Now on with your road trip!")
        else:
            pass
    food_day_one =True
    food_day_two = True
    food_day_three = True
    roadtrip=True
    while roadtrip:
        if money <=0:
            time.sleep(2)
            money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
            for letter in money_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            return money
        elif morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        while food_day_one:
            food_day_one_string = input('\n\nWould you like to purchase fast food or nice meals for your breakfast, lunch, and dinner today? (Type "1" for fast food or "2" for nice meals) ')
            if food_day_one_string == "1":
                time.sleep(0.5)
                print("\nFast food it is.")
                money = money - 45
                print("\nMoney Left: $", money)
                morale1 = morale1-15
                morale2 = morale2-15
                food_day_one =False
            elif food_day_one_string =="2":
                time.sleep(0.5)
                print("\nA nice meal it is.")
                money = money - 135
                print("\nMoney Left: $", money)
                food_day_one = False
            else:
                pass
            if money <=0:
                time.sleep(2)
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        print("\n\nNext stop is Hebron Ohio! Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to Hebron Ohio! You are now at a rest stop to get gas and supplies.")
        time.sleep(1)
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        print("\n\nNext stop is St. Louis Illinois! You will be spending the night here. Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to St. Louis Illinois! You will be spending the night here.")
        time.sleep(1)
        for i in range(6):
            print("\nSleeping...")
            time.sleep(1)
        print("\n\nGood morning! Before leaving to start the day, you need to make one quick trip. You are now at a rest stop to get gas and supplies.")
        snacks = 0
        movie = 0
        gas = 0
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
        while food_day_two:
            food_day_two_string = input('\n\nWould you like to purchase fast food or nice meals for your breakfast, lunch, and dinner today? (Type "1" for fast food or "2" for nice meals) ')
            if food_day_two_string == "1":
                time.sleep(0.5)
                print("\nFast food it is.")
                money = money - 45
                print("\nMoney Left: $", money)
                morale1 = morale1-15
                morale2 = morale2-15
                food_day_two =False
            elif food_day_two_string =="2":
                time.sleep(0.5)
                print("\nA nice meal it is.")
                money = money - 135
                print("\nMoney Left: $", money)
                food_day_two = False
            else:
                pass
            if money <=0:
                time.sleep(2)
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)    
        print("\n\nNext stop is Salina Kansas! Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to Salina Kansas! You are now at a rest stop to get gas and supplies.")
        time.sleep(1)
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        print("\n\nNext stop is Denver Colorado! You will be spending the night here. Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\n\nWelcome to Denver Colorado! You will be spending the night here.")
        time.sleep(1)
        for i in range(6):
            print("\nSleeping...")
            time.sleep(1)
        print("\n\nGood morning! Before leaving to start the day, you need to make one quick trip. You are now at a rest stop to get gas and supplies.")
        snacks = 0
        movie = 0
        gas = 0
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                time.sleep(2)
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        while food_day_three:
            food_day_three_string = input('\n\nWould you like to purchase fast food or nice meals for your breakfast, lunch, and dinner today? (Type "1" for fast food or "2" for nice meals) ')
            if food_day_three_string == "1":
                time.sleep(0.5)
                print("\nFast food it is.")
                money = money - 45
                print("\nMoney Left: $", money)
                morale1 = morale1-15
                morale2 = morale2-15
                food_day_three =False
            elif food_day_three_string =="2":
                time.sleep(0.5)
                print("\nA nice meal it is.")
                money = money - 135
                print("\nMoney Left: $", money)
                food_day_three = False
            else:
                pass
            if money <=0:
                time.sleep(2)
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money    
        time.sleep(1)
        print("\n\nNext stop is Salina Utah! Who knew this was such a popular town name (I promise they are real towns on the route for the trip). Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to Salina Utah! You are now at a rest stop to get gas and supplies.")
        time.sleep(1)
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        print("\n\nNext stop is beautiful Las Vegas! You have almost made it, only one more segment to go!!!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        else:
            roadtrip = False
            return money
def roadtrip2():
    print("\n\n")
    player = input("What is your name? (Press Enter once done): ")
    friend1 = input("What is the name of your first friend? (Press Enter once done): ")
    friend2 = input("What is the name of your second friend? (Press Enter once done): ")
    begin_string = "\nAlright " + player+", " + friend1+", and " + friend2+", " + "it is time to get going! Good luck on your adventure!"
    for letter in begin_string:
        print(letter, end='')
        time.sleep(.010)
    time.sleep(2)
    morale1 = 125
    morale2 = 125
    money = 700
    time.sleep(1)
    tunes =True
    while tunes ==True:
        music = input('\n\nWould you like to purchase unlimited music for the trip for $15? (Type "Yes" for music, Type "No" for no music) ')
        if music == "Yes":
            money = money - 15
            print("Your total money left is: $",money)
            tunes =False
        elif music == "No":
            print("Your total money left is: $",money)
            morale1 = morale1 - 5
            morale2 = morale2 - 5
            tunes =False
        else:
            pass
    time.sleep(1)
    gas= 0
    snacks = 0
    movie = 0
    open = True
    while open:
        print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
        print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
        purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
        if purchase == "Yes":
            want_gas =True
            want_snacks = True
            want_movies = True
            type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
            if type_of_purchase == "1":
                while want_gas ==True:
                    gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                    if gas ==450:
                        print("\nYour tank is already full. You cannot purchase more gas.")
                        want_gas = False
                    elif gas_purchase =="1":
                        print("\nYou now have a full tank to drive.")
                        money = money - 50
                        gas = 450
                        print("Your total money left is: $", money)
                        want_gas = False
                    elif gas_purchase =="2":
                        print("\nYou cannot drive. Purchase gas before friends get angry.")
                        morale1 = morale1 - 5
                        morale2 = morale2 - 5
                        print("Your total money left is: $", money)
                    else:
                        pass
            if type_of_purchase == "2":
                while want_snacks ==True:
                    snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                    if snacks ==30:
                        print("\nNo more snacks can be purchased today.")
                        want_snacks = False
                    elif snack_purchase =="1":
                        print("\nGood Decision. Nobody will go hangry.")
                        money = money -30
                        snacks = 30
                        print("Your total money left is: $", money)
                        want_snacks =False
                    elif snack_purchase =="2":
                        print("\nLet's hope your friends do not go hangry.")
                        morale1 = morale1 - 5
                        morale2 = morale2 - 5
                        want_snacks = False
                    else:
                        pass
            if type_of_purchase =="3":
                while want_movies ==True:
                    movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                    if movie_purchase =="2":
                            print("\nYour total money left is: $", money)
                            want_movies = False
                    if movie_purchase =="1":
                        buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                        if movie ==5:
                            print("\nNo more movies can be purchased at the time.")
                            wnat_movies = False
                        elif buy_movie =="0":
                            print("\nYou just wasted your friends time. I am sure they are not happy.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_movies = False
                        elif buy_movie =="1":
                            print("\nGood choice.")
                            money = money -5
                            movie = movie +1
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="2":
                            print("\nGood choice.")
                            money = money -10
                            movie = movie +2
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="3":
                            print("\nGood choice.")
                            money = money -15
                            movie = movie +3
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="4":
                            print("\nGood choice.")
                            money = money -20
                            movie = movie +4
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="5":
                            print("\nLet's hope you bought some popcorn!")
                            money = money -25
                            movie = movie +5
                            print("Your total money left is: $", money)
                            want_movies = False
                        else:
                            pass
                    else:
                        pass
        elif purchase =="No":
                if gas != 450:
                    print("\nYou need to purchase gas before leaving.")
                    pass
                elif gas ==450:
                    open = False
                    print("\n\nThank you for visiting the store! Now on with your road trip!")
        else:
            pass
    food_day_one =True
    food_day_two = True
    food_day_three = True
    roadtrip=True
    while roadtrip:
        if money <=0:
            time.sleep(2)
            money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
            for letter in money_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            return money
        elif morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        while food_day_one:
            food_day_one_string = input('\n\nWould you like to purchase fast food or nice meals for your breakfast, lunch, and dinner today? (Type "1" for fast food or "2" for nice meals) ')
            if food_day_one_string == "1":
                time.sleep(0.5)
                print("\nFast food it is.")
                money = money - 45
                print("\nMoney Left: $", money)
                morale1 = morale1-15
                morale2 = morale2-15
                food_day_one =False
            elif food_day_one_string =="2":
                time.sleep(0.5)
                print("\nA nice meal it is.")
                money = money - 135
                print("\nMoney Left: $", money)
                food_day_one = False
            else:
                pass
            if money <=0:
                time.sleep(2)
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        print("\n\nNext stop is Hebron Ohio! Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, " and ", friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1,  " and ",friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, " and ", friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to Hebron Ohio! You are now at a rest stop to get gas and supplies.")
        time.sleep(1)
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        print("\n\nNext stop is St. Louis Illinois! You will be spending the night here. Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to St. Louis Illinois! You will be spending the night here.")
        time.sleep(1)
        for i in range(6):
            print("\nSleeping...")
            time.sleep(1)
        print("\n\nGood morning! Before leaving to start the day, you need to make one quick trip. You are now at a rest stop to get gas and supplies.")
        snacks = 0
        movie = 0
        gas = 0
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        while food_day_two:
            food_day_two_string = input('\n\nWould you like to purchase fast food or nice meals for your breakfast, lunch, and dinner today? (Type "1" for fast food or "2" for nice meals) ')
            if food_day_two_string == "1":
                time.sleep(0.5)
                print("\nFast food it is.")
                money = money - 45
                print("\nMoney Left: $", money)
                morale1 = morale1-15
                morale2 = morale2-15
                food_day_two =False
            elif food_day_two_string =="2":
                time.sleep(0.5)
                print("\nA nice meal it is.")
                money = money - 135
                print("\nMoney Left: $", money)
                food_day_two = False
            else:
                pass
            if money <=0:
                time.sleep(2)
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        print("\n\nNext stop is Tulsa Oklahoma! Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to Tulsa Oklahoma! You are now at a rest stop to get gas and supplies.")
        time.sleep(1)
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        print("\n\nNext stop is San Jon New Mexico! You will be spending the night here. Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\n\nWelcome to San Jon New Mexico! You will be spending the night here.")
        time.sleep(1)
        for i in range(6):
            print("\nSleeping...")
            time.sleep(1)
        print("\n\nGood morning! Before leaving to start the day, you need to make one quick trip. You are now at a rest stop to get gas and supplies.")
        snacks = 0
        movie = 0
        gas = 0
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        while food_day_three:
            food_day_three_string = input('\n\nWould you like to purchase fast food or nice meals for your breakfast, lunch, and dinner today? (Type "1" for fast food or "2" for nice meals) ')
            if food_day_three_string == "1":
                time.sleep(0.5)
                print("\nFast food it is.")
                money = money - 45
                print("\nMoney Left: $", money)
                morale1 = morale1-15
                morale2 = morale2-15
                food_day_three =False
            elif food_day_three_string =="2":
                time.sleep(0.5)
                print("\nA nice meal it is.")
                money = money - 135
                print("\nMoney Left: $", money)
                food_day_three = False
            else:
                pass
            if money <=0:
                time.sleep(2)
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        print("\n\nNext stop is Joseph City Arizona. Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to Joseph City Arizona! You are now at a rest stop to get gas and supplies.")
        time.sleep(1)
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        print("\n\nNext stop is beautiful Las Vegas! You have almost made it, only one more segment to go!!!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        else:
            roadtrip = False
            return money
def roadtrip3():
    print("\n\n")
    player = input("What is your name? (Press Enter once done): ")
    friend1 = input("What is the name of your first friend? (Press Enter once done): ")
    friend2 = input("What is the name of your second friend? (Press Enter once done): ")
    begin_string = "\nAlright " + player+", " + friend1+", and " + friend2+", " + "it is time to get going! Good luck on your adventure!"
    for letter in begin_string:
        print(letter, end='')
        time.sleep(.010)
    time.sleep(2)
    morale1 = 125
    morale2 = 125
    money = 700
    time.sleep(1)
    tunes =True
    while tunes ==True:
        music = input('\n\nWould you like to purchase unlimited music for the trip for $15? (Type "Yes" for music, Type "No" for no music) ')
        if music == "Yes":
            money = money - 15
            print("Your total money left is: $",money)
            tunes =False
        elif music == "No":
            print("Your total money left is: $",money)
            morale1 = morale1 - 5
            morale2 = morale2 - 5
            tunes =False
        else:
            pass
    time.sleep(1)
    gas= 0
    snacks = 0
    movie = 0
    open = True
    while open:
        print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
        print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
        purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
        if purchase == "Yes":
            want_gas =True
            want_snacks = True
            want_movies = True
            type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
            if type_of_purchase == "1":
                while want_gas ==True:
                    gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                    if gas ==450:
                        print("\nYour tank is already full. You cannot purchase more gas.")
                        want_gas = False
                    elif gas_purchase =="1":
                        print("\nYou now have a full tank to drive.")
                        money = money - 50
                        gas = 450
                        print("Your total money left is: $", money)
                        want_gas = False
                    elif gas_purchase =="2":
                        print("\nYou cannot drive. Purchase gas before friends get angry.")
                        morale1 = morale1 - 5
                        morale2 = morale2 - 5
                        print("Your total money left is: $", money)
                    else:
                        pass
            if type_of_purchase == "2":
                while want_snacks ==True:
                    snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                    if snacks ==30:
                        print("\nNo more snacks can be purchased today.")
                        want_snacks = False
                    elif snack_purchase =="1":
                        print("\nGood Decision. Nobody will go hangry.")
                        money = money -30
                        snacks = 30
                        print("Your total money left is: $", money)
                        want_snacks =False
                    elif snack_purchase =="2":
                        print("\nLet's hope your friends do not go hangry.")
                        morale1 = morale1 - 5
                        morale2 = morale2 - 5
                        want_snacks = False
                    else:
                        pass
            if type_of_purchase =="3":
                while want_movies ==True:
                    movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                    if movie_purchase =="2":
                            print("\nYour total money left is: $", money)
                            want_movies = False
                    if movie_purchase =="1":
                        buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                        if movie ==5:
                            print("\nNo more movies can be purchased at the time.")
                            wnat_movies = False
                        elif buy_movie =="0":
                            print("\nYou just wasted your friends time. I am sure they are not happy.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_movies = False
                        elif buy_movie =="1":
                            print("\nGood choice.")
                            money = money -5
                            movie = movie +1
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="2":
                            print("\nGood choice.")
                            money = money -10
                            movie = movie +2
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="3":
                            print("\nGood choice.")
                            money = money -15
                            movie = movie +3
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="4":
                            print("\nGood choice.")
                            money = money -20
                            movie = movie +4
                            print("Your total money left is: $", money)
                            want_movies = False
                        elif buy_movie =="5":
                            print("\nLet's hope you bought some popcorn!")
                            money = money -25
                            movie = movie +5
                            print("Your total money left is: $", money)
                            want_movies = False
                        else:
                            pass
                    else:
                        pass
        elif purchase =="No":
                if gas != 450:
                    print("\nYou need to purchase gas before leaving.")
                    pass
                elif gas ==450:
                    open = False
                    print("\n\nThank you for visiting the store! Now on with your road trip!")
        else:
            pass
    food_day_one =True
    food_day_two = True
    food_day_three = True
    roadtrip=True
    while roadtrip:
        if money <=0:
            time.sleep(2)
            money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
            for letter in money_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            return money
        elif morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        while food_day_one:
            food_day_one_string = input('\n\nWould you like to purchase fast food or nice meals for your breakfast, lunch, and dinner today? (Type "1" for fast food or "2" for nice meals) ')
            if food_day_one_string == "1":
                time.sleep(0.5)
                print("\nFast food it is.")
                money = money - 45
                print("\nMoney Left: $", money)
                morale1 = morale1-15
                morale2 = morale2-15
                food_day_one =False
            elif food_day_one_string =="2":
                time.sleep(0.5)
                print("\nA nice meal it is.")
                money = money - 135
                print("\nMoney Left: $", money)
                food_day_one = False
            else:
                pass
            if money <=0:
                time.sleep(2)
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        print("\n\nNext stop is Elyria Ohio! Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to Elyria Ohio! You are now at a rest stop to get gas and supplies.")
        time.sleep(1)
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        print("\n\nNext stop is Atkinson Illinois! You will be spending the night here. Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to Atkinson Illinois! You will be spending the night here.")
        time.sleep(1)
        for i in range(6):
            print("\nSleeping...")
            time.sleep(1)
        print("\n\nGood morning! Before leaving to start the day, you need to make one quick trip. You are now at a rest stop to get gas and supplies.")
        snacks = 0
        movie = 0
        gas = 0
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        while food_day_two:
            food_day_two_string = input('\n\nWould you like to purchase fast food or nice meals for your breakfast, lunch, and dinner today? (Type "1" for fast food or "2" for nice meals) ')
            if food_day_two_string == "1":
                time.sleep(0.5)
                print("\nFast food it is.")
                money = money - 45
                print("\nMoney Left: $", money)
                morale1 = morale1-15
                morale2 = morale2-15
                food_day_two =False
            elif food_day_two_string =="2":
                time.sleep(0.5)
                print("\nA nice meal it is.")
                money = money - 135
                print("\nMoney Left: $", money)
                food_day_two = False
            else:
                pass
            if money <=0:
                time.sleep(2)
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        print("\n\nNext stop is York Nebraska! Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to York Nebraska! You are now at a rest stop to get gas and supplies.")
        time.sleep(1)
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        print("\n\nNext stop is Denver Colorado! You will be spending the night here. Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\n\nWelcome to Denver Colorado! You will be spending the night here.")
        time.sleep(1)
        for i in range(6):
            print("\nSleeping...")
            time.sleep(1)
        print("\n\nGood morning! Before leaving to start the day, you need to make one quick trip. You are now at a rest stop to get gas and supplies.")
        snacks = 0
        movie = 0
        gas = 0
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        while food_day_three:
            food_day_three_string = input('\n\nWould you like to purchase fast food or nice meals for your breakfast, lunch, and dinner today? (Type "1" for fast food or "2" for nice meals) ')
            if food_day_three_string == "1":
                time.sleep(0.5)
                print("\nFast food it is.")
                money = money - 45
                print("\nMoney Left: $", money)
                morale1 = morale1-15
                morale2 = morale2-15
                food_day_three =False
            elif food_day_three_string =="2":
                time.sleep(0.5)
                print("\nA nice meal it is.")
                money = money - 135
                print("\nMoney Left: $", money)
                food_day_three = False
            else:
                pass
            if money <=0:
                time.sleep(2)
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        time.sleep(1)
        print("\n\nNext stop is Salina Utah! Buckle up and get ready for the ride!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        gas = 0
        time.sleep(2)
        print("\n\nWelcome to Salina Utah! You are now at a rest stop to get gas and supplies.")
        time.sleep(1)
        open = True
        while open:
            print("\n\nWelcome to the store. You will purchase supplies here. Here is a current look at your supplies: ")
            print("Money: $", money, "\nGas: ", gas, "miles\nSnacks: ", snacks, "\nMovies: ", movie)
            purchase = input("Would you like to purchase any supplies? (Type 'Yes' to purchase supplies and 'No' to not purchase supplies) ")
            if purchase == "Yes":
                want_gas =True
                want_snacks = True
                want_movies = True
                type_of_purchase = input("\n\nType '1' for gas, '2' for snacks, '3' for movies. ")
                if type_of_purchase == "1":
                    while want_gas ==True:
                        gas_purchase = input("\n\nWould you like to purchase a full tank of gas for $50? (Type '1' for yes and '2' for no) ")
                        if gas ==450:
                            print("\nYour tank is already full. You cannot purchase more gas.")
                            want_gas = False
                        elif gas_purchase =="1":
                            print("\nYou now have a full tank to drive.")
                            money = money - 50
                            gas = 450
                            print("Your total money left is: $", money)
                            want_gas = False
                        elif gas_purchase =="2":
                            print("\nYou cannot drive. Purchase gas before friends get angry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            print("Your total money left is: $", money)
                        else:
                            pass
                if type_of_purchase == "2":
                    while want_snacks ==True:
                        snack_purchase = input("\n\nWould you like to purchase a days worth of snacks for $30? (Type '1' for yes and '2' for no) ")
                        if snacks ==30:
                            print("\nNo more snacks can be purchased today.")
                            want_snacks = False
                        elif snack_purchase =="1":
                            print("\nGood Decision. Nobody will go hangry.")
                            money = money -30
                            snacks = 30
                            print("Your total money left is: $", money)
                            want_snacks =False
                        elif snack_purchase =="2":
                            print("\nLet's hope your friends do not go hangry.")
                            morale1 = morale1 - 5
                            morale2 = morale2 - 5
                            want_snacks = False
                        else:
                            pass
                if type_of_purchase =="3":
                    while want_movies ==True:
                        movie_purchase = input("\n\nWould you like to purchase any movies? Each movie is worth $5. (Type '1' to purchase movies and '2' to not purchase any) ")
                        if movie_purchase =="2":
                                print("\nYour total money left is: $", money)
                                want_movies = False
                        if movie_purchase =="1":
                            buy_movie = input("\n\nHow many movies would you like to buy? (Type the number of movies you would like to buy with a maximum of 5 movies per store trip and press enter to proceed) ")
                            if movie ==5:
                                print("\nNo more movies can be purchased at the time.")
                                wnat_movies = False
                            elif buy_movie =="0":
                                print("\nYou just wasted your friends time. I am sure they are not happy.")
                                morale1 = morale1 - 5
                                morale2 = morale2 - 5
                                want_movies = False
                            elif buy_movie =="1":
                                print("\nGood choice.")
                                money = money -5
                                movie = movie +1
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="2":
                                print("\nGood choice.")
                                money = money -10
                                movie = movie +2
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="3":
                                print("\nGood choice.")
                                money = money -15
                                movie = movie +3
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="4":
                                print("\nGood choice.")
                                money = money -20
                                movie = movie +4
                                print("Your total money left is: $", money)
                                want_movies = False
                            elif buy_movie =="5":
                                print("\nLet's hope you bought some popcorn!")
                                money = money -25
                                movie = movie +5
                                print("Your total money left is: $", money)
                                want_movies = False
                            else:
                                pass
                        else:
                            pass
            elif purchase =="No":
                    if gas != 450:
                        print("\nYou need to purchase gas before leaving.")
                        pass
                    elif gas ==450:
                        open = False
                        print("\n\nThank you for visiting the store! Now on with your road trip!")
            else:
                pass
            if money <=0:
                money_lose_string = "\n\n\n\nWe regret to inform you that you have spent all of your money on the roadtrip. You will be unable to complete the trip to Las Vegas. Thank you for playing!"
                for letter in money_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip = False
                return money
        print("\n\nNext stop is beautiful Las Vegas! You have almost made it, only one more segment to go!!!")
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        print("\nOn the road...")
        time.sleep(0.5)
        print("\nOn the road...")
        time.sleep(0.5)
        result =losemorale()
        if result == 1 or result == 2 or result ==3:
            print("\n\nOh no. Looks like", friend1, "ate something that did not sit well with them. With two frequent rest stops", friend2, "has become frustrated.")
            morale2= morale2-20
            time.sleep(2)
        elif result == 4 or result == 5:
            print("\n\nOh no. Looks like", friend2, "ate something that did not sit well with them. With two frequent rest stops", friend1, "has become frustrated.")
            morale1= morale1-20
            time.sleep(2)
        elif result == 6 or result == 7 or result ==8 or result ==9 or result ==10 or result == 11 or result ==12:
            print("\n\nBad weather causes the trip to take three extra hours. Both friends get a little irritated.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==13:
            print("\n\nMassive earthquake casues a rift in the road. There is no way pass. Your road trip has abruptly ended.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result == 14 or result == 15 or result ==16 or result ==17 or result ==18 or result ==19 or result ==20:
            print("\n\nYour friends get into a political debate. This is the worst possible topic of conversation for a road trip. Both feel unsatisfied after discussion.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 21 or result ==22:
            print("\n\nYour favorite sports team has lost. The vibes in the car are at an all time low.")
            morale1 = morale1 -5
            morale2 = morale2-5
            time.sleep(2)
        elif result ==23 or result ==24 or result ==25 or result ==26 or result ==27:
            print("\n\nOh no! Your third best friend has called you and asked what you were doing. You had to break the news to them that they were not invited.", friend1, "and", friend2, "feel guilty.")
            morale1 = morale1 -15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 28 or result ==29 or result ==30:
            print("\n")
            print("\n")
            print(friend1, "'s mother is not happy they went on this trip unannounced.", friend1, "now must acknowledge they are in a world of pain when they get home.")
            morale1 = morale1-25
            time.sleep(2)
        elif result == 31 or result == 32 or result ==33:
            print("\n")
            print("\n")
            print(friend2, "'s mother is not happy they went on this trip unannounced and made this known on the phone.", friend2, "now must acknowledge they are in a world of pain when they get home.")
            morale2 = morale2-25
            time.sleep(2)
        elif result == 34 or result == 35:
            print("\n")
            print("\n")
            print(friend1, "made a joke that did not sit well with others.", friend2, "is not happy with their decision making.")
            morale2 = morale2-10
            time.sleep(2)
        elif result == 36 or result == 37:
            print("\n")
            print("\n")
            print(friend2, "made a joke that did not sit well with others.", friend1, "is not happy with their decision making.")
            morale1 = morale1-10
            time.sleep(2)
        elif result == 44 or result ==45:
            print("\n\n")
            print(friend1, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale1 = morale1-20
            time.sleep(2)
        elif result ==46 or result ==47:
            print("\n\n")
            print(friend2, "'s boss calls them into work. While they do not have to go in, they do feel bad about letting their boss down.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 48 or result ==49 or result ==50:
            print("\n\n")
            print(friend1, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale1 = morale1-20
            time.sleep(2)
        elif result == 51 or result ==52 or result ==53:
            print("\n\n")
            print(friend2, "'s dogsitter cancelled last minute. It is very stressful to find a replacement, but eventually one is found.")
            morale2 = morale2-20
            time.sleep(2)
        elif result == 54 or result ==55 or result ==56:
            print("\n\nNo service in the car for more than an hour. Your friends go insane because we are all addicted to the Internet.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 57 or result ==58 or result ==59:
            print("\n\n")
            print(player, "spills their drinks and snacks in the car. Both", friend1, friend2, "get angry at", player,".")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 60 or result ==61 or result ==62:
            print("\n\n")
            print(player, "forgot to take their trash out and now the car smells bad. Both", friend1, friend2, "get angry at", player)
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 63 or result ==64 or result ==65 or result ==66 or result ==67 or result ==68 or result ==69:
            print("\n\nRoad closed ahead. Add another 3 hours of driving.")
            morale1 = morale1-10
            morale2 = morale2-15
            time.sleep(2)
        elif result == 70 or result ==71 or result ==72 or result ==73 or result ==74 or result ==75 or result ==76 or result ==77 or result ==78 or result ==79 or result ==80 or result ==81 or result ==82 or result ==83 or result ==84 or result ==85 or result ==86 or result ==87 or result ==88:
            print("\n\nTraffic adds another 3 hours. Friends get upset.")
            morale1 = morale1-10
            morale2 = morale2-10
            time.sleep(2)
        elif result ==90 or result ==91:
            print("\n\nYou get into a car accident. Thankfully everyone is alright, but your trip no longer is.")
            morale1 = morale1-1000
            morale2 = morale2-1000
            time.sleep(2)
            if morale1 <=0:
                time.sleep(2)
                friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend1_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
            elif morale2 <=0:
                time.sleep(2)
                friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
                for letter in friend2_lose_string:
                    print(letter, end='')
                    time.sleep(.010)
                roadtrip =False
                money = 0
                return money
        elif result ==92 or result ==93 or result ==94 or result ==95 or result ==96 or result ==97:
            print("\n\nSome car almost veers into you driving recklessly. While you are all safe, it is still very unsettling.")
            morale1 = morale1-15
            morale2 = morale2-15
            time.sleep(2)
        elif result == 98 or result ==99 or result ==100:
            print("\n\nYou have somehow caught every red light in a small town with no traffic. How is this even possible. Frustration grows.")
            morale1 = morale1-20
            morale2 = morale2-20
            time.sleep(2)
        elif result == 101 or result ==102 or result ==103 or result ==104 or result ==105 or result ==106 or result ==107:
            print("\n\n")
            print (friend1, "'s phone has died. They are not happy.")
            morale1 = morale1-15
            time.sleep(2)
        elif result == 108 or result ==109 or result ==110 or result ==111 or result ==112 or result ==113 or result ==114:
            print("\n\n")
            print (friend2, "'s phone has died. They are not happy.")
            morale2 = morale2-15
            time.sleep(2)
        else:
            pass
        if morale1 <=0:
            time.sleep(2)
            friend1_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend1, " is too low. ", friend1,  " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend1_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        elif morale2 <=0:
            time.sleep(2)
            friend2_lose_string = "\n\n\n\nWe regret to inform you that the morale of ", friend2, " is too low. ", friend2, " has decided to leave the roadtrip. You are not able to continue and will not make it to Las Vegas. Thank you for playing!"
            for letter in friend2_lose_string:
                print(letter, end='')
                time.sleep(.010)
            roadtrip =False
            money = 0
            return money
        else:
            roadtrip = False
            return money
if route_selection =="1":
    result =roadtrip1()
    if result >0:
        print("\n\n")
        print("\n\n")
        print("\n\n")
        print("\n\n")
        vegas_image()
        vegas_finish_string =("\n\nWelcome to Las Vegas!!!! You made it to your destination! \n\nBefore we let you guys go and have a good time, here is your total money left from the trip: $", result, "\n\nSince we are in Vegas I have one final question, would you like to spin a roulette wheel to see if you can double your money?")
        for letter in vegas_finish_string:
            print(letter, end='')
            time.sleep(.010)
        time.sleep(10)
        roulette_image()
        time.sleep(2)
        spin = True
        while spin:
            roulette = input("\nWould you like to spin the roulette wheel? (Type '1' to play and '0' to not play): ")
            if roulette =="1":
                print("\n\nHere we go! Good luck!!")
                roulette_game = roulette_table()
                if roulette_game ==1:
                    print("\n\nCongratulations!!!!! You have just doubled your road trip money for Las Vegas! You now have an additional $", result*2, " to spend in Las Vegas. Thank you very much for playing and have fun on your trip (Do not worry about getting home)")
                    print("\n\nThe end. Thank you!!")
                if roulette_game ==0:
                    print("\n\nWe are sorry you did not win. At least you had a good road trip right? (Do not worry about getting home)")
                    print("\n\nThank you for playing! The end.")
                spin = False
            elif roulette =="0":
                print("\n\nAlright, thank you very much for playing! Use that money wisely and have fun in Las Vegas, you made it (and do not worry how to get home, that is a later issue)")
                print("\n\nThe end. Thank you!")
                spin = False
            else:
                pass
    else:
        print("\nThe end.")
elif route_selection =="2":
    result = roadtrip2()
    if result > 0:
        print("\n\n")
        print("\n\n")
        print("\n\n")
        print("\n\n")
        vegas_image()
        vegas_finish_string =("\n\nWelcome to Las Vegas!!!! You made it to your destination!\n\nBefore we let you guys go and have a good time, here is your total money left from the trip: $", result, "\n\nSince we are in Vegas I have one final question, would you like to spin a roulette wheel to see if you can double your money?")
        for letter in vegas_finish_string:
            print(letter, end='')
            time.sleep(.010)
        time.sleep(10)
        roulette_image()
        time.sleep(2)
        spin = True
        while spin:
            roulette = input("\nWould you like to spin the roulette wheel? (Type '1' to play and '0' to not play): ")
            if roulette =="1":
                print("\n\nHere we go! Good luck!!")
                roulette_game = roulette_table()
                if roulette_game ==1:
                    print("\n\nCongratulations!!!!! You have just doubled your road trip money for Las Vegas! You now have an additional $", result*2, " to spend in Las Vegas. Thank you very much for playing and have fun on your trip (Do not worry about getting home)")
                    print("\n\nThe end. Thank you!!")
                if roulette_game ==0:
                    print("\n\nWe are sorry you did not win. At least you had a good road trip right? (Do not worry about getting home)")
                    print("\n\nThank you for playing! The end.")
                spin = False
            elif roulette =="0":
                print("\n\nAlright, thank you very much for playing! Use that money wisely and have fun in Las Vegas, you made it (and do not worry how to get home, that is a later issue)")
                print("\n\nThe end. Thank you!")
                spin = False
            else:
                pass
    else:
        print("\nThe end.")
elif route_selection =="3":
    result =roadtrip3()
    if result >0:
        print("\n\n")
        print("\n\n")
        print("\n\n")
        print("\n\n")
        vegas_image()
        vegas_finish_string =("\n\nWelcome to Las Vegas!!!! You made it to your destination!\n\nBefore we let you guys go and have a good time, here is your total money left from the trip: $", result, "\n\nSince we are in Vegas I have one final question, would you like to spin a roulette wheel to see if you can double your money?")
        for letter in vegas_finish_string:
            print(letter, end='')
            time.sleep(.010)
        time.sleep(10)
        roulette_image()
        time.sleep(2)
        spin = True
        while spin:
            roulette = input("\nWould you like to spin the roulette wheel? (Type '1' to play and '0' to not play): ")
            if roulette =="1":
                print("\n\nHere we go! Good luck!!")
                roulette_game = roulette_table()
                if roulette_game ==1:
                    print("\n\nCongratulations!!!!! You have just doubled your road trip money for Las Vegas! You now have an additional $", result*2, " to spend in Las Vegas. Thank you very much for playing and have fun on your trip (Do not worry about getting home)")
                    print("\n\nThe end. Thank you!!")
                if roulette_game ==0:
                    print("\n\nWe are sorry you did not win. At least you had a good road trip right? (Do not worry about getting home)")
                    print("\n\nThank you for playing! The end.")
                spin = False
            elif roulette =="0":
                print("\n\nAlright, thank you very much for playing! Use that money wisely and have fun in Las Vegas, you made it (and do not worry how to get home, that is a later issue)")
                print("\n\nThe end. Thank you!")
                spin = False
            else:
                pass
    else:
        print("\nThe end.")


  

#CITATIONS
#https://youtu.be/NoTM8JciWaQ
#https://docs.python.org/3/library/time.html
