import sys		#to be able to use sys.argv
from heifer_generator import HeiferGenerator as Heifer		#Pull from heifer_generator.py
def list_cows(cows):		#Function is to show use the cows avaiable in heifer and then print the name. 
    print("Cows available:", end="")
    for cow in cows:
        print(f" {cow.name}", end="")
if __name__ == '__main__':			#main function
    cows = Heifer.get_cows()
    arg = sys.argv
    if sys.argv[1] == '-l':			#logic for -l which prints cows and calls the list_cows function
        list_cows(cows)
        print()
        print()

    elif sys.argv[1] == "-n":			#prints the cow with the message 
        selected_cow = 0
        message = ""
        for cow in cows:
            if sys.argv[2] == cow.name:
                image = cow.image
                selected_cow = 1
        if selected_cow == 0:				#if user's cow is not heifer 
            print(f"Could not find {sys.argv[2]} cow!\n")

        if selected_cow == 1:
            for i in range(3, len(sys.argv)):
                message += (sys.argv[i] + " ")
            print("\n" + message)
            print(image)

    else:				#in case cow is not in heifer
        message = ""
        for i in range(1, len(sys.argv)):
            message += (sys.argv[i] + " ")
        print("\n" + message)
        print(cows[0].image)
