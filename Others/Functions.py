def my_function():
    print("Hello From My Function!")

    data = {"rakesh":"MBA","rajesh":"Btech","suresh":"MBA"}
    print(data["rajesh"])

    data2 = ["rakesh","rajesh","suresh"]
    print(data2)

    data4 = ('rakesh','2',3,3,5,5,6)
    print(data4[0])
    rakes = 'rakesh'
    print(id(rakes))
    integers = False
    print(type(integers))

def my_function2(inputValue):
    print("This is my my value =>" + inputValue)

my_function2('rakesh')



def call_by_reference(x):
    x = 10
    print(x)

a = 20
call_by_reference(a)

print(a)


#print("Please insert your ATM Card..")
    
#my_function2("rakesh")


