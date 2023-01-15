
def function(a):
    if (len(a) == 0):
        print("given list has no values.")

    for i in range (len(a)):

        if (a[i]!=a[len(a)-2] and (a[i]!=a[len(a)-1])):
            print(str(a[i]),end=", ")

        if (a[i]==a[len(a)-2]):
            print(str(a[-2]),end=" and ")
            
        if(a[i]==a[len(a)-1]):
            print(str(a[-1]))


a = list(input("enter: ").split())
function(a)
 