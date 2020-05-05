#!/usr/bin/python3

import random
import time
import os
import sys

sys.stdout.write(u"\u001b[2J")
snake = ('231', '34', '34', '34', '34', '34', '34', '34', '34', '34', '34', '28', '22', '22', '22', '234', '233', '233',
         '232', '0')
width = os.get_terminal_size().columns-1
height = os.get_terminal_size().lines
matrix = []
headpoints = []


def create_snake(snake):
    full_snake = []
    for i in range(len(snake) - 1):
        full_snake.append(["\u001b[38;5;" + snake[i] + "m", chr(random.randint(12448, 12543))])
    full_snake.append(["\u001b[38;5;34m", "  "])
    return full_snake


def issue_snakes(headpoints, snake, width):
    points = []
    for i in range(len(headpoints)):
        if headpoints[i][0] - len(snake) < 5:
            points.append(headpoints[i][1])
    for i in range(random.randint(0, 4)):
        new_point = 2*random.randint(1, width//2)
        if new_point not in points:
            headpoints.append([0, new_point, create_snake(snake)])
    return headpoints


def move_snakes(headpoints, snake):
    ii=0
    while ii < (len(headpoints)):
        if headpoints[ii][0] >= height + len(snake):
            del headpoints[ii]
        headpoints[ii] = [headpoints[ii][0] + 1, headpoints[ii][1], headpoints[ii][2]]
        ii+=1
    return headpoints


def change_snake(headpoints, snake):
    for x in range(len(headpoints)):
        for _ in range(random.randint(0, 2)):
            newchr = chr(random.randint(12448, 12543))
            newpos = random.randint(0, len(snake)-2)
            headpoints[x][2][newpos][1] = newchr
    return headpoints


def current_matrix(headpoints, height, snake):
    for i, j, k in headpoints:
        counter = 0
        while i-counter >= 0 and counter < len(snake) and i < height:
            matrix.append([i - counter, j, k[counter]])
            counter += 1
        counter = i - height
        while i >= height and counter < len(snake) and i < height + len(snake):
            matrix.append([i - counter, j, k[counter]])
            counter += 1
    return matrix


while True:
    width = os.get_terminal_size().columns-1
    height = os.get_terminal_size().lines
    headpoints = issue_snakes(headpoints, snake, width)
    matrix=[]
    matrix = current_matrix(headpoints, height, snake)
    headpoints = move_snakes(headpoints, snake)
    headpoints = change_snake(headpoints, snake)
    time.sleep(0.05)
    for i in matrix:
        sys.stdout.write(u"\u001b["+str(i[0])+";"+str(i[1])+"H")
        sys.stdout.write(i[2][0]+i[2][1])
