def main():
    data = input("Data: ")

    output = []

    data = data.split(")")
    print(data)

    i = 0
    for name in data:
        if "(name" in name or "(given name" in name:
            data[i] = name.split(" (")[0]
            output.append(name.split(" (")[0])

    print(output)

main()