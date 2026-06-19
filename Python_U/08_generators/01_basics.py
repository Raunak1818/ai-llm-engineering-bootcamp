def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

for cup in stall:
    print(cup)




# regular function
def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]





# generator function 

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai = get_chai_gen()
print(next(chai))   # print Cup 1 (it just has execute once first yield value with you & fn is paused)
print(next(chai))   # print Cup 1 & Cup 2 (whenever you call next time it keep track everything in the memory & give the result which you are yielding)
print(next(chai))   # print Cup 1 & Cup 2 & Cup 3 ( it still in the memory, start exactly where you left it)
# print(next(chai))   #give error