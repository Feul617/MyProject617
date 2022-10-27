class Star:
    type = 'star'
    x = 100

    def change():
        x = 200
        print('x is', x)


print("x is", Star.x)
Star.change()
print("x is", Star.x)

star = Star() # 굳이 객체를 생성하는 것도 가능
print('x is', star.x) # 객체 변수로 액세스하지만, 결국 클래스 변수 x를 가르킨다


class Player:
    name = 'Player' # 클래스 변수

    def __init__(self):
        self.x = 100

    def where(self):
        print(self.x)

player = Player()

print(Player.name) # 클래스 변수 출력
print(player.name) # name이라는 객체 변수가 없으면 같은 이름의 클래스 변수가 선택된다.

Player.where(player) # 이게 원칙적인 파이썬에서의 멤버함수 호출
player.where() # => Player.whele(player)과 동일

table = {
    "SLEEP" : {"HIT" : "WAKE"},
    "WAKE" : {"TIMER10" : "SLEEP"}
}

cur_state = "WAKE"
next_state = table[cur_state]["TIMER10"]

print(next_state)
