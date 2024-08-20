
class Test:
    def __init__(self, id):
        self.id = id
        id = 100
 
 
x = Test(23)
 
print(x.id)


def func(num):
    res = '*'
    for _ in range(num):
        res += res
    return res
 
 
for x in func(2):
    print(x, end='')

data = [261, 321]
try:
    print(data[-3])
except Exception as exception:
    print(exception.args)
else:
    print("('success',)")
print(list('Hello'))

w = bool(23)
x = bool('')
y = bool(' ')
z = bool([False])
print(f'w{w}x{x}y{y}z{z}')

class Economy:
    def __init__(self):
        self.econ_attr = True
 
 
class Business(Economy):
    def __init__(self):
        super().__init__()
        self.busn_attr = False


x = 1 // 5 + 1 / 5

print(x)

class Team:
    def show_ID(self):
        print(self.get_ID())
 
    def get_ID(self):
        return "anonymous"
 
 
class A(Team):
    def get_ID(self):
        return "Alpha"
 
 
a = A()
a.show_ID()

 
econ_a = Economy()
econ_b = Economy()
busn_a = Business()
busn_b = busn_a
print(isinstance(busn_a, Economy)
      and isinstance(econ_a, Business), end=" ")
print(busn_b is busn_a or econ_a is econ_b)


x=1

def a(x):
    return 2 * x
 
 
x = 2 + a(x)      # Line 8
print(a(x))       # Line 9

print(__name__)

class Cat:
    Species = 1
 
    def get_species(self):
        return 'kitty'
 
 
class Tiger(Cat):
    def get_species(self):
        return 'tiggy'
 
    def set_species(self):
        pass
 
 
creature = Tiger()
print(hasattr(creature, "Species"),
      hasattr(Cat, "set_species"))


list1 = [1, 3]
list2 = list1
list1[0] = 4
print(list2)
print(sorted("213"))

print([i for i in range(-1, -2)])

def func(p1, p2):
    p1 = 1
    p2[0] = 42
 
 
x = 3
y = [1, 2, 3]
 
func(x, y)
 
print(x, y[0])

def func(x):
    return 1 if x % 2 != 0 else 2
 
 
print(func(func(1)))
i=4
while i > 0:
    i -= 2
    print('*')
    if i == 2:
        break
else:
 
    print('*')


x = 1 / 2 + 3 // 3 + 4 ** 2

print(x)
 





