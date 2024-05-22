sities=['gkp','mrj','cmp','gzb','mp','cg']
student=['neeraj','kishan','manish','alok','arbaz']
def count(list):
    print(len(list))
count(sities)
count(student)
def print_name(list):
    for item in list:
        print(item,end=" ")
print_name(student)