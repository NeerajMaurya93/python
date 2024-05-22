#when a function call itself repeatedly
def num(n):#recursive function
    if(n==0):#base case
        return
    print(n)
    num(n-1)
num(6)
