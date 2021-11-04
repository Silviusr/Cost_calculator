import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.shape_base import tile

consumptions = ['water', 'food', 'taxi', 'other', 'books', 'creative']

data = [23, 17, 41, 92, 94, 7]

explode = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

wp = { 'linewidth': 1, 'edgecolor':"black"}

colors = ( "white", "cyan", "red",
          "yellow", "blue", "gold")

def func(pct,allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return "{:.1f}%\n{:d} $".format(pct, absolute)


fig, ax = plt.subplots(figsize =(10, 8))
wedges, texts, autotexts = ax.pie(data, 
                            autopct = lambda pct: func(pct,data),
                            explode = explode,
                            labels = consumptions,
                            shadow = False,
                            colors = colors,
                            startangle = 90,
                            wedgeprops = wp,
                            textprops = dict(color = 'Black'))
ax.legend(wedges, consumptions,
            title = 'Consumption',
            loc = 'center left',
            bbox_to_anchor =(1, 0, 0.5, 1))

plt.setp(autotexts, size = 8, weight = 'bold')
ax.set_title('Customize')

plt.show()
