# Savage Son
# v1.0
# workbench.tv

import sys
import re
from math import sin, cos

def printElement(pts):
    print("{")
    print("\tpoints: '{}',".format(pts))
    print("\tcolor: colorGroups.normal")
    print("},")

file =  sys.argv[1]
f = open(file, 'r')
if f.mode == 'r':
    xml = f.read()

    # Match rectangles
    matches = re.findall(r"rect x=\"([0-9.]+)\" y=\"([0-9.]+)\" width=\"([0-9.]+)\" height=\"([0-9.]+)\"", xml)
    if(matches):
        for match in matches:
            x = float(match[0])
            y = float(match[1])
            w = float(match[2])
            h = float(match[3])
            pts = "{} {} {} {} {} {} {} {}".format(x, y, x + w, y, x + w, y + h, x, y + h)

            printElement(pts)

    # Match circles
    matches = re.findall(r"circle cx=\"([0-9.]+)\" cy=\"([0-9.]+)\" r=\"([0-9.]+)\"", xml)
    if(matches):
        for match in matches:
            x1 = float(match[0])
            y1 = float(match[1])
            r = float(match[2])
            a_increment = 0.174533
            pts = ""
            for i in range(0, 36):
                a = i * a_increment
                x = round(cos(a) * r + x1, 1)
                y = round(sin(a) * r + y1, 1)
                pts += "{},{} ".format(x, y,)
            printElement(pts.rstrip())


    # Match polygon points
    matches = re.findall(r"points=\"([0-9., \r\n\t]+) \"", xml, re.MULTILINE)
    if(matches):
        for match in matches:
            pts = re.sub(r"([\r\n\t]+)", " ", match)
            printElement(pts)
    f.close()
