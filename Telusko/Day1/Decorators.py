#using decorators we can change implementations of methods which is not controlled by us
# we can just overrided the implementation

def division(a,b):
    print(a/b)


#i want to add a logic to swap the value if a < b

def smart_div(fun):

    def inner(a,b):
        if(a<b):
            a,b = b,a

        return fun(a,b)


    return inner    

div = smart_div(division)
div(2,4)
