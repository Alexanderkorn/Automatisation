# import matplotlib.pyplot as plt
# import numpy as np
#
# matr = np.random.rand(12, 12)
#
# csf = plt.contourf(matr)
# plt.colorbar();
# plt.show()
#
# import matplotlib.pyplot as plt
# x= [ 10,20,30]
# y=['cats','dogs','fishes']
# z=[.2,.1,0]
# plt.pie(x, labels=y, explode=z)
# # plt.show()
# plt.plot([50,60,70,100,130], [.006,.010,.006,.010,.022])
# plt.title('Histogram of IQ')
# plt.xlabel('Smarts', fontsize=14, color='red')
# plt.ylabel('Probability')
# plt.text(60, .025, 'something...')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.annotate('Interesting', xy=(130,.022), xytext=(100,.025),arrowprops=dict(facecolor='black'))
# plt.show()
# y = np.random.randn(500) # generate random numbers
# print(y)
# #y = [3,4,5,3,0,6,6]
# plt.hist(y)
# plt.show()
# from __future__ import print_function
import numpy
from matplotlib.pyplot import figure, show


class IndexTracker(object):
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('use scroll wheel to navigate images')

        self.X = X
        rows, cols, self.slices = X.shape
        self.ind = self.slices//2

        self.im = ax.imshow(self.X[:, :, self.ind])
        self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = numpy.clip(self.ind + 1, 0, self.slices - 1)
        else:
            self.ind = numpy.clip(self.ind - 1, 0, self.slices - 1)

        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        ax.set_ylabel('slice %s' % self.ind)
        self.im.axes.figure.canvas.draw()


fig = figure()
ax = fig.add_subplot(111)

X = numpy.random.rand(20, 10, 40)

tracker = IndexTracker(ax, X)


fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
show()
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
y = np.random.randn(1000) + 5

# normal distribution center at x=0 and y=5
plt.hist2d(x, y, bins=50)
plt.show()
