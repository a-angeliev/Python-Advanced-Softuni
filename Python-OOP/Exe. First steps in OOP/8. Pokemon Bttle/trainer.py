from pokemon import Pokemon


class Trainer:
    def __init__(self, name: str, pokemons=[]):
        self.name = name
        self.pokemons = pokemons

    def add_pokemon(self, pokemon):
        pokem = pokemon.name
        health = pokemon.health
        if pokemon in self.pokemons:
            return "This pokemon in already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokem} with health {health}"

    def release_pokemon(self, pokemon_name:str):
        flag = False
        for el in self.pokemons:
            if pokemon_name in el.name:
                self.pokemons.remove(el)
                flag = True
                return f"You have released {pokemon_name}"
        if not flag:
            return f"Pokemon is not caught"

    def trainer_data(self):
        data = ""
        for el in self.pokemons:
            data += f"-{el.name} with health {el.health}\n"
        return f"Pokemon Trainer {self.name}\n Pokemon count {len(self.pokemons)}\n {data}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
