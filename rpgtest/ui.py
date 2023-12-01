import os

class window:
    
    def __init__(self, id, title, options, connections):
        self.id = id
        self.title = title
        self.options = options
        self.connections = connections

    def display(self):
        from loc import locs

        clear()
        print(self.title + "\n")
        print("What would you like to do?")
        
        i = 1
        input_string = ""
        for entry in self.options:
            input_string += f"[{i}] {entry}"
            i += 1
            if i <= len(self.options):
                input_string += " | "

        res = input(input_string + "\n").strip()

        while not res.isnumeric():
            res = input()

        res = int(res)

        while res < 0 or res > len(self.options) + 1:
            res = input()

        target = self.connections[res - 1]
        print("\n")

        for key in locs:
            value = locs[key]
            if value.id == target:
                value.display()

        raise ValueError("Target location not found")

def clear():
    os.system("cls" if os.name == "nt" else "clear")