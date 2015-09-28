# -*- coding: utf-8 -*-
from time import time
from sys import stdout
from termcolor import colored


ANIMATE_VGROW = u"▇▆▅▄▃▂▃▄▅▆▇"
ANIMATE_HGROW = u"▉▊▋▌▍▎▏▎▍▌▋▊▉"
ANIMATE_SPIN = u"◑◒◐◓"
ANIMATE_COUNT = u" ⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟" + \
                u"⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"


class Animation(object):
    def __init__(self, message, animation=ANIMATE_SPIN, freq=3):
        self._message = message
        self._animation = animation
        self._wait = 1/float(freq)
        self._time = None
        self._index = 0

    @classmethod
    def create(cls, message, animation=ANIMATE_SPIN, freq=3):
        _a = cls(message, animation, freq)
        return _a.__iter__()

    def _get_status_text(self, anichar, color="green"):
        return "".join([
            " [",
            colored(anichar, color),
            "] ",
            self._message,
            "\r"
        ])

    def __iter__(self):
        # Initialize the time so the delta calculation does
        # not error out.
        return self

    def __next__(self):
        return self.next()

    def next(self):
        # Initialize delta
        if not self._time:
            self._time = time() - self._wait

        # Calculate last delta and skip of no update is needed
        delta = time() - self._time
        if self._wait > delta:
            # Nothing to do yet
            return
        self._time = time()

        # Find new animation char
        c = self._animation[self._index % len(self._animation)]
        self._index += 1

        # Assemble the message line
        line = self._get_status_text(c)

        # Put it on the screen
        stdout.write(line)
        stdout.flush()

    def finish(self, message, success=True):
        print self._get_status_text(message, "green" if success else "red")

    def finish_and_replace(self, message):
        x = self._get_status_text(' ')
        _overlap = len(x) - len(message)
        filler = " "
        if _overlap > 0:
            filler = filler * _overlap

        print "".join([message, filler])
