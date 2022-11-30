# f = open('data.txt', 'r')
# data = f.read()
# f.close()
# print(data) # parsing을 하지 않아서 출력이 문자열
# #역 직렬화를 하려면 data가 다시 dict타입으로 바뀌어야 함
import json
with open('data.json', 'r') as f:
    data = json.load(f)
#json은 int, float, str, bool 4가지와 이것으로 만드는 list, dict만 지원함

print(type(data))
print(data)