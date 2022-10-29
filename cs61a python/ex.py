def identity(n):
    return n
def cube(n):
    return pow(n,3)
def summation(n,term):
    total=0
    k=1
    while(k<=n):        
        total+=term(k)
        k+=1
    return total
def make_adder(n):
    def adder(k):
        return n+k
    return adder
def apply_twice(f,x):
    return f(f(x))

def square(x):
    return x*x

def sum_all(x):
    print(x)
    def next_all(y):
        return sum_all(x+y)
    return next_all

def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    k=n
    if(k==0):
        return identity
    elif(k==1):
        return func
    else:
        return make_repeater(func,k-1)