# Terminology

**Space-filling curve** is a curve which maps a unit line segment to a continuous curve in the unit n-dimensional cube.

**Fraction** is an n-dimensional subcube, which is some partition of an n-dimensional cube.

**Genus** is the number of fractions of the first partition of an n-dimensional cube.

**Monofractal** - a curve constructed using one recurrent formula**

**Polyfractal** - a curve constructed with the help of several recurrent formulas.

**Prototype** is a way of passing through the fractions of the first partition of an n-dimensional cube.

**Basic transformation** is the operation that performs an isometric transformation of a fraction (rotation, reflection and/or reverse).

To define a curve means to specify its prototype and the sequence of basic transformations.


# Hilbert curve

Let ${\bf i} = (1,0)$, ${\bf j} = (0,1)$ and ${\bf I} = (-1,0)$, ${\bf J} = (0,-1)$ then the prototype chain code for the Hilbert curve is $P_0 = {\bf jiJ}$. The recursive formula describing this curve has the form:

$$P_{n+1} = ji(P_n),\text{ }{\bf j},\text{ }ij(P_n),\text{ }{\bf i},\text{ }ij(P_n),\text{ }{\bf J},\text{ }JI(P_n).$$

Basic transformation $ji(P_n)\to ij$ means that $j\to i$, $i \to j$ and $J\to I$, $I \to J$ for $P_n$. 

Basic transformation $JI(P_n)\to ij$ means that $J\to i$, $I \to j$ and $j\to I$, $i \to J$ for $P_n$. 

It transforms the coordinates as follows:

$$ji(P_n)=\begin{pmatrix}
j& i\\
y_1& x_1 \\
y_2& x_2 \\
\ldots& \ldots \\
y_m& x_m
\end{pmatrix},
\qquad\qquad
JI(P_n)=\begin{pmatrix}
J& I\\
-y_1& -x_1 \\
-y_2& -x_2 \\
\ldots& \ldots \\
-y_m& -x_m
\end{pmatrix}.
$$

Permuting the letters in the base transformation is equivalent to permuting the columns in the matrix, and changing the letter case is equivalent to multiplying by -1.

![image](./animation/Hilbert_curve.gif)

# Peano curve

Prototype chain code for the Peano curve is $P_0 = {\bf jjiJJijj}$. The recursive formula describing this curve has the form:

$$P_{n+1} = ij(P_n),\text{ }{\bf j},\text{ }Ij(P_n),\text{ }{\bf j},\text{ }ij(P_n),\text{ }{\bf i},\text{ }iJ(P_n),\text{ }{\bf J},\text{ }IJ(P_n),\text{ }{\bf J},\text{ }iJ(P_n),\text{ }{\bf i},\text{ }ij(P_n),\text{ }{\bf j},\text{ }Ij(P_n),\text{ }{\bf j},\text{ }ij(P_n).$$

![image](./animation/Peano_curve.gif)

# H curve

Н curve is trangular curve. It was first obtained by Niedermeier R., Reinhardt K. and Sanders P. Prototype chain code for the H curve is $P_0 = {\bf j}$. The recursive formula describing this curve has the form:

$$P_{n+1} = ij(P_n),\text{ }{\bf j},\text{ }\overline{iJ}(P_n),\text{ }{\bf i},\text{ }\overline{Ij}(P_n),\text{ }{\bf i},\text{ }ij(P_n).$$

The curve is completed to a square according to the following rule:

$$L = ij(P_n),\text{ }{\bf i},\text{ }IJ(P_n).$$

The line above the base transforms means reversal. This operation consists in changing the case of the letters of the base transformation and passing in the reverse order $P_n$.

It transforms the coordinates as follows:

$$\overline{iJ}(P_n)=\begin{pmatrix}
i& J\\
-x_m& y_m \\
\ldots& \ldots \\
-x_2& y_2 \\
-x_1& y_1
\end{pmatrix},
\qquad\qquad
\overline{Ij}(P_n)=\begin{pmatrix}
I& j\\
x_m& -y_m \\
\ldots& \ldots \\
x_2& -y_2 \\
x_m& -y_m
\end{pmatrix}.
$$

Changing the case of the letters of the base transformation is equivalent to multiplying the matrix by -1 and passing in the reverse order $P_n$ is equivalent to passing each column of the matrix in reverse order.

![image](./animation/H_curve.gif)

# $\beta\Omega$ curve

Prototype chain code for the $\beta\Omega$ curve are $P_0^{(0)} = {\bf jiJ}$ and $P_0^{(1)} = {\bf jiJ}$. The recursive formulas describing this curve has the form:

$$P_{n+1}^{(0)} = iJ(P_n^{(1)}),\text{ }{\bf j},\text{ }Ji(P_n^{(1)}),\text{ }{\bf i},\text{ }\overline{ji}(P_n^{(1)}),\text{ }{\bf J},\text{ }\overline{IJ}(P_n^{(1)})$$
$$P_{n+1}^{(1)} = iJ(P_n^{(1)}),\text{ }{\bf j},\text{ }Ji(P_n^{(1)}),\text{ }{\bf i},\text{ }\overline{ji}(P_n^{(1)}),\text{ }{\bf J},\text{ } jI(P_n^{(0)})$$

![image](./animation/beta_Omega_curve_1.gif) ![image](./animation/beta_Omega_curve_2.gif)

# $AR^2W^2$ curve

![image](./animation/ARW_curve_1.gif) ![image](./animation/ARW_curve_2.gif)
![image](./animation/ARW_curve_3.gif) ![image](./animation/ARW_curve_4.gif)










