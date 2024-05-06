# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
def salom(name):
    print(f'Hi, {name}')
class Talaba:
    def __init__(self):
        self.name = input('What is your name?')
        self.age = input('What is your age?')
        self.degree = input('What is your degree?')

    def get_age(self):
        return f'Age: {self.age}'
    def get_degree(self):
        return f'Degree: {self.degree}'
    def get_name(self):
        return f'Name: {self.name}'
    def get_all(self):
        return f'Name: {self.name}, Age: {self.age}, Degree: {self.degree}'
talaba = Talaba()
kursant = Talaba()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    salom('Firdavs')
    print(f'Bu talaba{talaba.get_all()}')
    print(f'Bu kursant{kursant.get_all()}')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
