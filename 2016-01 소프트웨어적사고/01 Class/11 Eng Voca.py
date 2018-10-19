#!/usr/bin/python
# -*- coding: utf-8 -*-

f = open("11-OnlineVocaList.txt", "r")

wordset = {}


print(f.read())

for data in f:
    data_parsed = data.strip().split("\t")
    print(data_parsed)
