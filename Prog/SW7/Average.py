def average(a: float, b: float) -> float:
    return (a + b) / 2

my_list = [1, 2, 4, 8, 16, 32] 

average_list = []
for i in range(len(my_list) - 1):
    average_list.append(average(my_list[i], my_list[i + 1]))

print(average_list)