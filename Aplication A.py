

'''
from PIL import Image
img = Image.open('cat.jpg')
print(img.format)
print(img.size)
print(img.mode)
#img.show()
'''


'''
crop = (100, 100, 200, 200)
img2 = img.crop(crop)
img2.show()
img2.save('cropped.gif', 'GIF')
img3 = Image.open('cropped.gif')
print(img3.format)
print(img3.size)
'''

'''
mustache = Image.open('moustaches.png')
handlebar = mustache.crop((316, 282, 394, 310))
img.paste(handlebar, (130, 250))
img.show()
'''

'''
from wand.image import Image
from wand.display import display

img = Image(filename='can.jpg')
print(img.size)
print(img.format)
'''

'''
import tkinter
from PIL import  Image, ImageTk

main = tkinter.Tk()
img = Image.open('cat.jpg')
tkimg = ImageTk.PhotoImage(img)
tkinter.Label(main, image=tkimg).pack()
main.mainloop()
'''

import matplotlib.pyplot as plot
import matplotlib.image as image

img = image.imread('cat.jpg')
plot.imshow(img)
plot.show()




































