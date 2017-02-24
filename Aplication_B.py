
'''
import csv
from collections import Counter
counts = Counter()
with open ('zoo.csv') as fin:
    cin = csv.reader(fin)
    for num, row in enumerate(cin):
        if num > 0:
            counts[row[0]] += int (row[-1])
        for animal, hush in counts.items():
            print("%10s %10s" % (animal, hush))
'''

'''
import bubbles
p = bubbles.Pipeline()
p.source(bubbles.data_object('csv_source', 'zoo.csv', inter_field=True))
p.aggregate('animal', 'hush')
p.pretty_print()
'''

def display_shapefile(name, iwidth=500, iheight=500):
    import shapefile
    from PIL import Image, ImageDraw
    r = shapefile.Reader(name)
    mleft, mbottom, mright, mtop = r.bbox
    # map units
    mwidth = mright - mleft
    mheight = mtop - mbottom
    # scale map units to image units
    hscale = iwidth/mwidth
    vscale = iheight/mheight
    img = Image.new("RGB", (iwidth, iheight), "white")
    draw = ImageDraw(img)
    for shape in r.shapes():
        pixels = [
            (int(iwidth - ((mright - x) * hscale)), int((mtop - y) * vscale))
        for x, y, in shape.points]
        if shape.shapeType == shapefile.POLYGON:
            draw.polygon(pixels, outline='black')
        elif shape.shapeType == shapefile.POLYLINE:
            draw.line(pixels, fill='black')
    img.show()
if __name__=="__main__":
    import sys
    display_shapefile(sys.argv[1], 700, 700)


































