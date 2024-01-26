import tkinter as tk
import random as r
import cards

root = tk.Tk()
root.title("Quadratic Casino(TM) Blackjack")

deck = []

def main():
    global deck
    deck = cards.reshuffle()
    begin_game_phase()

    root.mainloop()

def begin_game_phase():
    global card_label
    global player_display
    global dealer_display

    card_label = tk.Label()
    display_container = tk.Frame()
    player_display = tk.Label(display_container, text="NUM")
    dealer_display = tk.Label(display_container, text="NUM")
    button_container = tk.Frame()
    hit_button = tk.Button(button_container, text="Hit", command=lambda: take_turn(True))
    stand_button = tk.Button(button_container, text="Stand", command=lambda: take_turn(False))

    card_label.grid(row=0, columnspan=3, sticky=tk.N)
    display_container.grid(row=1, columnspan=4, sticky=tk.N)
    player_display.grid(row=0, columnspan=2, sticky=tk.W)
    dealer_display.grid(row=0, column=2, columnspan=2, sticky=tk.E)
    button_container.grid(row=2, columnspan=3, sticky=tk.S)
    hit_button.grid(row=0, sticky=tk.W)
    stand_button.grid(row=0, column=1, sticky=tk.E)

def take_turn(hit):
    if hit:
        new_suit, new_type, new_value = draw_card()

        card_label.config(text=f"Player draws {new_type} of {new_suit}")

def draw_card():
    global deck
    card = deck.pop(r.randint(0, len(deck) - 1))
    return card.suit, card.type, card.value

main()