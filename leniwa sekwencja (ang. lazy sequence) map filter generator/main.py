####leniwa sekwencja (ang. lazy sequence)

###map
m = map(lambda x: x**3, range(5))
print(list(m))

m = map(lambda x: x**3 if x % 2 == 0 else x, range(5))
print(list(m))

###filter

# def jest_parzysta(x):
#     return x % 2 == 0

# f = filter(jest_parzysta, range(10))

f = filter(lambda x: x % 2 == 0, range(10))
#print(list(f))
print(next(f))
print(next(f))
print(next(f))

f = filter(lambda x: x**3, range(5))  # ❌ to nie podnosi do sześcianu!
print(list(f))



###wyrażenie generatorowe (generator expression)

wg = (x*2 for x in range(10))
#print(list(wg))
print(next(wg))
print(next(wg))
print(next(wg))
print(next(wg))



###Generator (yield)

# przykład yeild
def licz_do_trzech():
    print("Start")
    yield 1
    print("Po pierwszym yield")
    yield 2
    print("Po drugim yield")
    yield 3
    print("Koniec")


gen = licz_do_trzech()
next(gen)  # Start → zwraca 1
next(gen)  # Po pierwszym yield → zwraca 2
next(gen)  # Po drugim yield → zwraca 3

#2 przykład Funkcja-generator

def kwadraty(n):
    for i in range(n):
        yield i * i

for x in kwadraty(5):
    print(x)



