#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
import time, datetime


def xor(k, str):
    repeat = math.ceil(len(str) / len(k))
    repeatkey = k * repeat
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str, repeatkey))


def encrypt(key, msg):
    tsenc = xor(datetime.datetime.fromtimestamp(time.time()).strftime('%Y.%m.%d.%H'), msg)
    keyenc = xor(key, tsenc)
    return keyenc


def decrypt(key, msg):
    keydec = xor(key, msg)
    tsdec = xor(datetime.datetime.fromtimestamp(time.time()).strftime('%Y.%m.%d.H'), keydec)
    return tsdec