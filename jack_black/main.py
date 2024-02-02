import tkinter as tk
import random as r
import time as t
import cards

root = tk.Tk()
root.title("Quadratic\u00ae Casino\u2122 Blackjack\u2122\u00ae")
root.minsize(250, 100)

deck = []

player_score = 0
dealer_score = 0

money = 1000
current_bet = 0

def main():
    place_bets()

    root.mainloop()

def place_bets():
    global bet_entry
    global current_bet

    current_bet = 0
    
    for child in root.winfo_children():
        child.destroy()

    if money == 0:
        debt_label = tk.Label(text="You are out of money, and thus have nothing more to gamble, unfortunately.").grid(sticky=tk.N)
    elif money < 0:
        debt_label = tk.Label(text="""You have bet more money than was in your possession.
                              You are now in crippling debt which you will be forced to work to repay for the rest of your life."""
                              ).grid(sticky=tk.N)
    else:
        bet_label = tk.Label(text=f"You have ${money}.\nPlace your bets, folks:")
        bet_entry = tk.Entry()
        bet_button = tk.Button(text="Go", command=proceed_to_game)

        bet_label.grid(row=0, columnspan=3, sticky=tk.N)
        bet_entry.grid(row=1, columnspan=3, sticky=tk.N)
        bet_button.grid(row=2, column=1, sticky=tk.S)

def proceed_to_game():
    global current_bet

    try:
        current_bet = int(bet_entry.get())
    except:
        return
    
    begin_game_phase()

def begin_game_phase():
    global card_label
    global player_display
    global dealer_display
    global button_container
    global bet_label
    global player_score
    global dealer_score
    global deck
    global money

    deck = cards.reshuffle()

    player_score = 0
    dealer_score = 0
    for child in root.winfo_children():
        child.destroy()

    card_label = tk.Label(text="Starting cards are being dealt...")
    display_container = tk.Frame()
    player_display = tk.Label(display_container, text="0", font=("Arial", 25, "bold"))
    dealer_display = tk.Label(display_container, text="0", font=("Arial", 25, "bold"))
    player_text = tk.Label(display_container, text="Player")
    dealer_text = tk.Label(display_container, text="Dealer")
    button_container = tk.Frame()
    hit_button = tk.Button(button_container, text="Hit", command=lambda: take_turn(True))
    stand_button = tk.Button(button_container, text="Stand", command=lambda: take_turn(False))
    bet_label = tk.Label(text=f"${current_bet} is riding on this game.")

    card_label.grid(row=0, columnspan=3, sticky=tk.N)
    display_container.grid(row=1, columnspan=4, sticky=tk.N)
    player_display.grid(row=0, columnspan=2, sticky=tk.W)
    dealer_display.grid(row=0, column=2, columnspan=2, sticky=tk.E)
    player_text.grid(row=1, column=0, columnspan=2, sticky=tk.W)
    dealer_text.grid(row=1, column=2, columnspan=2, sticky=tk.E)
    button_container.grid(row=2, columnspan=3, sticky=tk.S)
    hit_button.grid(row=0, sticky=tk.W)
    stand_button.grid(row=0, column=1, sticky=tk.E)
    bet_label.grid(row=1, column=4, sticky=tk.E)

    
    for button in button_container.winfo_children():
        button.config(state="disabled")

    root.update()
    t.sleep(2)
    take_turn(True)
    root.update()
    t.sleep(1)
    take_turn(True)
    root.update()
    t.sleep(1)
    dealer_turn()

    
    for button in button_container.winfo_children():
        button.config(state="active")

    if player_score == 21:
        card_label.config(text="Player has Blackjack, and subsequently wins!")
        bet_label.config(text=bet_label.cget("text") + "\nYou are refunded twice the bet!")
        money += current_bet
        button_container.destroy()
        tk.Button(text="Rematch?", command=place_bets).grid(row=2, columnspan=3, sticky=tk.S)

def take_turn(hit):
    global player_score
    global money

    if hit:
        new_suit, new_type, new_value = draw_card()

        new_text=f"Player draws {new_type} of {new_suit}"
        if new_value != -1:
            player_score += new_value
            new_text += "."
        elif player_score > 10:
            player_score += 1
            new_text += ".\nAs 11 would cause them to bust it counts as 1."
        else:
            player_score += 11
            new_text += "."

        if player_score > 21:
            new_text += "\nPlayer busts! Dealer wins."
            bet_label.config(text=bet_label.cget("text") + "\nThe bet is lost.")
            money -= current_bet
            button_container.destroy()
            tk.Button(text="Rematch?", command=place_bets).grid(row=2, columnspan=3, sticky=tk.S)

        card_label.config(text=new_text)
        player_display.config(text=player_score)

    else:
        for button in button_container.winfo_children():
            button.config(state="disabled")

        dealer_active = True
        while dealer_active:
            t.sleep(1)
            dealer_active = dealer_turn()
            root.update()

        t.sleep(1)
        if player_score > 21 or dealer_score > 21:
            pass
        elif player_score == dealer_score:
            if player_score > 19:
                card_label.config(text="It is a tie!")
                bet_label.config(text=bet_label.cget("text") + "\nThe bet is returned unchanged.")
            else:
                card_label.config(text="As scores are tied below 20, the dealer wins!")
                bet_label.config(text=bet_label.cget("text") + "\nThe bet is lost.")
                money -= current_bet
        elif player_score > dealer_score:
            card_label.config(text=f"Player wins with a score of {player_score}!")
            bet_label.config(text=bet_label.cget("text") + "\nYou are refunded twice the bet!")
            money += current_bet
        else:
            card_label.config(text=f"Dealer wins with a score of {dealer_score}!")
            bet_label.config(text=bet_label.cget("text") + "\nThe bet is lost.")
            money -= current_bet

        button_container.destroy()
        tk.Button(text="Rematch?", command=place_bets).grid(row=2, columnspan=3, sticky=tk.S)  

def dealer_turn():
    global card_label
    global dealer_score
    global money

    new_suit, new_type, new_value = draw_card()
    new_text=f"Dealer draws {new_type} of {new_suit}"
    if new_value != -1:
        dealer_score += new_value
        new_text += "."
    elif dealer_score > 10:
        dealer_score += 1
        new_text += ".\nAs 11 would cause them to bust it counts as 1."
    else:
        dealer_score += 11
        new_text += "."

    if dealer_score > 21:
        new_text += "\nDealer busts! Player wins."
        bet_label.config(text=bet_label.cget("text") + "\nYou are refunded twice the bet!")
        money += current_bet
        button_container.destroy()
        tk.Button(text="Rematch?", command=place_bets).grid(row=2, columnspan=3, sticky=tk.S)

    card_label.config(text=new_text)
    dealer_display.config(text=dealer_score)

    if dealer_score < 17:
        return True
    elif dealer_score >= 21:
        return False
    elif player_score == dealer_score and player_score >= 17:
        return False
    else:
        return True

def draw_card():
    global deck
    card = deck.pop(r.randint(0, len(deck) - 1))
    return card.suit.name, card.type.name, card.value

main()