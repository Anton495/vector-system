from examples import *
from draw import plot_curve

# Indicate subdivision number

n = 2

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

sub = curve.get_subdiv(n)
sub = curve.get_curve_coord(sub[0])

plot_curve(sub, curve.dim, curve.genus, n)
