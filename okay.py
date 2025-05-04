x = [4,1,2,3]
y = sorted(x)
x.sort()
print(x)
x = sorted([-4 , 1 , -2 , 3] , key = abs , reverse = True)
# this is what reverse = true does with key = abs it takes only mod value does the job.
print(x)

# # wc = sorted(word_count.items() , key = lambda item: item[1], reverse = True)
# print(wc)
even_numbers = [s for s in range(10) if s % 2 == 0]
print(even_numbers)
sq_even = [p * p for p in even_numbers]
print(sq_even)

# turning a list into dictionary
sq_dic = { a : a*a for a in range(13) if a % 2  != 0}
print(sq_dic)
sq_set = {b * b for b in [2,-9]}
# yeah no doubt thats a set .
print(sq_set)
pairs = [
    (x,y)
    for x in range(10)
    for y in range(x + 1 , 10)
]
print(pairs)
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
my_list = [1,2,3,4,5]
my_iterator = MyIterator(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

try:
    print(next(my_iterator))
except StopIteration:
    print("End of iteration reached.")

list1 = [10*x for x in range(10)]
iterator = iter(list1)

print(next(iterator))
print(next(iterator))

def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
try:
    print(next(gen))
except StopIteration:
    print("End of Generation")

# Randomness
import random
four_un_random = [random.random() for _ in range(4)]
print(four_un_random)

# random.seed(10)
print(random.random())
print('all good? ')
# random.seed(10)
print(random.random())

rando = random.randrange(10)
print(rando)
an_random = random.randrange(3,6)
print(an_random)
# let's sort the list and then make it random again..
x = [a for a in range(10)]
print(x)
x.sort(reverse = True)
print(x)
shuf= random.shuffle(x)
print(x)

class Set:
    def __init__(self , values = None):
        """ This is the constructor 
        it gets called when you create a new Set. You would use it like  
        s = Set()
        s2 = Set([1,2,3])
        """
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)
        def __repr__(self):
            """" this is the string representation of a Set object
            if you type it at the Python prompt , or pass it to str()"""
            return "Set: " + str(self.dict.keys())
        
        def add(self , value):
            self.dict[value] = True
        
        def contains(self, value):
            return value in self.dict

        def remove(self , value):
            del self.dict[value]

# Enumerate huh..
# case when you want to iterate over a list by both its 
# elements and their indexes.
# not pythonic

# zip
list1 = [1,2,3]
list2 = ['a','b','c']
print(zip(list1, list2))

pairs = [('a' , 1) , ('b', 2) , ('c', 3)]
letter , nums = zip(*pairs)
print(f'{letter} , {nums}')

def add(a,b):
    return a + b

print(add(1,2))
try:
    print(add([1,2]))
except TypeError:
    print("TypeError: add() missing 1 required positional argument: 'b'")
print(add(*[1,2]))

def other_way_magic(x,y,a,z):
    return x+y+z+a

x_y_list = [1,2,3]
z_dict = {"z": 3}

print(other_way_magic(*x_y_list, **z_dict))
