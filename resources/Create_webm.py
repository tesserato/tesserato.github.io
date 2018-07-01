import os
import numpy as np
import moviepy.editor as mpy

path = 'Demo Finite Difference/plots/'
filenames = os.listdir(path)
filenames = [int(fn.replace('.png', '')) for fn in filenames if '.png' in fn]
filenames = np.sort(filenames)
filenames = [path + str(fn) + '.png' for fn in filenames]

clip = mpy.ImageSequenceClip(filenames, fps=48)
# clip.write_gif('clip.gif', 48, 'imagemagick', loop=0, opt='optimizeplus', fuzz=.6)
clip.write_videofile('#clip.webm', codec='libvpx', fps=48, audio=False)