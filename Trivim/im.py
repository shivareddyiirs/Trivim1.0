import matplotlib
import os
import numpy as np
from PIL import Image
##import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
from matplotlib.artist import Artist
from matplotlib.mlab import dist_point_to_segment
from matplotlib import backend_bases
from PyQt4 import QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from os.path import expanduser
home = expanduser("~")

with open(os.path.join(home,"Trivim.txt"),'r')as f:
       wrkdrr = f.readlines()[0]


class Annotate1(FigureCanvas):
  def __init__(self):
      self.plot = Figure()
      self.ax= self.plot.add_subplot(111)
  
      img = Image.open(os.path.join(wrkdrr,'pic_resize.jpg'))
      img = np.asarray(img)
      print img
      self.ax.imshow(img)  
      
      
      FigureCanvas.__init__(self, self.plot)
      self.mpl_connect('button_press_event', self.on_press)
      self.mpl_connect('button_release_event', self.on_release)
      self.mpl_connect('button_draw', self.draw_callback)
      self.rect = Rectangle((0,0), 1, 1, facecolor='None', edgecolor='green')
      self.x0 = None
      self.y0 = None
      self.x1 = None
      self.y1 = None
      self.ax.add_patch(self.rect)
      
      print "plot"

  def draw_callback(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)
        self.ax.figure.canvas.draw()
      
      

  def on_press(self, event):
      print 'press'
      self.x0 = event.xdata
      self.y0 = event.ydata    
      self.x1 = event.xdata
      self.y1 = event.ydata
      self.rect.set_width(self.x1 - self.x0)
      self.rect.set_height(self.y1 - self.y0)
      self.rect.set_xy((self.x0, self.y0))
      self.ax.figure.canvas.draw()

  def on_release(self, event):
      print 'release'
      self.x1 = event.xdata
      self.y1 = event.ydata
      self.rect.set_width(self.x1 - self.x0)
      self.rect.set_height(self.y1 - self.y0)
      self.rect.set_xy((self.x0, self.y0))
      self.rect.set_linestyle('solid')
      self.ax.figure.canvas.draw()
      print self.x0,self.y0,self.x1,self.y1
      global mask
      mask = [self.y0,self.y1,self.x0,self.x1]
      print mask
      array = np.asarray(mask)
      print array
      with open(os.path.join(wrkdrr,'curr_proj.txt')) as f:
        mask1 = f.readlines()[0]
      
      np.savetxt(os.path.join(mask1,'mask.txt'), array, delimiter=' , ')
      
                

    
      
class Annotate(QtGui.QWidget) :
  def __init__(self, parent = None):      
      QtGui.QWidget.__init__(self, parent)      
      self.canvas= Annotate1()
      self.vbl = QtGui.QVBoxLayout()
      self.vbl.addWidget(self.canvas)
      self.setLayout(self.vbl)
     
  
         
