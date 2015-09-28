#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from progress import ProgressBar
from animation import *
from time import sleep

p = ProgressBar(" Doing the 1st thing:", max_value=20, width=20)
for i in range(21):
    p.update(i)
    sleep(.25)
p.finish("Success")

a = Animation("Waiting for the 2nd thing:")
for i in range(21):
    a.next()
    sleep(.25)
a.finish("Success")

a = Animation("Waiting for the 3rd thing:", animation=ANIMATE_VGROW)
for i in range(21):
    a.next()
    sleep(.25)
a.finish("Success")

a = Animation("Waiting for the 4th thing:", animation=ANIMATE_HGROW)
for i in range(21):
    a.next()
    sleep(.25)
a.finish("Success")

a = Animation("Waiting for the 5th thing:", animation=ANIMATE_COUNT)
for i in range(21):
    a.next()
    sleep(.25)
a.finish("Success")

a = Animation("Waiting for the 6th thing with custom:", animation="|\\-/")
for i in range(21):
    a.next()
    sleep(.25)
a.finish("Success")
