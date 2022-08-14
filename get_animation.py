from examples import *
from draw import plot_curve
from PIL import Image
import os

# Indicate subdivision number

n = 4

# Indicate curve

# 2d curve examples (mono-fractal)
# get_hilbert_curve()
# get_peano_curve()
# get_meurthe_curve()
# get_coil_curve()
# get_serpentine_curve()
# get_R_curve()
# get_bauman_curve()

# 2d curve examples (bi-fractal)
# get_beta_Omega_curve()

# 2d curve examples (tetra-fractal)
# get_ARW_curve()

# 3d curve examples (mono-fractal)
# get_tokarev_curve()
# get_haverkort_curve_1()
# get_haverkort_curve_2()

# 3d curve examples (bi-fractal)
# get_neptunus_curve()
# get_luna_curve()
# get_spring_curve()


# example
curve = get_spring_curve()

if __name__ == "__main__":

    frames = []
    for k in range(0,n):
        
        sub = curve.get_subdiv(k)
        sub_n = curve.get_curve_coord(sub[0])
        
        plot_curve(sub_n, curve.dim, curve.genus, k)
        frames.append(Image.open('curve_' + str(k) + '.png'))

    frames[0].save('test.gif', format='GIF',
                   append_images=frames[1:],
                   save_all=True,
                   duration=2000, loop=0, transparency=100)

    for k in range(0,n):
        os.remove('curve_' + str(k) + '.png') 
