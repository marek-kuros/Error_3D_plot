import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from matplotlib import cm

BAR_SIZE = 5

def read_csv():
    df = pd.read_csv('Errors.csv')
    x = df['X']
    y = df['Y']
    z = df['ERROR']
    return x, y, z

def plot_error():
    # set up the figure and axes
    fig = plt.figure(figsize=(15, 15))
    ax1 = fig.add_subplot(111, projection='3d')

    # fake data

    x, y, z = read_csv()
    x, y = np.meshgrid(x, y)
    bottom = np.zeros_like(z)

    ax1.bar3d(x, y, z, BAR_SIZE,  BAR_SIZE, BAR_SIZE, shade=True)
    ax1.set_title('Error')

    plt.show()

# def test():
#     xAmplitudes, yAmplitudes, zAmplitudes = read_csv()

#     x = np.array(xAmplitudes)   #turn x,y data into numpy arrays
#     y = np.array(yAmplitudes)

#     fig = plt.figure()          #create a canvas, tell matplotlib it's 3d
#     ax = fig.add_subplot(111, projection='3d')
    
#     # hist, xedges, yedges = np.histogram2d(x, y, bins=(20,20))
#     # xpos, ypos = np.meshgrid(xedges[:-1]+xedges[1:], yedges[:-1]+yedges[1:])

#     xpos = xpos.flatten()/2.
#     ypos = ypos.flatten()/2.
#     zpos = np.zeros_like (xpos)

#     dx = xedges [1] - xedges [0]
#     dy = yedges [1] - yedges [0]
#     dz = hist.flatten()

#     cmap = cm.get_cmap('jet') # Get desired colormap - you can change this!
#     max_height = np.max(dz)   # get range of colorbars so we can normalize
#     min_height = np.min(dz)
#     # scale each z to [0,1], and get their rgb values
#     rgba = [cmap((k-min_height)/max_height) for k in dz] 

#     ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=rgba, zsort='average')
#     plt.title("X vs. Y Amplitudes for ____ Data")
#     plt.xlabel("My X data source")
#     plt.ylabel("My Y data source")
#     plt.savefig("Your_title_goes_here")
#     plt.show()  
plot_error()
#test()