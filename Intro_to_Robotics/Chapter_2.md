# Spatial Descriptions and Transformations

### Rotation Matrix

$$
{}^A_B\!R = [ \begin{array}{c} {}^A\!\hat{X}_B & ^A\!\hat{Y}_B  & {}^A\!\hat{Z}_B \end{array}] \\\\
{}^B_A\!R = {}^A_B\!R^{-1} = {}^A_B\!R^T
$$

$^A\hat{X}_B$ is the unit vector along frame B's x direction, described in frame A

### Transformation Matrix
$$
\begin{align} {}^A_B\!T &= \begin{bmatrix} ^A_B\!R & {}^A\!P_{BORG} \\ 0^T & 1 \end{bmatrix} \\\\
{}^A_C\!T &= {}^A_B\!T {}^B_C\!T \\\\
^A\!P &= {}^A_B\!T ^B\!P \\\\
^A\!P &= {}^A_B\!R ^B\!P + {}^A\!P_{BORG}
\end{align}
$$
### Euler Angle

- around axes of fixed reference frame
- around axes of rotated reference frame (itself)
- x-y-z fixed angles equivalent z-y-x euler angle

formula see book (2-64)

### Angle-Axis

Rodrigues' rotation formula, see book (2-80)

### Quaternion

$$
\begin{align}
q_1 = k_xsin(\theta/2) \\\\
q_2 = k_ysin(\theta/2) \\\\
q_3 = k_zsin(\theta/2) \\\\
q_4 = cos(\theta/2) \\\\
\end{align}
$$

### Free Vector

During transformation, apply only the rotation, no translation