final={}
tmp=[]
inventory = {'gold coin': 42, 'rope': 1}


    


def displayInventory():
    print("Inventory:")
    item_total = 0
    addToInventory()
    for k, v in final.items():
        print(str(v) + ' - ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))





def addToInventory():
    global tmp
    for k,v in inventory.items():
        for a in range (v):
            tmp.append(k)
    global final
    global dragonLoot
    dragonLoot=tmp+dragonLoot
    for i in range(len(dragonLoot)):
        final.setdefault(dragonLoot[i],dragonLoot.count(dragonLoot[i]))
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
displayInventory()     
                                                                                                                                                                                                                                                                                                             
