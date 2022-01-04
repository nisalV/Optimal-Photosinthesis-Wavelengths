#   GPL Project - Group 05
#   Week 04 - Slurry Analysis 01
#   The Graph of Intensity vs Wavelength
#   and The Graph of Absorbence vs Wavelength

#   IMPORTANT : You have to edit in 06 different locations in the code
#   The locations are commented in the code.
#   Please edit them according to your spectres

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import math

def spec(img_name):
    im = Image.open(img_name)
    pix = im.load()
    width, height = im.size

    x_all = []
    y_all = []
    wl_start = 320
    wl_end = 720
    wl_range = wl_end - wl_start
    wl_p_pix = wl_range / width

    for i in range(0, width):
        s = 0.0
        c = 0
        for j in range(0, height):
            RGB = pix[i, j]
            s += 0.21 * int(RGB[0]) + 0.72 * int(RGB[1]) + 0.07 * int(RGB[2])  # luminosity method
            c += 1.0

        x_all.append(i * wl_p_pix + wl_start)
        y_all.append(s / c)

    y_all = np.array(y_all)

    index_max = np.where(y_all == max(y_all))
    index_max = np.array(index_max, dtype='i')
    peak_start = (index_max[0][0] - 1) * wl_p_pix + wl_start
    last_index = len(index_max)
    peak_end = (index_max[last_index - 1][0]) * wl_p_pix + wl_start
    max_x = (peak_end + peak_start) / 2
    max_in_wl_err = (peak_end - peak_start) / 2

    return [x_all, y_all, max_x]


# (01) You may have to edit here if you have a less amount of spectrum
x0, y0, max_x0 = spec('00.jpg')     # Light Source
x1, y1, max_x1 = spec('01.jpg')

# Graph 01
# (02) You may have to edit here if you have different concentration values and less amount of spectres
plt.plot(x0, y0, label='Light Source')        # Light Source
plt.plot(x1, y1, label='Through leaf')
plt.legend(loc='upper left')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('The Graph of Intensity vs Wavelength')
plt.show()

# (03) You may have to edit here if you have less amount of spectres
t1 = y1 / y0

# (04) You may have to edit here if you have a less amount of spectres
a1 = -(np.log10(t1))

# Graph 02
# (05) You may have to edit here if you have different concentration values and less amount of spectres

plt.plot(x0, a1, label='Through leaf')

# (06) You must edit the 2 values according to the peaks that you wish to chose in your second graph
wl1 = 450 # Enter here the first peak wavelength
wl2 = 713  # Enter here the Second peak wavelength

plt.axvline(x=wl1, linestyle='--', label='%.1f nm' % wl1)
plt.axvline(x=wl2, linestyle='--', label='%.1f nm' % wl2)

plt.xlabel('Wavelength (nm)')
plt.ylabel('Absorbance')
plt.title('The Graph of Absorbance vs Wavelength')
plt.legend(prop={'size':10})
plt.show()
