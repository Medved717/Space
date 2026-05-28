import random

print(random.random())

print(random.randint(1, 124))

azs = ['Лукойл', 'Роснефть', 'ТАТНЕФТЬ', 'Ирбис', 'Апельсин']
print(random.choice(azs))

azs_1 = ['Лукойл', 'Роснефть', 'ТАТНЕФТЬ', 'Ирбис', 'Апельсин']
random.shuffle(azs_1)
print(azs_1)

