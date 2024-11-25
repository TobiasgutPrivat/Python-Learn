import math
def optimaler_badetag(temparaturen):
    max_temparatur = 0
    max_temparatur_index = 0
    for i in range(len(temparaturen)):
        if temparaturen[i] > max_temparatur:
            max_temparatur_index = i
            max_temparatur = temparaturen[i]

    Wochentage = ["Mo.","Di.","Mi.","Do.","Fr.","Sa.","So."]

    return Wochentage[max_temparatur_index]


temparaturen = [1,2,8,4,8,8,7]
print(optimaler_badetag(temparaturen))


def get_durchschnitt(liste):
    summe = 0
    for i in liste:
        summe += i
    return summe/len(liste)

temparaturen = [1,2,8,4,8,8,7]
print(get_durchschnitt(temparaturen))

def get_nearest_index(liste):
    durchschnitt = get_durchschnitt(liste)
    nächstes = 0
    for i in range(len(liste)):
        if abs(durchschnitt - liste[nächstes]) > abs(durchschnitt - liste[i]):
            nächstes = i
    return liste[nächstes]
    

temparaturen = [1,2,8,4,8,8,7]
print(get_nearest_index(temparaturen))


kette = "1"
for i in range(2,100):
    kette += "," + str(i)

print(kette)

def ist_primzahl(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def naechst_groessere_primzahl(m):
    i = 0
    while True:
        i += 1
        if  ist_primzahl(m+i):
            return m+i
        if  ist_primzahl(m-i):
            return m-i
        

print(naechst_groessere_primzahl(21))