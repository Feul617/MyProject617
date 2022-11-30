import pickle

class NPC:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

    def show(self):
        print(f'Name:{self.name} Pos:({self.x}, {self.y})')

with open('npcs.pickle', 'rb') as f: #바이너리를 사용해서 암호화에 유리
    npcs = pickle.load(f)
for npc in npcs:
    npc.show()