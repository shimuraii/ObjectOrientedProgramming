class Math:   
    @staticmethod #stays the same, do not change
    def add5(x):
        return x + 5
    @staticmethod
    def add10(x):
        return x + 10
    @staticmethod
    def pr():
        print("run")
Math.pr()
print(Math.add5(3))