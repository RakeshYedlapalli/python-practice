class MethodOverloading:

    def methodOverloading(self, a=None, b=None , c = None):
        result = 0
        if a != None and b != None:
            return a + b
        elif a != None:
            return a
        
        return b



methodOverloading = MethodOverloading()

result = methodOverloading.methodOverloading(3, 4)
print("Result is =>", result)
result = methodOverloading.methodOverloading(3)

# methodOverloading.method(3,4)
