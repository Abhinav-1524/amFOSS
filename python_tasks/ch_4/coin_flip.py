def randit():
    for i in range(100):
        rand = random.randint(0,1)
        list.append(rand)

def streaks():
    for i in range(94):
        if (list[i]==list[i+1]):
            global streak
            streak = streak + 1
        if(streak == 6):
            global numberofstreaks
            numberofstreaks += 1
            streak = 0
        else:
            continue




import random
numberofstreaks = 0
list=[]
rand = 0
streak =0
for experimentnumber in range (10000):
    randit()
    streaks()
print(numberofstreaks)
print("chances of streaks :" ,( numberofstreaks / 1000)) 
    