import random
i=10
k=1
count=0
while(i>=1):
    i=i-1
    print(f'you have {i} chance')
    lst=['g','w','s']
    computer=random.choice(lst)
    pc=print(computer)
    you=input("enter your choice as 's','g','w': ")
    print(you)
    if you==computer:
        print("you loose")



print(f'you won {count} times')
