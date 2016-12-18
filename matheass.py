#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a very basic math trainer for my son
# It is supposed to present the user with 10
# math tasks - suitable for elementary school
# If there are no error, then a fictional princess
# is saved from a dangerous dragon and an evil
# dungeon.
#
# December 2016
# Robert Hilbrich

from __future__ import print_function
import random
import sys


def calc_add():
    s1 = random.randint(0, 100)
    s2 = random.randint(0, 100)
    return (s1, s2, s1 + s2)


def calc_sub():
    m = random.randint(5, 100)
    s = random.randint(0, m)
    return (m, s, m - s)


def calc_mul():
    f1 = random.randint(0, 10)
    f2 = random.randint(0, 10)
    return (f1, f2, f1 * f2)


def calc_div():
    div_is_correct = False
    while not div_is_correct:
        task = calc_mul()
        if task[0] != 0:
            div_is_correct = True
    return (task[2], task[0], task[1])


def getTask():

    # We need to make sure to have proper multiplication operator
    operators = ('+', '-', '\xc2\xb7'.decode('utf8'), ':')

    # Find out, which operation we are now using
    op_id = random.randint(0, 3)

    # Trigger the appropriate sub-function for each op
    ops = {0: calc_add,
           1: calc_sub,
           2: calc_mul,
           3: calc_div}

    # Get the task and its result
    task = ops[op_id]()

    return (task[0], operators[op_id], task[1], task[2])


def main():
    print("Hallo Ritter Niklas!\n")
    print("Du brauchst 100 Punkte, damit die Prinzessin gerettet wird!")
    print("Deine Rüstung hält allerdings nur 5 Fehler aus ...\n")
    print("Bestehst Du diese 10 Prüfungen, dann hast Du es geschafft.\n")

    score = 0
    fails = 0

    for i in range(1, 11):
        print("Prüfung Nummer %2d:" % i)
        task = getTask()

        while True:
            print("%d %c %d = " % (task[0], task[1], task[2]), end="")
            r = sys.stdin.readline()
            try:
                result = int(r)
                break
            except:
                print("Oh - Deine Eingabe war wohl keine Zahl.")

        if (result == task[3]):
            score += 10
            print("Wunderbar - genau richtig! ", end="")
            print("Du bekommst 10 Punkte mehr. ", end="")
            print("Du hast nun %d Punkte!\n" % score)
        else:
            fails += 1
            print("Leider falsch - richtig wäre: %d" % task[3])
            if fails == 5:
                print("Damit hast Du nun 5 Fehler gemacht und der Drache")
                print("knabbert schon an Deinen Haaren ...")
                print("Versuche es doch noch einmal!")
            else:
                print("Du hast nun %d Fehler gemacht - ohje ohje!" % fails)
                print("So langsam kommt der Drache immer näher ... \n")

    print("")

    if score == 100:
        print("Jipiiiieeeehhh!")
        print("Die Prinzessin ist gerettet und Du hast den Drachen erlegt!")
        print("Eine tolle Jagd Herr Ritter Niklas!")
        print("")
        print("Bei so einem tollen Ergebnis freue ich mich schon ", end="")
        print("auf die nächste Jagd mit Dir!")

    else:
        print("Gratulation - Du hast bis hierhin durchgehalten und der Drache")
        print("hat Dich nicht gefressen. Deine >>%d Punkte<< reichen " % score)
        print("aber nicht, um das Tür des Gefängnisses aufzusprengen.\n")
        print("Versuche es doch noch einmal!")

if __name__ == "__main__":
    main()
