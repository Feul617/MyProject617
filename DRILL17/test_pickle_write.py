import pickle

class NPC:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

    def show(self):
        print(f'Name:{self.name} Pos:({self.x}, {self.y})')

yuri = NPC('Yuri', 100, 200)
tom = NPC('Tom', 200, 400)
npcs = [yuri, tom]
with open('npcs.pickle', 'wb') as f: #binary를 사용해서 암호화에 유리
    pickle.dump(npcs, f)