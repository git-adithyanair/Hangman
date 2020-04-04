import turtle
import random
import sys
import time

words_list = []

draw = turtle.Turtle()
draw.hideturtle()
draw.width(5)
draw.speed(0)
draw.pencolor("brown")

screen = turtle.Screen()
screen.bgcolor("yellow")

with open(sys.argv[1], "r") as words:
    for word in words:
        word = word.strip()
        words_list.append(word)

def draw_line(x,y,h,d):
    draw.up()
    draw.setpos(x,y)
    draw.down()
    draw.seth(h)
    draw.fd(d)

def draw_circle(x,y,r):
    draw.up()
    draw.setpos(x,y)
    draw.down()
    draw.circle(r)

def part1():
    draw_line(-50,-100,0,100)

def part2():
    draw_line(0,-100,90,200)

def part3():
    draw_line(0,100,0,100)

def part4():
    draw_line(100,100,270,25)

def part5():
    draw_circle(75,50,25)

def part6():
    draw_line(100,25,270,60)

def part7():
    draw_line(100,-5,135,30)

def part8():
    draw_line(100,-5,45,30)

def part9():
    draw_line(100,-35,240,40)

def part10():
    draw_line(100,-35,300,40)


game_word = words_list[random.randint(0,len(words_list) - 1)]
word_list = list(game_word)
parts = [part1, part2, part3, part4, part5, part6, part7, part8, part9, part10]
display = ["_" for i in range(len(word_list))]
count = -1
win = False

while win is False:

    print(" ".join(display))
    ch = input("Input letter: ")

    if ch == "end":
        exit()

    for j in range(len(game_word)):
        if ch == game_word[j]:
            if ch in word_list:
                word_list.remove(ch)
            display[j] = ch

    if ch not in game_word:
        count = count + 1
        parts[count]()

    if len(word_list) == 0:
        print(" ".join(list(game_word)))
        print("Congratulations! You've won!")
        win = True
        time.sleep(2)
        exit()

    if count == 9:
        print("You lost! The word was %s!" % game_word)
        time.sleep(2)
        exit()

turtle.mainloop()
