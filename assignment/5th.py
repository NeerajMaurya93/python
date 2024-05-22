#first
dict={
    'cat ' : 'a small animal',
    'table' : ['a pice of furniture','list of facts & figures']
}
print(dict)

#second
subject ={
    'python','java','c++','python','javascript','java','python','java','c++','c'
}
print(subject)
print(len(subject))
 #3rd
mark={}
x=int(input('enter the number :'))
mark.update({'phy' : x})
x=int(input('enter the number :'))
mark.update({'math' : x})
x=int(input('enter the number :'))
mark.update({'eng' : x})
print(mark)