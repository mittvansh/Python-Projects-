class Pakuri:

    def __init__(self, species):                #Initialize Pakuri Class
        self.species = species
        self.atk = (len(species) * 7) + 9
        self.dfs = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13
    def get_species(self):
        return self.species             #return attributes

    def get_attack(self):
        return self.atk             #return attack

    def get_defense(self):
        return self.dfs             #return defense

    def get_speed(self):                #return speed
        return self.speed

    def set_attack(self, new_attack):
        self.atk_lvl = new_attack               #set attack value

    def evolve(self):                    #evolve pakuri attributes, defense, attack and speed
        self.atk *= 2
        self.dfs *= 4
        self.speed *= 3