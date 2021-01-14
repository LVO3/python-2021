class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4,2)

print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print(id(a.first))

b = FourCal(1,3)

print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
print(id(b.first))

class MoreFourCal(FourCal):
    pass

c = MoreFourCal(6, 2)
print(c.mul())
