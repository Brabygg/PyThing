import os

def main():
    clear()
    choice = input("Select program configuration:\n[1] RGB -> HEX\n[2] HEX -> RGB\n").strip()

    if choice == "1":
        rgb_to_hex()
    elif choice == "2":
        hex_to_rgb()

    main()

def rgb_to_hex():
    rgb = input("\nEnter an RGB value (RRR GGG BBB): ").strip().split(" ")
    
    hexes = []
    try:
        for color in rgb:
            if len(color) > 3:
                raise Exception
            
            color = int(color)
            if color > 255 or color < 0:
                raise Exception
            
            color = hex(color)
            color = color[2:len(color)]
            if len(color) == 1:
                color = "0" + color
            hexes.append(color)

        hexes = "".join(hexes)
    
    except:
        input("The entered format was incorrect.\n")
        return
    
    input(f"Conversion successful. Output: #{hexes}")

def hex_to_rgb():
    code = input("\nEnter a hex value (RRGGBB): ").strip()
    if len(code) != 6:
        input("The entered format was incorrect.\n")
        return
    s_code = [code[0:2], code[2:4], code[4:6]]
    
    rgb = []
    try:
        for color in s_code:
            color = int(color, 16)

            if color > 255 or color < 0:
                raise Exception
            
            rgb.append(color)
    except:
        input("The entered format was incorrect.\n")
        return
    
    input(f"Conversion successful. Output: R {rgb[0]}, G {rgb[1]}, B {rgb[2]}")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

main()