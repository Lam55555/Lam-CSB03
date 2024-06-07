thisdict = {
    "class_name": "CSB06",
    "year": 2024,
    "studen_count": 10
}

#access item
print(thisdict['class_name'])  #dung de hien value cua class_name

#change item
thisdict["studen_count"] = 9
print(thisdict["studen_count"])

#add item
thisdict["new_student"] = "Quynh Anh"
print(thisdict)

# #remove item
# thisdict.pop('new_student')
# print(thisdict)

# #remove phan tu cuoi
# thisdict.popitem()
# print(thisdict)

#vong lap
# for x in thisdict:
#     print(x)  #Lay key

# for x in thisdict:
#     print(thisdict[x])

# for x in thisdict.keys():
#     print(x)

# for x in thisdict.values():
#     print(x)

# for x,y in thisdict.items():
#     print(x,y)  #lay ca key lan value

student = {
    "student1":{
        'name':'Tai',
        'age':18
    },
    'student2':{
        'name':'Lam',
        'age':17,
    },
    'student3':{
        'name':'Huy',
        'age':16
    }
}



# for i in student.values():
#     print(i['name'])

for a,b in student.items():
    print(b['name'])