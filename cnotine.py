def cnotine(prompt):
    while True:
        cont = input(prompt + "\n[1 - Continue; 2 - Cancel]\n").strip()
        if (cont == "1"):
            return True
        elif (cont == "2"):
            return False

def multi_cnotine(prompt):
        return input(prompt + "\n[1 - Continue; 2 - Cancel]\n").strip()