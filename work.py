#!/usr/bin/env python3
import cgi

print("Content-type: text/html")
print()

form = cgi.FieldStorage()
name = form.getfirst("in_name", "не задано")
file = open('data.txt')
text = file.read()
file.close
if name in text:
    print(f"Вже бачилися, {name}")
else:
    print(f"Привіт, {name}")
    with open('data.txt', 'a') as fil: fil.write(f'{name}; ')
