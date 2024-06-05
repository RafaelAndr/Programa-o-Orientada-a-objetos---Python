import random

print(random.random())
print(random.uniform(4,10))
print(random.randint(4,10))

cores = ["Verde", "Vermelho", "Azul"]
print(random.choice(cores))
print(random.choices(cores, k=2))
print(random.shuffle(cores))
print(cores)

