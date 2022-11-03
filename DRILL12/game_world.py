# game world
# layer 0: Background Objects
# layer 1: Frontground Objects


objects = [[], []]


def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return

def all_objects():
    for layer in objects:
        for o in layer:
            yield o

#yield가 들어있는 함수는 함수가 아닌 generator로 취급

def clear():
    for o in all_objects():
        del o

    for layer in objects:
        layer.clear()

    raise ValueError('Trying destroy non existing object')