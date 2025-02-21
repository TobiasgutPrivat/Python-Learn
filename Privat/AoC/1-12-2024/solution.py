with open("data.txt", "r") as f:
    data = f.read().splitlines()
    first: list = [int(line.split()[0]) for line in data]
    second: list = [int(line.split()[1]) for line in data]
    for line in data:
        first.append(int(line.split()[0]))
        second.append(int(line.split()[1]))

    first.sort()
    second.sort()

    totalDiv = 0
    for i in range(len(first)):
        div = abs(first[i] - second[i])
        totalDiv += div

    print(totalDiv)
        