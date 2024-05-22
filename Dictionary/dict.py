#mutable
#no oredrd of dict
#we can not creat a duplicate key
info={
    'key': 'value',
    'name':'neeraj',
    'subject':['c','c++','java','python'],#set is used in dect
    'topic':('set','dictionry','tupl'),#tupl is used in dict
    'learning':'coding',
    'age':18,
    'marks':87
}
print(info)
print(type(info))
print(info["key"])
print(info["name"])
print(info["subject"])
print(info["topic"])
print(info["age"])
info["key"]='lucky'#replec the value with lucky
info['surname']='maurya'#add a new aliment in dict
print(info)
