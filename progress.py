# -*- coding: utf-8 -*-
from sys import stdout


class ProgressBar(object):
    def __init__(self,
                 message, max_value=100,
                 bg=None, fg=None, br=None, width=20):
        self._bg = bg or u"░"
        self._fg = fg or u"▓"
        self._bl = br[0] if br else ''
        self._br = br[1] if br else ''
        self._width = width
        self._message = message
        self._max = float(max_value)
        self._value = 0

    def _get_status_text(self):
        _bg, _fg = '', ''
        _p = self._value / self._max
        _c = int(self._width * _p)
        if self._value == 0:
            _bg = self._bg * self._width
        elif _c < self._width:
            _fg = self._fg * _c
            _bg = self._bg * (self._width - _c)
        else:
            _c = self._max
            _p = 1
            _fg = self._fg * int(self._max)

        return "".join([
            self._message,
            " ",
            self._bl,
            _fg,
            _bg,
            self._br,
            " ",
            "{}/{} {}%".format(int(_c), int(self._max), _p * 100)
        ])

    def update(self, value):
        self._value = value
        line = self._get_status_text()
        stdout.write("".join([line, '\r']))
        stdout.flush()

    def finish(self, message, success=True):
        self._value = int(self._max) if success else self._value
        line = self._get_status_text()
        print "".join([
            line,
            " [{}]".format(message)
        ])

    def finish_and_replace(self, message):
        x = self._get_status_text()
        _overlap = len(x) - len(message)
        filler = " "
        if _overlap > 0:
            filler = filler * _overlap

        print "".join([message, filler])
