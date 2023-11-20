from pakuri import Pakuri           #import Pakuri class from pakuri.py 
class Pakudex:
    def __init__(self, capacity = 20):          #initialize Pakudex class 
        self.capacity = capacity
        self.pakudex = []

    def get_size(self):                 #return size 
        return len(self.pakudex)

    def get_capacity(self):                 #return capacity 
        return self.capacity

    def get_species_array(self):                    #return species from the array 
        if self.pakudex:
            return [pakuri.get_species() for pakuri in self.pakudex]
        else:
            return None

    def get_stats(self, species):               #return stats 
        for pakuri in self.pakudex:
            if pakuri.get_species() == species:
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None

    def sort_pakuri(self):                      #sort the list of pakuri in terms of species
        self.pakudex.sort(key=lambda pakuri: pakuri.get_species())

    def add_pakuri(self, species):                  #add new pakuri and handle errors if they are full or already contain the new species 
        if self.get_size() < self.capacity:
            for pakuri in self.pakudex:
                if pakuri.get_species() == species:
                    print(f"Error: Pakudex already contains this species!")
                    return False

            new_pakuri = Pakuri(species)
            self.pakudex.append(new_pakuri)
            return True
        else:
            print("Error: Pakudex is full!")
            return False

    def evolve_species(self, species):              #evolve the species of pakuri and increase stats 
        for pakuri in self.pakudex:
            if pakuri.get_species() == species:
                pakuri.evolve()
                return True
        return False