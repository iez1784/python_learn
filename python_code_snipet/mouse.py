class mouse:
    def __init__(self):
        self.age = 0

    def born(self):
        self.age += 1
        if self.age > 2: return mouse()


import sys

if __name__ == '__main__':
    month = 1
    if len(sys.argv) > 1: month = int(sys.argv[1])

    mice = [mouse()]
    for i in range(month):
        for j in range(len(mice)):
            new_mouse = mice[j].born()
            if new_mouse: mice.append(new_mouse)

    print(len(mice))



            
    
