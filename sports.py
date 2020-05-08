class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name,height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


while True:
    new_player = input("Do you want to add a 'Basketball Player' or a 'Football Player'? 'Exit' to leave the program: ")
    if new_player == "Basketball Player".lower():
        f_name = input("Enter player's first name: ")
        l_name = input("Enter player's last name: ")
        height = input("Enter player's height: ")
        weight = input("Enter player's weight: ")
        points = input("Enter the number of player's points: ")
        rebounds = input("Enter the number of player's rebounds: ")
        assists = input("Enter the number of player's assists: ")

        new_basketball_player = BasketballPlayer(first_name=f_name, last_name=l_name, height_cm=height,
                                                 weight_kg=weight, points=points, rebounds=rebounds, assists=assists)

        with open("basketball_player.txt", "a") as basketball_file:
            basketball_file.write(str(new_basketball_player.__dict__))

        print("Player successfully entered!")
        print("Player's data: {0}".format(new_basketball_player.__dict__))

    elif new_player == "Football Player".lower():
        f_name = input("Enter player's first name: ")
        l_name = input("Enter player's last name: ")
        height = input("Enter player's height: ")
        weight = input("Enter player's weight: ")
        goals = input("Enter the number of player's goals: ")
        y_cards = input("Enter the number of player's yellow cards: ")
        r_cards = input("Enter the number of player's red cards: ")

        new_football_player = FootballPlayer(first_name=f_name, last_name=l_name, height_cm=height, weight_kg=float(weight),
                                             goals=goals, yellow_cards=y_cards,red_cards=r_cards)

        with open("football_player.txt", "a") as football_file:
            football_file.write(str(new_football_player.__dict__))

        print("Player successfully entered!")
        print("Player's data: {0}".format(new_football_player.__dict__))

    elif new_player == "Exit".lower():
        print("Leaving the program..........")
        break

    else:
        print("Invalid command")
        print("Please try 'Basketball Player, Football Player, or Exit'.")