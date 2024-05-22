f=open("file  input output/demo.txt","r")
data=f.read()#if we want toread one liune then we use f.readline
print(data)
print(type(data))
f.close()