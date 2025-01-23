#iteratots 
import random
import re
import functools

def lazy_loader(n):
    i = 0 
    while i < n:
        yield i
        i+=1
# yield i creates a iterator object that is used for further processing . 
for number in lazy_loader(10):
    print(number)

# for  the case when comprehension is wrapped in parentheses.

lazy_below30 = (i for i in lazy_loader(30) if i % 2 == 0)

for number in lazy_below30:
    print(number)

five_continuous_random = [ random.random() for _ in range(5)]
print(five_continuous_random)

def random_seed(n):
    i = 0 
    while i < n : 
        print(i)
        i+=1

random_seed(10)
print(random_seed(10))
random_seed(4)
print(random.random())

#random-randrange
print(random.randrange(10))
print(random.randrange(3,9))

#.shuffle method.
lowkey_range = list(range(10))
random.shuffle(lowkey_range)
print(lowkey_range)
#shuffle is an in-iterator method .that modifies the list directly and doesn't create a new list.2
#choice
what_to_study_now = random.choice(['data science textbook' , 'React and tailwind css' , 'ds project' , 'ui projects'])
print(what_to_study_now)

#non repetative random
range_of_ticket_sold = range(100);
winning_num = random.sample(range_of_ticket_sold , 5)
print(winning_num)

#if duplication is needed just call choice fn multiple time.
four_but_different = [random.choice(range(10)) for _ in range(4)]
print(four_but_different)

# some regex
conditions = [
    not re.match("a" , "cat"),
    re.search('a', 'cat'),
    not re.search('c' , 'dog'),
    3 == len(re.split("[ab]" , "carbs")),
    'R_D_' == re.sub("[0,9]" , '_', 'R2D2')
]
all_true = True;
for condition in conditions:
    if not condition:
        all_true = False
        break

print(all_true)

#object oriented python

def exp(base,power):
    return base ** power

def two_to_the_base(power):
    return 2 ** power

from functools import partial
two_to_the = partial(exp,2)
print(two_to_the(3))

#use partial with later argument
square_of = partial(exp, power = 2)
print(square_of(3))

def double(x) :
    return 2*x

xs  = [12,34,22,11]
doubled_0 = [double(x) for x in xs] 
doubled = map(double,xs)
doubled_2 = partial(map,double)
twice_xs = doubled_2(xs)
print(doubled)

def multiply(x,y):
    return x*y

element_w_product = map(multiply , [1,2] , [4,5])
for x in element_w_product:
    print(x)

def is_even(x):
    return x%2 == 0

xs = range(1,8)
x_evens = [x for x in xs if is_even(x)]
print(x_evens)
x_evens_again = filter(is_even , xs)
for x in x_evens_again:
    print(x)
list_evener = partial(filter, is_even)
xs_twice = list_evener(xs)
print(xs_twice)

from functools import reduce
xs_product = reduce(multiply, xs)
pr = partial(reduce, multiply)
xs_pr2 = pr(xs)
print(xs_pr2)

#for in case where both the index and its elmeent will be used the most pythonic way is to use enumerate
# as enumnerate returns tupple of index and element itself. (index, element)


def do_something(i,element):

    print(f'element is present at index {i} and is named {element}')

zanpakuto = ['Zangetsu' , 'Senbonzakura' , 'Kyokasuigetsu' , 'katen kyotsu' , 'Benihime' , 'suzimushi' ]

for i,element in enumerate(zanpakuto):
    do_something(i,element) 
# for just index
# for i, _ in enumerate(zanpakuto):
#     do_something(i)

#zip and unzip
list1 = ['apple' , 'mango' , 'kiwi']
list2 = ['green gram' , 'chickpea' , 'peanut']
list3 = zip(list1,list2);
pair = []
for x in list3:
    print(x)
    pair.append(x)

print(pair)
fruit,sprouts = zip(* pair)
print(f'{fruit} {sprouts}')