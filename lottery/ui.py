import lottery
import tkinter as tk

def return_prize():
    prizes = []
    listbox_prizes.delete(0, tk.END)
    try:
        prizes = lottery.get_prize(int(textbox_count.get()))
    except Exception as e:
        listbox_prizes.insert(0, f"Error: {str(e)}")
        return
    if len(prizes) > 0:
        listbox_prizes.insert(0, "Congratulations, you have won:")
        for i in range(len(prizes)):
            listbox_prizes.insert(i + 2, prizes[i - 1])
    else:
        listbox_prizes.insert(0, "You didn't win anything. Loser.")

root = tk.Tk()
root.title("Lottery Thing")
root.geometry("350x150")

label_count = tk.Label(root, text="Number of draws:")
label_count.grid(row=0, column=0, sticky=tk.E, padx=5, pady=10)

textbox_count = tk.Entry(root, width=2)
textbox_count.grid(row=0, column=1, sticky=tk.W, padx=5, pady=10)
textbox_count.focus_set()

button_submit = tk.Button(root, width=10, height=1, text="Win(?)", command=return_prize)
button_submit.grid(row=1, column=0, sticky=tk.E, padx=1, pady=2)

listbox_prizes = tk.Listbox(root, height=3, width=50)
listbox_prizes.grid(row=2, column=0, sticky=tk.E, padx=14, pady=15, columnspan=2)

root.mainloop()