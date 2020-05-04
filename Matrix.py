#!/usr/bin/python3

import random
import time
import os

print("\u000c")
snake = ('0','232','233','233','233','233','234','22','22','22','28','34','34','34','34','34','34','34','34','34','34','231')
matrix = []
wide = os.get_terminal_size().columns//2
high = os.get_terminal_size().lines
headpoints = []
prn=''

for i in range(high):
    matrix.append([])
    for j in range(wide):
        matrix[i].append(["\u001b[38;5;0m", chr(random.randint(12448,12543))])


def change_chr(matrix):
    '''
    :param matrix:
    :return: Возвращает новую матрицу с измененными символами
    '''
    for _ in range(random.randint(0,500)):
        newi=random.randint(0,high-1)
        newj=random.randint(0,wide-1)
        newchr=chr(random.randint(12448, 12543))
        matrix[newi][newj][1] = newchr
    return matrix


def new_head(headpoints, wide):
    '''
    :param headpoints:
    :param wide:
    :return: Генерирует голову новой струи
    '''
    points = []
    for i in range(len(headpoints)):
        points.append(headpoints[i][1])
    for i in range(random.randint(0,4)):
        new_point = random.randint(0,wide-1)
        if new_point not in points:
            headpoints.append([0,new_point])
    return headpoints




def colorized(matrix, headpoints, wide, high):
    '''
    :param matrix:
    :param headpoints:
    :param wide:
    :param high:
    :return: Возвращает матрицу с подсвечеными струйками
    '''
    for i , j in headpoints:
        counter = 1

        while i >= 0 and counter < len(snake) and i < high:
            matrix[i][j][0] = "\u001b[38;5;"+snake[0-counter]+"m"
            counter += 1
            i -= 1
        counter = i - high+1
        i = i
        while i >= high and counter < len(snake) and i < high+len(snake) :
            matrix[i-counter][j][0] = "\u001b[38;5;"+snake[0-counter-1]+"m"
            counter += 1
    return matrix


while True:
    wide = os.get_terminal_size().columns//2
    high = os.get_terminal_size().lines

    headpoints = new_head(headpoints, wide)
    matrix = colorized(matrix, headpoints, wide, high)
    #print("\u001b[2H")
    #print("\u001b[2J")
    prn=''
    for j in range(high):
        prn=prn+'\n'
        for i in range(wide):
            prn=prn+matrix[j][i][0]+matrix[j][i][1]
    print(prn)
    time.sleep(0.13)
    ii=0
    while ii < (len(headpoints)):
        if headpoints[ii][0] < high+len(snake):
            headpoints[ii][0] += 1
            ii += 1
        else:
            del headpoints[ii]
    matrix = change_chr(matrix)
