#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import random


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
    task = getTask()
    print("%d %c %d = %d\n" % task)

if __name__ == "__main__":
    main()
