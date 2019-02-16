#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from __future__ import unicode_literals
import matplotlib.pyplot as plt
from pylab import *


plt.plot([0, 10, 20, 30, 35],
         [1.34, 1.35, 1.365, 1.395, 1.41])

plt.axis([0, 40, 1.32, 1.42])  # задание [xmin, xmax, ymin, ymax]

plt.xlabel(u'Концентрация раствора, %', family="verdana")    # обозначение оси абсцисс
plt.ylabel(u'Показатель преломления n', family="verdana")    # обозначение оси ординат

plt.title(u'Желатин', family="verdana")  # название графика
#plt.legend()       # вставка легенды (текста в label)
#text(20, 1.4,u'Желатин', fontsize = 18, family="verdana")

plt.grid(True)

savefig("n_from_c.png", dpi=300)
plt.show()
