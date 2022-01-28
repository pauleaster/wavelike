import matplotlib.pyplot as plt
import numpy as np

WAVELENGTH = 100
THRESHOLD = 0.95

KVAL = 2 * np.pi / WAVELENGTH

def peak( x, y, x_origin, y_origin):
    dist =  np.sqrt((x - x_origin) ** 2 + (y - y_origin) **2)
    intensity = np.cos(dist * KVAL)
    if intensity > THRESHOLD:
        return 1
    return 0
    retu

def superposition( x, y, x1, y1, x2, y2):

    dist1 =  np.sqrt((x - x1) ** 2 + (y - y1) **2)
    dist2 =  np.sqrt((x - x2) ** 2 + (y - y2) **2)

    intensity = np.cos(dist1 * KVAL) + np.cos(dist2 * KVAL)
    # if intensity > THRESHOLD:
    #     return 1
    # return 0
    return intensity



XMAX = 1600
YMAX = 900


DX = 200
X1 = XMAX/2 - DX/2
Y1 = 1
X2 = XMAX/2 + DX/2




x_vals = [x for x in range(0, XMAX)]

y_vals = [y for y in range(0, YMAX)]

wave1 = [[peak(x, y, X1, Y1) for x in x_vals] for y in y_vals]
wave2 = [[peak(x, y, X2, Y1) for x in x_vals] for y in y_vals]


# plt.figure()
# plt.contourf(x_vals, y_vals, wave1)

# plt.figure()
# plt.contourf(x_vals, y_vals, wave2)

plt.figure()
both_waves = [[superposition(x, y, X1, Y1, X2, Y1) for x in x_vals] for y in y_vals]
plt.contourf(x_vals, y_vals, both_waves)

plt.show()


