# Savage Son
# v1.1
# workbench.tv

import sys
import re
from math import sin, cos

def printElement(pts, name):
    print("// {}".format(name or 'untitled'))
    print("{")
    print("\tpoints: '{}',".format(pts))
    print("\tcolor: colorGroups.{}".format(name.lower() or 'untitled'))
    print("},")

file =  sys.argv[1]
f = open(file, 'r')
if f.mode == 'r':
    xml = f.read()

    # Match rectangles
    matches = re.findall(r"rect (?:id=\"([a-zA-Z0-9]+)[_\S]*\" )?(?:x=\"([0-9.]+)\" )?(?:y=\"([0-9.]+)\" )?(?:class=\"[\S]+\" )?width=\"([0-9.]+)\" height=\"([0-9.]+)\"", xml)
    if(matches):
        for match in matches:
            x = float(match[1] or 0.0)
            y = float(match[2] or 0.0)
            w = float(match[3])
            h = float(match[4])
            pts = "{:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f}".format(x, y, x + w, y, x + w, y + h, x, y + h)

            printElement(pts, match[0])

    # Match circles
    matches = re.findall(r"circle (?:id=\"([a-zA-Z0-9]+)[_\S]*\" )?(?:class=\"[\S]+\" )?cx=\"([0-9.]+)\" cy=\"([0-9.]+)\" r=\"([0-9.]+)\"", xml)
    if(matches):
        for match in matches:
            x1 = float(match[1])
            y1 = float(match[2])
            r = float(match[3])
            a_increment = 0.174533
            pts = ""
            for i in range(0, 36):
                a = i * a_increment
                x = round(cos(a) * r + x1, 1)
                y = round(sin(a) * r + y1, 1)
                pts += "{:.2f},{:.2f} ".format(x, y,)
            printElement(pts.rstrip(), match[0])


    # Match polygon points
    matches = re.findall(r"(?:id=\"([a-zA-Z0-9]+)[_\S]*\" )?(?:class=\"[\S]+\" )?points=\"([0-9., \r\n\t]+)\"", xml, re.MULTILINE)
    if(matches):
        for match in matches:
            pts = re.sub(r"([\r\n\t]+)", " ", match[1])
            pts = re.sub(r"([ ]{2})", " ", pts)
            printElement(pts.rstrip(), match[0])
    f.close()
