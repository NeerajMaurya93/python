with open("file  input output/demo.txt","r")as f:
   data= f.read
   print(data)
with open("file  input output/demo.txt","w")as f:
    f.write("new data")