import pyinputplus as pyip
items=[]
total=0
bread=pyip.inputMenu(['wheat','white','sourdough'],prompt='select the bread type: \n')
items.append(bread)

protein=pyip.inputMenu(['chicken','turkey','ham','tofu'],prompt='select a protein type: \n')
items.append(protein)

cheese=pyip.inputYesNo(prompt='do you want cheese: \n')


if cheese == 'yes':
    cheesetype = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'],prompt='what type of cheese do you want?: \n')
    items.append(cheesetype)

extras = pyip.inputYesNo('do you want mayo, mustard, lettuce, or tomato? \n')

if extras == 'yes':
    extratype= pyip.inputMenu(['tomato', 'mayo', 'mustard', 'lettuce'],prompt='select extratype \n')
    items.append(extratype)

num=pyip.inputInt(prompt='how many sandwich do you need?',min=1)
items.append(num)

prices ={'wheat' : 5 , 'white' : 4 ,'sourdough':3,'chicken':10,'turkey':8,'ham':9,'tofu':5,'cheddar':3,'swiss':4,'mozzarella':5,'tomato':1 ,'mayo':2,'mustard':1,'lettuce':2}
print(items)

for i in items:
    if i in prices.keys():
        total=total+prices.get(i)
total=(total) * num
print('the total price for the sandwich is ', total)
