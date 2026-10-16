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
students = [
    Student("张三", 20, "男", "Tsinghua", "13800000001"),
    Student("李四", 21, "女", "NEU", "13800000002"),
    Student("王五", 19, "男", "MIT", "13800000003")
]
def search_by_name(name):
    result = [s for s in students if name in s.name]
    return result
def search_by_address(address):
    result = [s for s in students if address in s.address]
    return result
def search_by_phone(phone):
    result = [s for s in students if phone in s.phone]
    return result
for s in search_by_name("张三"):
    print(s.name, s.address, s.phone)
for s in search_by_address("NEU"):
    print(s.name, s.address, s.phone)
for s in search_by_phone("13800000003"):
    print(s.name, s.address, s.phone)
