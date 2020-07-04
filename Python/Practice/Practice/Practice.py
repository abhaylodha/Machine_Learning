#Fundamental Data Types
    #int
    #float
    #bool
    #str
    #list
    #tuple
    #set
    #dict
#Classes - Custom Data Types
#Specialized Data Types
#None

print(2+4)
print(2-4)
print(2*4)
print(2/4)
print(2 ** 4)
print(21 // 4)  #Divison ounded down.
print(21 % 4)   #Reminder

#Math functions.
print(round(3.1))  #Rounding to nearest integer. Result type changes from float to integer.
print(abs(-3.1))   #Absolute value

#Binary Number
print(bin(5))           #Returns a binary number. Data Type is str (String).
print(int('0b101',2))   #Converts a binary number to decimal integer

a,b,c = 1,2,'abcd'       # One to one assignment.
print(a)
print(b)
print(c)

PI = 3.14
radius = 5
circle_area = PI * radius ** 2   #expression -> PI * radius ** 2 and statement -> circle_area = PI * radius ** 2

print("Area of circle : ", circle_area)

#Augmented assignment operator
sum = 0
sum += 5  #Augmented assignment operator.
sum -= 1  #Augmented assignment operator.
sum *= 2  #Augmented assignment operator.
sum /= 4  #Augmented assignment operator.
print(sum)

long_string = '''
WOW
0 0
 _
'''

print(long_string)

name = 'Abc'
age = 25

s = f'Hi {name}, your age is {age}'
s1 = 'Hi {}, your age is {}'.format(name,age)
s2 = 'Your age is {1} Mr. {0}'.format(name,age)
s3 = 'Your age is {age_val} Mr. {name_val}'.format(age_val = age, name_val = name)

print (s)
print (s1)
print (s2)
print (s3)

#String are immutable
s1 = 'abcdefgh'
#s1[0]='x'   #Not permitted.

#Lists are mutable
l1 = ['Amit','Nilesh','Sanket','Aniket']
l2 = l1     #Points to same list l1
l3=l1[:]    #Creates a new list.
l1[0] = 'Sachin'
print(l1)
print(l2)
print(l3)

l3.remove

#List unpacking
a,b,c = [1,2,3]
print(a)   #1
print(b)   #2
print(c)   #3

a,b,c,*rest = [1,2,3,4,5,6,7,8,9]
print(a)   #1
print(b)   #2
print(c)   #3
print(rest) #Rest items

a,b,c,*rest,d = [1,2,3,4,5,6,7,8,9]
print(a)   #1
print(b)   #2
print(c)   #3
print(rest) #Rest items except last
print(d)

####################
#Dictionary (Hash Table/ Maps)
####################
dictionary = {
    'one' : 1,
    'two' : 2,
    }
print("two's value : ", dictionary['two'])
print("keys dictionary : ", dictionary.keys())
print("type of dictionary : ", type(dictionary))

#Dictionary keys are immutable. Hence List which are mutable cannot be used as keys.

#dictionary.get will avoid failures if key does nto exist. Ex-
user = {
    'name' : 'User 1',
    'city' : 'Mumbai'
    }
print("User Age : ", user.get('age'))

print("User Age with default : ", user.get('age',55))

print('name in user','name' in user)
print('name in user keys','name' in user.keys())
print('city in user values', 'city' in user.values())

print('items in user', user.items())

user2 = user.copy()
print('pop removes an item ', user.pop('name'))
print('name removed from user dictionary ', user)

#Update adds the key if no exists or updates existing one if it exists.
user2.update({'age' : 55, 'city' : 'Pune'})
print('user2 Dictionary : ', user2)

print('popitem removes an item randomly from user2 : ', user2.popitem())
print('something removed from user2 dictionary ', user2)

#Other way to initialize a dictionary with keys as string types.
user2 = dict(a=1,b=2)
print("User2 b : ", user2.get('b'))


####################
#Tuples. immutable. Cannot Sort/reverse it. etc.
####################
t1 = (1,2,3,4,5,3)
print(t1[0], t1[1])
print(3 in t1)
print('Count of 3 : ', t1.count(3))
print('Index of 4 : ', t1.index(4))

####################
#Set
####################
st = {1,2,3,4,5,5,5,5}
st.add(4)
st.add(100)
print('set : ', st)

lst = [1,2,3,4,5,6,5,4,3,2,1]
set1 = set(lst)
print(set1)

####################
#Truethy and Falsy
####################

#All values are considered "truthy" except for the following, which are "falsy":

#None
#False
#0
#0.0
#0j
#Decimal(0)
#Fraction(0, 1)
#[] - an empty list
#{} - an empty dict
#() - an empty tuple
#'' - an empty str
#b'' - an empty bytes
#set() - an empty set
#an empty range, like range(0)
#objects for which
#obj.__bool__() returns False
#obj.__len__() returns 0

####################
#Ternary Operator
####################
is_old = True

print("You are old enough to drive.") if is_old else print("You are *not* old enough to drive.")

####################
# is vs ==
####################
#is checks if both objects point to same memory location or not ?
l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1
l4 = l1.copy()

print("l1 == l2 returned true") if (l1 == l2) else print("l1 == l2 returned false")
print("l1 is l2 returned true") if (l1 is l2) else print("l1 is l2 returned false")
print("l3 is l1 returned true") if (l3 is l1) else print("l3 is l1 returned false")
print("l4 is l1 returned true") if (l4 is l1) else print("l4 is l1 returned false")

s1 = "abc"
s2 = "abc"
print("s1 == s2", s1==s2)

####################
# enumerate
####################
#Converts an iterables to a tuple of 2. first element is index and second element is value from iterable.
#enumeraqt([1,2,3]) converts it to [(0,1), (1,2), (2,3)]
print(list(enumerate("Hello")))
for i in enumerate("Hello") :
  print("item index = ",i[0],"item value = ",i[1])

#Can also be written as :
for i,char in enumerate("Hello") :
  print("item index = ",i,"item value = ",char)

####################
# While with else
####################

i = 1
while i < 10 :
  print(i)
  i += 1
else :
  print("Done with while loop")

####################
# Break, Continue and Pass
####################
#pass is just a placeholder.
#For Ex -
a = 11
if (a == 10) :
  #Pass does not do anything. It just fills a place for if true case here.
  pass
else :
  print ("a is not 10")

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
    ]

fillchar="*"
emptychar=" "
for row in picture :
  for pixel in row :
      print (fillchar,end = '') if pixel else print (emptychar,end = '')
  print()

#####################
# Finding duplicates in a list
#####################
some_list = ['a','b','c','b','d','m','n','n','n']
duplicates=[]
for item in some_list :
  new_list=some_list[1:]
  if item in new_list :
    duplicates.append(item)
  while (item in new_list):
    new_list.remove(item)
  else :
    some_list = new_list
print (duplicates)

#####################
# DocStrings
#####################
#Used for adding documentation to the function.
def printInput(a):
  '''
  Info: This function prints whetever is passed as arguments.
  '''
  print(a)

print('help - ')
help(printInput)   #Displays docstrings.
print('__doc__')
print(printInput.__doc__)   #Displays docstrings.
print('---------------------')
printInput('fgdfgfd')

#####################
# Clean Code
#####################

def is_odd_or_even (n) :
  if n%2 == 0 :
    return True
  else :
    return False

#Can also be written as :
def is_odd_or_even_v2 (n) :
  return n % 2 == 0

print(is_odd_or_even(50))
print(is_odd_or_even(51))

print(is_odd_or_even_v2(50))
print(is_odd_or_even_v2(51))

#####################
# *args and **kwargs
#####################
#*args - Varying number of arguments
#**kwargs - Keyword arguments

def fun1 (*args, **kwargs) :
  print(args)
  print(kwargs)
  print(kwargs['n1'])

fun1 (1,2,3,4,5,n1=55,n2=50)

