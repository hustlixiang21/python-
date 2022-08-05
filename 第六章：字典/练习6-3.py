#!/usr/bin/env python3

glossary = {

'string': 'A series of characters.', 'comment': 'A note in a program that the Python interpreter ignores.', 'list': 'A collection of items in a particular order.', 'loop': 'Work through a collection of items, one at a time.', 'dictionary': "A collection of key-value pairs.", }

word = 'string'

print("\n{}: {}".format(word.title(),glossary[word]))

word = 'comment'

print("\n{}: {}".format(word.title(),glossary[word]))

word = 'list'

print("\n{}: {}".format(word.title(),glossary[word]))

word = 'loop'

print("\n{}: {}".format(word.title(),glossary[word]))

word = 'dictionary'

print("\n{}: {}".format(word.title(),glossary[word]))
# 低版本的python！！！草泥马！