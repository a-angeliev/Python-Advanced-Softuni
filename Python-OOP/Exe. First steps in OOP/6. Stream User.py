class SteamUser:
    def __init__(self, username:str, game: list, player_hours = 0):
        self.username = username
        self.game = game
        self.player_hours = player_hours

    def play(self, game, hours):
        if game in self.game:
            self.player_hours += int(hours)
            return f"{self.username} is playing {game}"
        else:
            return f"{game} is not in library"

    def buy_game(self,game):
        if not game in self.game:
            self.game.append(game)
            return f"{self.username} bought {game}"
        else:
            return f"{game} is already in your library"

    def status(self):
        return f"{self.username} has {len(self.game)} games. Totaly played time: {self.player_hours}"

user = SteamUser("Peter", ["Rainbow Six Siege", "CS:GO", "Fortnite"])
print(user.play("Fortnite", 3))
print(user.play("Oxygen Not Included", 5))
print(user.buy_game("CS:GO"))
print(user.buy_game("Oxygen Not Included"))
print(user.play("Oxygen Not Included", 6))
print(user.status())
