class Circle:
    def getcircum(self):
        circum=self.radius*2*3
        return circum
    def getarea(self):
        area=self.radius**2*3
        return area
small=Circle()
big=Circle()

small.radius=1
big.radius=10
print(f'반지름 {small.radius}인 원의 넓이는 {small.getarea()},둘레는 {small.getcircum()}')
print(f'반지름 {big.radius}인 원의 넓이는 {big.getarea()},둘레는 {big.getcircum()}')

