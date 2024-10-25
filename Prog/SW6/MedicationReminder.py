for day in range(3):
    print(f"Day: {day}")
    for hour in range(24):
        if hour % 4 == 0 and hour != 4:
            print(f"Hour {hour}: Take your medication.")
        else:
            print(f"Hour {hour}:")