from turtle import *

def draw_tree(length):
    if length >= 5:
        forward(length)
        right(20)
        draw_tree(length - 10)
        left(40)
        draw_tree(length-10)
        right(20)
        backward(length)

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
    draw_tree(80)
    exitonclick()

if __name__ == '__main__':
    main()
    