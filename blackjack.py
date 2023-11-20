from p1_random import P1Random

rng = P1Random()

game_continue = True
game_num = 1
player_wins = 0
deal_wins = 0
game_tie = 0

while game_continue:
    print(f"START GAME #{game_num}\n")
    game_num += 1
    player_hand = 0
    card = rng.next_int(13) + 1
    if card == 1:
        print("Your card is a ACE!")
        card = 1
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
    elif card == 11:
        print("Your card is a JACK!")
        card = 10
    elif card == 12:
        print("Your card is a QUEEN!")
        card = 10
    elif card == 13:
        print("Your card is a KING!")
        card = 10
    player_hand += card
    print(f"Your hand is: {player_hand}\n")
    no_winner = True
    while no_winner:
        print("1. Get another card \n2. Hold hand \n3. Print statistics \n4. Exit \n")
        option = int(input("Choose an option: "))
        if option == 1:
            card = rng.next_int(13) + 1
            if card == 1:
                print("\nYour card is a ACE!")
                card = 1
            elif 2 <= card <= 10:
                print(f"\nYour card is a {card}!")
            elif card == 11:
                print("\nYour card is a JACK!")
                card = 10
            elif card == 12:
                print("\nYour card is a QUEEN!")
                card = 10
            elif card == 13:
                print("\nYour card is a KING!")
                card = 10
            player_hand += card
            print(f"Your hand is: {player_hand}\n")
            if player_hand == 21:
                print("BLACKJACK! You win!")
                player_wins += 1
                no_winner = False
            elif player_hand > 21:
                print("You exceeded 21! You lose.")
                deal_wins += 1
                no_winner = False
            pass
        elif option == 2:
            dealer_hand = rng.next_int(11) + 16
            if dealer_hand > 21:
                print(f"Dealer's hand: {dealer_hand} \nYour hand is: {player_hand}" + "\n" + "\nYou win!\n")
                player_wins += 1
            elif dealer_hand == player_hand:
                game_tie += 1
                print(f"Dealer's hand: {dealer_hand} \nYour hand is: {player_hand}" + "\n" + "\nIt's a tie! No one wins!\n")
            elif player_hand < dealer_hand <= 21:
                print(f"Dealer's hand: {dealer_hand} \nYour hand is: {player_hand}" + "\n" + "\nDealer wins!\n")
                deal_wins += 1
            elif dealer_hand < player_hand <= 21:
                print(f"Dealer's hand: {dealer_hand} \nYour hand is: {player_hand}" + "\n" + "\nYou win!\n")
            print(f"START GAME #{game_num}\n")
            game_num += 1
            player_hand = 0
            card = rng.next_int(13) + 1
            if card == 1:
                print("Your card is a ACE!")
                card = 1
            elif 2 <= card <= 10:
                print(f"Your card is a {card}!")
            elif card == 11:
                print("Your card is a JACK!")
                card = 10
            elif card == 12:
                print("Your card is a QUEEN!")
                card = 10
            elif card == 13:
                print("Your card is a KING!")
                card = 10
            player_hand += card
            print(f"Your hand is: {player_hand}\n")
            no_winner = True

        elif option == 3:
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {deal_wins}")
            print(f"Number of tie games: {game_tie}")
            total_loss = deal_wins + game_tie
            print(f"Total # of games played is: {player_wins + total_loss}")
            pp_wins = (player_wins / (player_wins + total_loss)) * 100
            print(f"Percentage of Player wins: {pp_wins}%\n")

        elif option == 4:
            no_winner = False
            game_continue = False

        else:
            print("Invalid input! \nPlease enter an integer value between 1 and 4.\n")

