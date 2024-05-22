#it is the collection of the unorderd items
#each element in the set must be unique & immutable
#in which not store list and dectionory value but tupl is stored
#removed duplicate value
collection={2,4,3,1,3 ,3 ,"hello","world","world","maurya"}
collection1={1,2,3,4,"hello","neeraj","world"}
#print(collection)
# print(type(collection))
# print(len(collection))
#collection={}#denoted the empty dict
#collection=set()#denoted the  empty set


# #methods of sets
#collection.add(5) 
# print(collection)# adds an element
# collection.remove(4)
# print(collection)#removed  the element
# collection.clear(1)
# print(collection)#empties the set
# collection.pop(2)
# print(collection)#removes a random value
print("union",collection.union(collection1))
print("intersection ",collection.intersection(collection1))