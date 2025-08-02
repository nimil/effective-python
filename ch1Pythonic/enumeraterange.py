from random import randint

random_bit = 0

for i in range(32):
    if  randint(0,1):
        random_bit |= 1 << i

print(bin(random_bit))



sum = 0

for i in range(101):
    sum += i

print(sum)



flavor_list = ['apple', 'banana', 'cherry', 'chocolate']

for flavor in flavor_list:
    print(flavor,'is flavor')


for i in range(len(flavor_list)):
 print(i+1,':',flavor_list[i])


for i,flavor in enumerate(flavor_list):
    print(i+1,':',flavor)


