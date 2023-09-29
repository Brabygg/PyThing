def cnotine(prompt):
    while True:
        cont = input(prompt + "\n[1 - Continue; 2 - Cancel]\n").strip()
        if (cont == "1"):
            return True
        elif (cont == "2"):
            return False

def multi_cnotine(prompt, max_value):
    while True:
        cont = input(prompt + "\n").strip()
        try:
            if (int(cont) <= max_value and int(cont) > 0):
                return int(cont)
        except Exception:
            continue