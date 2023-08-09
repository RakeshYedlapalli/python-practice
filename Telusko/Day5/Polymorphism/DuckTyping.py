

class Pycharm:
    def execute(self):
        print("Compiling")
        print("Executing")


class MyEditor:
    def execute(self):
        print("Code convention")
        print("Spell check")
        print("Compiling")
        print("Executing")


class Laptop:

    def code(self,ide):
        ide.execute()



pycharm = Pycharm()
myEditor = MyEditor()

lap = Laptop()

lap.code(pycharm)
lap.code(myEditor)