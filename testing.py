import inspect

def f1(x,y):
    print(x+y)
def f2(x,y):
    print(x,y)
def f3(x):
    print(x)
def f4():
    print("Hi there")
    
FUNCTIONS = [f1, f2, f3, f4]
ARGUMENTS = [[3,3],[1,2],[1],[]]

def route_one():
    index = 0
    for index,fun in enumerate(FUNCTIONS):
        fun(*ARGUMENTS[index])
        print("total args needed",len(inspect.getargspec(fun).args))
        #should print total numbers needed
        #this way we can just have all our items in a list and keep track
        #wihout a list of list

def test(a,b,c):
	print(a,b,c)

if __name__ == '__main__':
        route_one()
        test(2, 3, 4)
        print(len(inspect.getargspec(test).args)) #prints 3