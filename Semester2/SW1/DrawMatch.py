from random import randint, shuffle

class Player:
    def chooseAmount(self, stackSize) -> int:
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError
    
class Human(Player):
    name: str

    def __init__(self):
        self.name = input("Player name: ")

    def __str__(self):
        return self.name
    
    def chooseAmount(self, stackSize):
        while True:
            try:
                amount = int(input(f"{self.name}, amount to draw (1-3): "))
                if amount >= 1 and amount <= 3:
                    return amount
                else:
                    print("Invalid amount")
            except ValueError:
                print("Invalid input")

class Computer(Player):
    name: str
    def __init__(self, name="Computer"):
        self.name = name

    def __str__(self):
        return self.name
    
    def chooseAmount(self, stackSize):
        # Optimal strategy: leave a multiple of 4 for the opponent
        amount = (stackSize - 1) % 4 or randint(1, 3)
        return amount

class MatchGame:
    players: list[Player]
    standings: dict[Player, int] = {}

    def __init__(self, players: list[Player]):
        self.players = players
        for player in self.players:
            self.standings[player] = 0

    def play(self):
        stackSize = randint(10, 20)
        shuffle(self.players)

        while True:
            for player in self.players:
                print()
                print('========O\n'*stackSize)
                amount = player.chooseAmount(stackSize)
                if amount not in [1,2,3]:
                    raise ValueError
                print(player, "draws", amount)
                print()
                stackSize -= amount
                if stackSize <= 0:
                    self.standings[player] += 1
                    print(f"{player} looses")
                    return

players: list[Player] = [Computer(), Computer()]
match = MatchGame(players)

play = True
while play:
    match.play()
    print()
    print("Standings:")
    for player, score in match.standings.items():
        print(player, 'losses:', score)
    print()
    play = input("Play again? (y/n): ") == "y"