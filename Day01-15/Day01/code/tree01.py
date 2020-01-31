from turtle import *
from random import randint

def random_delta_branch(start=6, end=15):
    return randint(start, end)

def draw_tree(trunk_length, smallest_branch):
    delta_branch = random_delta_branch()
    if trunk_length >= smallest_branch:
        forward(trunk_length)
        right(20)
        draw_tree(trunk_length - delta_branch, smallest_branch)
        left(40)
        draw_tree(trunk_length - delta_branch, smallest_branch)
        right(20)
        backward(trunk_length)


def main():
    # set color
    color('green')
    # set turtle speed, 0 is the fastest 1->10 from slow to fast
    speed(0)

    # adjust initial position of the tree
    left(90)
    penup()
    backward(150)
    pendown()

    # draw tree
    draw_tree(80, 5)
    exitonclick()

if __name__ == '__main__':
    main()
    