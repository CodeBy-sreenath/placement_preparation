class Bird:
    def fly(self):
        print("bird can fly")
class Penguine(Bird):
    def fly(self):
        print("penguine cannot fly")
obj=Penguine()
obj.fly()               