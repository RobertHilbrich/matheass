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
    return ("%d + %d = ?  " % (s1, s2), s1 + s2)


def calc_text_add():
    s1 = random.randint(1, 100)
    s2 = random.randint(1, 100)
    return(u"\
Graf Drakula hat Geburtstag. Er hat %d Brüder und %d Schwestern. \
Alle möchte er gerne zu seiner Geburtstagsfeier einladen. Wieviele Gäste \
kommen dann insgesamt zu seiner Geburtstagsfeier?\
\n\n" % (s1, s2), s1 + s2)


def calc_sub():
    m = random.randint(5, 100)
    s = random.randint(0, m)
    return ("%d - %d = ?  " % (m, s), m - s)


def calc_text_sub():
    m = random.randint(5, 100)
    s = random.randint(1, m)
    return(u"\
Für seine Geburtstagsfeier hat Graf Drakula %d EUR gespart, um \
für seine Freunde eine große Party zu veranstalten. Für die Torte \
musste er %d EUR beim Bäcker bezahlen. Wieviel Geld hat er noch \
für die Getränke übrig?\
    \n\n" % (m, s), m - s)


def calc_mul():
    f1 = random.randint(0, 10)
    f2 = random.randint(0, 10)
    return (str(f1) + ' \xc2\xb7 '.decode('utf8') + str(f2) + " = ?  ",
            f1 * f2)


def calc_text_mul():
    f1 = random.randint(3, 10)
    f2 = random.randint(1, 10)
    return(u"\
Bei der Geburtstagsfeier von Graf Drakula kommen %d Gäste. Jeder Gast und \
auch Drakula wollen das Geburtstagsmahl von %d Tellern essen. \
Wieviele Teller müssen nach dem Essen von den Zwergen abgewaschen werden?\
\n\n" % (f1 - 1, f2), f1 * f2)


def calc_div():
    f1 = random.randint(1, 10)
    f2 = random.randint(0, 10)
    p = f1 * f2
    return("%d : %d = ?  " % (p, f1), f2)


def calc_text_div_1():
    f1 = random.randint(3, 10)
    f2 = random.randint(0, 10)
    p = f1 * f2
    return(u"\
Zur Geburtstagsfeier von Graf Drakula kommen %d Gäste. Die Geburtstagstorte \
besteht aus %d Stücken. Wieviele Tortenstücke kann jeder Partygast - und auch \
Drakula - essen, so dass alle gleich viele Stücken Torte bekommen? \
\n\n" % (f1 - 1, p), f2)


def calc_text_div_2():
    f2 = random.randint(1, 10)
    p = 2 * f2
    return(u"\
Zur Geburtstagsfeier von Graf Drakula kommt 1 Gast. Die Geburtstagstorte \
besteht aus %d Stücken. \
Wieviele Tortenstücke kann jeder Partygast - und auch \
Drakula - essen, so dass alle gleich viele Stücken Torte bekommen?\
\n\n" % p, f2)


def calc_text_complex_1():
    z1 = random.randint(5, 10)
    z2 = random.randint(1, 10)
    z3 = random.randint(5, 25)
    z4 = random.randint(3, 30)

    return(u"\
Die Zwerge wollen Graf Drakula auch ein Geschenk machen. Sie sammeln dafür \
Geld und packen es gemeinsam in einen Beutel. %d Zwerge spenden jeweils \
%d EUR, Zwerg Frederik spendet %d EUR und Zwerg Mika spendet %d EUR. \
Wieviel Geld ist nun insgesamt im Beutel? \
\n\n" % (z1, z2, z3, z4), z1 * z2 + z3 + z4)


def getTask():

    # Find out, which operation we are now using
    op_id = random.randint(0, 11)

    # Trigger the appropriate sub-function for each op
    ops = {0: calc_add,
           1: calc_sub,
           2: calc_mul,
           3: calc_div,
           4: calc_text_add,
           5: calc_text_sub,
           6: calc_text_mul,
           7: calc_text_div_1,
           8: calc_text_div_2,
           9: calc_text_complex_1,
           10: calc_text_complex_1,
           11: calc_text_complex_1
           }

    # Get the task and its result
    return ops[op_id]()


def main():

    random.seed()

    maxTasks = 20
    maxFails = 5

    print("\
Hallo Ritter Niklas!\n\
Du brauchst %d Punkte, damit die Prinzessin gerettet wird!\n\
Deine Rüstung hält allerdings nur %d Fehler aus ...\n\
Bestehst Du diese %d Prüfungen, dann hast Du es geschafft.\n"
          % (maxTasks * 10, maxFails, maxTasks))

    score = 0
    fails = 0

    for i in range(1, maxTasks + 1):
        print("Prüfung Nummer %2d:" % i)
        task = getTask()

        while True:
            print(task[0] + u"Lösung: ", end="")
            r = sys.stdin.readline()
            try:
                result = int(r)
                break
            except:
                print("Oh - Deine Eingabe war wohl keine Zahl.")

        if (result == task[1]):
            score += 10
            print("Wunderbar - genau richtig! ", end="")
            print("Du bekommst 10 Punkte mehr. ", end="")
            print("Du hast nun %d Punkte!\n" % score)
        else:
            fails += 1
            print("Leider falsch - richtig wäre: %d" % task[1])
            if fails == maxFails:
                print("Damit hast Du nun %d Fehler gemacht und der Drache" % maxFails)
                print("knabbert schon an Deinen Haaren ...")
                print("Versuche es doch noch einmal!")
                return
            else:
                print("Du hast nun %d Fehler gemacht - ohje ohje!" % fails)
                print("So langsam kommt der Drache immer näher ... \n")

    print("")

    if score == maxTasks * 10:
        print("Jipiiiieeeehhh!")
        print("Die Prinzessin ist gerettet und Du hast den Drachen erlegt!")
        print("Eine tolle Jagd Ritter Niklas!")
        print("")
        print("Bei so einem tollen Ergebnis freue ich mich schon ", end="")
        print("auf die nächste Jagd mit Dir!")

    else:
        print("Gratulation - Du hast bis hierhin durchgehalten und der Drache")
        print("hat Dich nicht gefressen. Deine >>%d Punkte<< reichen " % score)
        print("aber nicht, um die Tür des Gefängnisses aufzusprengen.\n")
        print("Versuche es doch noch einmal!")

if __name__ == "__main__":
    main()
