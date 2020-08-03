# Manipulator Kinematics

### DH Parameters (modified)

Procedures to set up frames all each joint:

1. Identify the joint axes
2. Identify the common perpendicular between them, choose its intersection with i-th axis as origin of {i}. (if parallel, any point can be chosen )
3. Assign z along i-th axis
4. Assign x along common perpendicular
5. Assign y to complete a right-hand coordinate system
6. Assign {0} to match {1} when the first joint variable is zero. For {N}, choose an origin location and x direction freely, but generally so as to cause as many linkage parameters as possible to become zero.

Parameters:

- a: translate along x, align z
- alpha: rotate around x, align z
- d: translate along z, align origin
- theta: rotate around z, align x

Transformation matrix formula see book (3-6)

**Get forward kinematics formula by multiplying all transformation matrix together.**