# Inverse manipulator kinematics

Dextrous workspace: 

> the volume of space that the robot end-effector can reach with all orientations

Reachable workspace:

> the volume of space that the robot can reach in at least one orientation.

Multiple solutions:

- choose the closest one
- or consider collision when there is obstacle

### Analytical Solution (Closed-Form)

Possible only when many alphas are 0 or 90 degrees.

Wrist-partition robot always has closed-form solution.

Has to be solved individually by each specific type of robot.

### Numerical Solution

- Jacobian Pseudo Inverse: need to calculated inverse, sensitive to singularity, but convergent very fast
- Jacobian Transpose: robust around singularity, but need way more iterations to convergent