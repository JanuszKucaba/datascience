'''
Learn matplotlib
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons


x = np.arange(-2, 2, 0.01)
y1 = np.sin(x)
y2 = x * x
y3 = x ** 3

image, area = plt.subplots()
l, = area.plot(x ,y1, lw=1, color='red')
plt.subplots_adjust(left=0.3)
rax = plt.axes([0.05, 0.7, 0.18, 0.18],
                facecolor = 'lightgray')
radio = RadioButtons(rax,
        ('f(x)=sin(x)', '$f(x)=x^2$', '$f(x)=x^3$'))

def change_function(label):
    '''change function'''
    dictionary = {'f(x)=sin(x)': y1,
                  '$f(x)=x^2$': y2,
                  '$f(x)=x^3$': y3}
    l.set_ydata(dictionary[label])
    plt.draw()

radio.on_clicked(change_function)
rax = plt.axes([0.05, 0.4, 0.15, 0.15],
                facecolor = 'lightgray')
radio2 = RadioButtons(rax, ('red', 'blue', 'green'))

def function_color(label):
    '''set plot color'''
    l.set_color(label)
    plt.draw()
radio2.on_clicked(function_color)

rax = plt.axes([0.05, 0.1, 0.15, 0.15],
                facecolor = 'lightgray')
radio3 = RadioButtons(rax, ('2', '4', '6'))

def line_thickness(label):
    '''set line width'''
    l.set_linewidth(int(label))
    plt.draw()
radio3.on_clicked(line_thickness)

plt.show()
