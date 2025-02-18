import math

trail = [(142.492, 208.536),
    (142.658, 207.060),
    (143.522, 205.978),
    (145.009, 205.546)]

def path_length(trail):
    length = 0
    for i in range(len(trail)-1):
        length += math.sqrt((trail[i+1][0] - trail[i][0])**2 + (trail[i+1][1] - trail[i][1])**2)
    return length

print(path_length(trail))