n=int(input("enterthe number"))
def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n
calc_sum(n)
sum=calc_sum(n)
print(sum)