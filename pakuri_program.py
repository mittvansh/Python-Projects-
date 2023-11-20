from pakudex import Pakudex
def pakudex_menu():             #function that prints out the menu
    print("Pakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri")
    print("2. Show Pakuri")
    print("3. Add Pakuri")
    print("4. Evolve Pakuri")
    print("5. Sort Pakuri")
    print("6. Exit")
    print()

bool = True             #boolean used in while loop
#main() method
if __name__ == "__main__":

    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:         #Determine max capacity per the user description
        max = input("Enter max capacity of the Pakudex: ")
        if max.isdigit() == False:      #Check user value
            print("Please enter a valid size.")     #Error message
            continue
        max = int(max)
        if max < 0:     #if max cap negative, error message
            print("Please enter a valid size.")
        elif max >= 0:      #max cap is positive then max value is set
            print(f"The Pakudex can hold {max} species of Pakuri.\n")
            pakudex = Pakudex(max)
            break

    while bool == True:
        pakudex_menu()

        menu_choice = input("What would you like to do? ")
        if menu_choice.isdigit() == False:
            print("Unrecognized menu selection!\n")
            continue
        menu_choice = int(menu_choice)          #make menu_choice into integer

        if menu_choice == 1:
            if pakudex.get_species_array() != None:     #Check if val for array isn't equal to None
                print("Pakuri In Pakudex:")
                count = 1
                for i in pakudex.get_species_array():
                    print(f"{count}. {i}\n")
                    count += 1
            else:
                print("No Pakuri in Pakudex yet!\n")

        elif menu_choice == 2:
            species = input("Enter the name of the species to display: ")
            if pakudex.get_stats(species) != None:      #check is get_stats(species) is none
                stats_list = pakudex.get_stats(species)[:]
                print()
                print(f"Species: {species}")
                print(f"Attack: {stats_list[0]}")
                print(f"Defense: {stats_list[1]}")
                print(f"Speed: {stats_list[2]}")
                print()                 #prints the stats
            else:
                print("Error: No such Pakuri!\n")
                print()         #prints error message if name doesn't match array

        elif menu_choice == 3:
            if pakudex.get_species_array() != None and len(pakudex.get_species_array()) == pakudex.capacity:
                print("Error: Pakudex is full!\n")
                continue
            species = input("Enter the name of the species to add: ")
            if (pakudex.get_species_array() == None) or (species not in pakudex.get_species_array()):
                pakudex.add_pakuri(species)
                print(f"Pakuri species {species} successfully added!\n")
            elif species in pakudex.get_species_array():
                print("Error: Pakudex already contains this species!\n")
        elif menu_choice == 4:
            species = input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(species) == False:
                print("Error: No such Pakuri!")
            else:
                print(f"{species} has evolved!\n")

        elif menu_choice == 5:      #Sort pakuri by species
            pakudex.sort_pakuri()
            print("Pakuri have been sorted!\n")

        elif menu_choice == 6:          #exit program
            print("Thanks for using Pakudex! Bye!")
            bool = False

        else:           #if input for menu option is not defined, this error message is printed
            print("Unrecognized menu selection!\n")