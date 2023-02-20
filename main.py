# # assignment operators = += -= /= *= %= **=

# name = "john doe"

# name +=  'mich' # name = name + "mich"

# num1 = 10

# #num1 -= 7 #num1 = num1 - 7
# #num1 /= 7 #num1 = num1 / 7
# # num1 *= 7 #num1 = num1 * 7
# # num1 %= 7 #num1 = num1 % 7
# num1 **= 7 #num1 = num1 ** 7

# print(num1)

# # conditional operators: > < >= <= == !=

# age = 20

# print(age != 20)

# # logical operators: and, or ,not

# # ans =  age > 20 and age <70 and age > 7
# ans =  age > 20 or age <70 and not(age <7)
# print(ans)

# # membership operators in not in

# text =  'this is late already'
# print('this' not in text)

# # identity operators: is is not

# num = 90

# # print (num != 40)

# # data structures is just a way of storing datas and orgamizing them 

# # list, tuple, set, dictionary
# # list is a data structure that is ordered, indexed, allows duplicates, and it is changeable

# colors = ['orange',       'red', 'green', 'yellow', 'blue', 'cyan', 'white', 'black', 'yellow']
# # print(colors[-4: -1])
# # print(colors[2:])
# colors[-1] = "indigo"
# colors.append('violet')
# colors.extend(['maroon', 'greenyellow'])
# colors.insert(1, 'skyblue')

# colors.pop(1)
# colors.remove('violet')

# del colors[-1]


# print(len(colors))


# tuple:  indexed, allows duplicates, but it is not changeable

# colors = ('orange', 'red', 'green', 'yellow', 'blue', 'cyan', 'white', 'black', 'yellow')
# color_list = list(colors)
# color_list[0] = 'bluegreen'
# colors = tuple(color_list)
# print(colors)

# set: not ordered, not indexed and does not allow duplicates

colors = {'orange','red', 'green', 'yellow', 'blue', }
colors2 = {'cyan', 'white', 'black', 'yellow', 'blue'}
sub = {'red', 'green'}
# colors.add('greenblue')
# colors.update(['greenyellow', 'redcyan'])
# colors.remove('blue')
# colors.pop()
# colors.discard('orange')

# x = colors.union(colors2)
# x = colors.intersection(colors2)
# colors.intersection_update(colors2)
# x =colors.difference(colors2)
# x =colors.difference_update(colors2)

# x =colors.symmetric_difference(colors2)
# x =colors.symmetric_difference_update(colors2)

# colors.issubset(sub)

# color_list = list(colors)
# print(colors.issuperset(sub))

# dictionary

person = {"name": "John Doe", "age": 40, "height":"5ft", }
person['age'] =90

person['country'] = "United States"
p = person.copy()
d = person
# del person['country']
# person.pop('ag.e')
person.popitem()

# print(person.setdefault('country', 'United States"))
print(d, p)