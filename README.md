# Terminology

**Space-filling curve** is a curve which maps a unit line segment to a continuous curve in the unit n-dimensional cube.

**Fraction** is an n-dimensional subcube, which is some partition of an n-dimensional cube.

**Genus** is the number of fractions of the first partition of an n-dimensional cube.

**Prototype** is a way of passing through the fractions of the first partition of an n-dimensional cube

**Basic transformation** is the operation that performs an isometric transformation of a fraction (rotation, reflection and/or reverse).

# Hilbert curve

Let **i** = (1,0), **j** = (0,1), **I** = (-1,0) and **J** = (0,-1) then the prototype chain code for the Hilbert curve is P_0 = **jiJ**. The recursive formula describing the curve has the form:



<img src="https://latex.codecogs.com/gif.latex?O_t= $$P_{n+1} = ji(P_n), {\bf j}, ij(P_n), {\bf i}, ij(P_n), {\bf J}, JI(P_n)$$ "/> 

![image](./animation/Hilbert_curve.gif)
