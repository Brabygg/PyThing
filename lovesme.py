import time as t
import os

def main():
    while True:
        loves_me = False
        try:
            num_petals = int(input("How many petals are on your flower of choice? ").strip())
        except:
            os.system("cls" if os.name == "nt" else "clear")
            continue

        while num_petals > 1:

            loves_me = not loves_me
            if loves_me:
                print("LOVES ME")
            else:
                print("LOVES ME NOT")
            num_petals -= 1

            t.sleep(1)
        loves_me = not loves_me

        if loves_me:
            input("\nCongratulations, they love you!\n")
        else:
            input("\nThey don't love you. Now go cry yourself to sleep.\n")

        os.system("cls" if os.name == "nt" else "clear")

main()