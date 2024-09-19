#to return the list of 5 random integers using random library
import random
l1=[]
for i in range(5):
    x=random.randint(299,399)
    l1.append(x)
print(l1)