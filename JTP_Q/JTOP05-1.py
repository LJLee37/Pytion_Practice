class FourCal:
    def __init__(self):
        self.n1 = 0
        self.n2 = 0
        self.temp = 0
    def SetData(self, a, b):
        self.n1 = a
        self.n2 = b
    def Add(self):
        self.temp = self.n1 + self.n2
        return self.temp
    def Mul(self):
        self.temp = self.n1 * self.n2
        return self.temp
    def Sub(self):
        self.temp = self.n1 - self.n2
        return self.temp
    def Div(self):
        self.temp = self.n1 / self.n2
        return self.temp

a = FourCal()
a.SetData(4, 2)
print(a.Add())
print(a.Mul())
print(a.Sub())
print(a.Div())
