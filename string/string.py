str1="this is first string"
str2= 'neeraj'
str3="""this is string"""
print(str1)
print(str1+" "+str2)
print(len(str1))
print(str1[2])
print(str1[3:8])

#list methods
print(str1.endswith("ing"))#return  true if string endes with substr
print(str1.capitalize())#capitalizes 1st char 
print(str1.replace("ing","om"))#replaces all occurrences of old
print(str1.find("is"))#return  1st index of 1st occurrence 
print(str1.count("i"))#count thr occorrence of substr
