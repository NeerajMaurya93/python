info={
    'key': 'value',
    'name':'neeraj',
    'subject':{
            'physics':67,
            'maths':65,
            'english':78,
            'hindi':56
        },
    'topic':('set','dictionry','tupl'),
    'learning':'coding',
    'age':18,
    'marks':87
}
print(info )
print(info['subject'])#if value is not present in dict the it is creat error
#print(info.get['subject'])#if value is not present in dect thent it is not creat error it is return none valu
print(info['subject']['maths'])
print(info.keys())
print(len(info.keys()))
print(info.values())
print(list(info.values()))
#print(info.update["city":"delhi"])
print(info.items())
