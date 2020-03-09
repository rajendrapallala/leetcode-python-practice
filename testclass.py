class Test1:
    def __init__(self):
        self.a = 1
        self.b = 2
    def __str__(self):
        return "The class variables a and b are {0} and {1} ".format(self.a, self.b)

if __name__ == "__main__":
    c1  = Test1()
    c2 = c1
    c2.a = 3
    print(c1)