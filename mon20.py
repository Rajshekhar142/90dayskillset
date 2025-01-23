def whatisThere():
    fruits = ['mango' , 'orange']
    torpedo = {}
    return torpedo

s = whatisThere()
first_char = s and s[0]
print(first_char);
# try replacing torpedo with fruit and notice the working of  and.
# any and all simple . any check for any iterable being true if present returns true else returns false , for non iterables.
# all check wheather all value are true or not a single false would evaluate to false look 
print(f'{any([True , 1 , 0])}' f'{any([False , 0.0 , {}])}' f'{all([True , 1, 3])}' f'{all([0 , 1, 1])}')
# true false true false
# sort
one = [1,4,5,2,3,99 , 1000 , 135];
sorted_one = sorted(one);
print(sorted_one);

two = [1, -3 , -4 , 55, -333 , 451];
sorted_two = sorted(two, key= abs , reverse= True);
print(sorted_two)
# key abs mean that value at the time of sorting were taken as mod value i.e +ve , and reverse = True means that order is
# reverse descending ..

# using lambdas on key 
class Person:
    def __init__(self , name , age):
        
        self.name = name
        self.age = age
    def __repr__(self):
        return f"(Person(name = '{self.name}' , age = {self.age}))";

People = [Person('Rajshekhar' , 20) , Person('Devendra' , 21) , Person("Dev" , 22)]
sorted_des = sorted(People , key = lambda x: x.age , reverse=True)
print(sorted_des);

#using list comprehension 
div_by_2 = [x for x in range(5) if x % 2 ==0]
print(div_by_2)
# get square
square_to_ten = [x*x for x in range(10) ]
print(square_to_ten);
st = [0 for _ in range(5)]
print(st)

gg = [(x,y) 
      for x in range(10)
      for y in range(10)]
print(gg)