import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.shape_base import tile

consumptions = ['water', 'food', 'taxi', 'other', 'books', 'creative']

data = [23, 17, 41, 92, 94, 70]

wp = { 'linewidth': 1, 'edgecolor':"white"}

colors = ( "white", "cyan", "red",
          "yellow", "blue", "gold")

def func(pct,allvalues):
    absolute = int(pct/100.*np.sum(allvalues))
    return "{p:.1f}%\n({a:d})".format(p=pct, a=absolute)

fig, ax = plt.subplots(figsize =(10, 8))
wedges, texts, autotexts = ax.pie(data, 
                            autopct = lambda pct: func(pct,data),
                            explode = None,
                            labels = consumptions,
                            shadow = False,
                            colors = colors,
                            startangle = 0,
                            wedgeprops = wp,
                            textprops = dict(color = 'Black'))
ax.legend(wedges, consumptions,
            title = 'Consumptions:',
            loc = 'center left',
            bbox_to_anchor =(1, 0, 0.5, 1))

plt.setp(autotexts, size = 8, weight = 'semibold')

ax.set_title('COST DIAGRAM')

plt.show()
