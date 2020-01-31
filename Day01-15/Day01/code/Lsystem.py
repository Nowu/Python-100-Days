from turtle import *

length = 10
angle = 90


def draw_path(path):
    for symbol in path:
        if symbol == 'F':
            forward(length)
        elif symbol == '-':
            left(angle)
        elif symbol == '+':
            right(angle)
        else:
            print('invalid symbol')

def apply_rule(path):
    rule = 'F-F+F+FF-F-F+F'
    return path.replace('F', rule)


path = 'F-F-F-F'
path = apply_rule(path)
path = apply_rule(path)
# path = apply_rule(path)

speed(100)
draw_path(path)

exitonclick()
