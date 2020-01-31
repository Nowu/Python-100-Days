# for more graphy, refer to Lsystem

from turtle import *

length = 10
angle = 90

def split_rule(path):
    lst = []
    i = 0
    while i < len(path):
        if path[i] == 'F':
            lst.append(path[i:i+2])
            i = i+2
        else:
            lst.append(path[i])
            i = i+1
    return lst

def apply_rule(path, rules):
    lst = split_rule(path)

    # 1:
    # path = ''
    # for symbol in lst:
    #     if symbol in rules:
    #         path += rules[symbol]
    #     else:
    #         path += symbol

    # 2:
    for i in range(len(lst)):
        symbol = lst[i]
        if symbol in rules:
            lst[i] = rules[symbol]
    path = ''.join(lst)

    return path

def draw_path(path):
    lst = split_rule(path)
    for symbol in lst:
        if symbol == 'Fl' or symbol == 'Fr':
            forward(length)
        elif symbol == '-':
            right(angle)
        elif symbol == '+':
            left(angle)
        else:
            print('invalid symbol')

rules = {
    'Fl': 'Fl+Fr+',
    'Fr': '-Fl-Fr'
}

path = 'Fl+Fr+'
for i in range(10):
    path = apply_rule(path, rules)

speed(0)
draw_path(path)

exitonclick()
