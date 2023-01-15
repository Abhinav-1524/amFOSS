
def collatz(number):
 
        if number%2 == 0:
            x=number//2
            print(x)
            return x
        else:
            x = (3*number) + 1
            print(x)
            return x


n = input("enter a number:")



while True:
    try:
        n=int(n)
        if n!=1:
            n= collatz(n)
        else:
            break
    except ValueError :
        print("please enter an integer.")
        n = input("enter a number:")