import numpy as np
from plotting import plot_curve

def get_H_curve_coord(n):

    #The definition of basis vectors and the origin
    O = np.array([[ 0 , 0 ]])
    i = np.array([[ 1 , 0 ]])
    j = np.array([[ 0 , 1 ]])

    #Curve Prototype (null curve subdivision)
    proto = j

    #Generating the n-th subdivision of the curve
    sub_n = proto
    for k in range(n):
    
        #Base mapping of second fraction and reverse
        iJ = np.column_stack((sub_n[:,0],-sub_n[:,1]))
        iJ1 = -np.flipud(iJ)

        #Base mapping of third fraction and reverse
        Ij = np.column_stack((-sub_n[:,0],sub_n[:,1]))
        Ij1 = -np.flipud(Ij)
    
        #Generating following subdivision
        sub_n = np.concatenate([sub_n, j, iJ1, i, Ij1, i, sub_n])

    #Joining the two triangles
    sub_n = np.concatenate([sub_n,i,-sub_n])

    #Generating curve coordinates
    sub_n = np.cumsum(np.concatenate([O,sub_n]),axis = 0)
    
    return sub_n

#Indicate subdivision number and run
n = 1

sub_n = get_H_curve_coord(n)

plot_curve(sub_n, 2, 4, n)
