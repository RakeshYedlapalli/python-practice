class Computer:

    def __init__(self , ram , rom) -> None:
        self.ram = ram
        self.rom = rom


    def config(self):
        print("Ram is ->", self.ram +" and ROM is ->", self.rom)


computer = Computer("16GB","1TB")
computer = Computer("24GB","2TB")

computer.config()
computer.config()


