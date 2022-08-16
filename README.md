# Terminology

**Space-filling curve** is a curve which maps a unit line segment to a continuous curve in the unit n-dimensional cube.

**Fraction** is an n-dimensional subcube, which is some partition of an n-dimensional cube.

**Genus** is the number of fractions of the first partition of an n-dimensional cube.

**Prototype** is a way of passing through the fractions of the first partition of an n-dimensional cube

**Basic transformation** is the operation that performs an isometric transformation of a fraction (rotation, reflection and/or reverse).

# Hilbert curve

Let ${\bf i} = (1,0)$, ${\bf j} = (0,1)$, ${\bf I} = (-1,0)$ and ${\bf J} = (0,-1)$ then the prototype chain code for the Hilbert curve is $P_0 = {\bf jiJ}$. The recursive formula describing the curve has the form:

$$P_{n+1} = ji(P_n),\text{ }{\bf j},\text{ }ij(P_n),\text{ }{\bf i},\text{ }ij(P_n),\text{ }{\bf J},\text{ }JI(P_n).$$

Basic transformation $ji(P_n)\to ij$ means that $j\to i$, $i \to j$ and $J\to I$, $I \to J$ for $P_n$. 

Basic transformation $JI(P_n)\to ij$ means that $J\to i$, $I \to j$ and $j\to I$, $i \to J$ for $P_n$. 

It transforms the coordinates as follows:


![image](./animation/Hilbert_curve.gif)
