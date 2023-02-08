# savageSon
Savage Son converts svg to points for use with [scriptui-battlestyle]

## Basic Usage

1. Put SavageSon.py somewhere
2. Run it with `python3 savageSon.py YOUR_SVG_FILE`
3. Profit

## Conversions

Savage Son takes rectangles and converts them to points. It grabs polygon points directly. And finally, it will also take circles and make them 36 point polygons since you can't use curves in icons for After Effects. If you have bezier lines, you'll have to resample those yourself in Illustrator or whatever.

## Notes

I have only tested this with Illustrator-formatted SVGs, which I'm assuming you probably have if you're developing for After Effects.

[scriptui-battlestyle]: https://github.com/adamplouff/scriptui-battlestyle
