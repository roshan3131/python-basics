

#LIST
#append()method
l=["abc",1,2,7,True,2.5]
l.append("bike")
print(l)

#insert()method
l[-1]="car"
l.insert(-2,"pens")
print(l)

#remove()method
l.remove(True)
print(l)

l.remove(2.5)
print(l)

#del()method
del l[-1]
print(l)


#DICTIONARY
this_dict={"books":"10","notes":"5","pencils":"3","pens":"8","eraser":"6","files":2}
print(this_dict)

#Extract keys and values from list
this_dict={"books":"10","notes":"5","pencils":"3","pens":"8","eraser":"6","files":2}
this_dict.values()
print(this_dict.values())
this_dict.keys()
print(this_dict.keys())