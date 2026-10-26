class Student:
    def __init__(self, name, age, gender, address, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = phone
    def eat(self):
        print(f"{self.name} 正在吃饭。")
    def study(self):
        print(f"{self.name} 正在学习。")
    def play(self):
        print(f"{self.name} 正在玩耍。")
s = Student("张三", 20, "男", "Tsinghua", "13800000001")
print(s.name, s.age, s.gender, s.address, s.phone)
s.eat()
s.study()
s.play()
