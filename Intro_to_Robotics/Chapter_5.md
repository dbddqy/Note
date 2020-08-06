# Jacobians: velocities and static forces

### Relative Velocity

${}^A\!({}^B\!V_{Q})$ is the velocity of Q relative to {B}, described in {A}

${}^A\!({}^A\!V_{Q})$ can be written as ${}^A\!V_{Q}$

${}^U\!V_{CORG}$ can be written as $v_c$ (U is the world frame)

### Observation of motion in {B} from {A}

$$
{}^A\!V_Q={}^A\!V_{BORG}+{}^A_B\!R {}^B\!V_Q + {}^A\!\Omega_B \times {}^A_B\!R {}^B\!Q \tag{5-13}
$$

three parts:

- velocity of {B} origin relative to {A}
- velocity of Q relative to {B}, described in {A}
- effect caused by rotation of {B}, relative to {A}

### Velocity "propagation"

a special case of (5-13)
$$
{}^{i+1}\!\omega_{i+1} = {}^{i+1}_i\!R {}^i\!\omega_i + \dot{\theta}_{i+1} {}^{i+1}\!\hat{Z}_{i+1} \tag{5-45} 
$$

$$
{}^{i+1}\!v_{i+1} = {}^{i+1}_i\!R({}^i\!v_i+{}^i\!\omega_i \times {}^i\!P_{i+1}) \tag{5-46}
$$

### Jacobian (6*N)

$$
\begin{bmatrix} v \\ \omega \end{bmatrix} = J(\theta)\dot{\theta} \tag{5-64}
$$

$$
J(\theta) = \begin{bmatrix}
\hat{Z}_0 \times (O_N - O_0) & \hat{Z}_1 \times (O_N - O_1) & \cdots \\ 
\hat{Z}_0 & \hat{Z}_1 & \cdots
\end{bmatrix}
$$

transform 6*6 jacobian from {B} to {A}:
$$
{}^A\!J(\theta) = \begin{bmatrix} {}^A_B\!R & 0 \\ 0 & {}^A_B\!R \end{bmatrix} {}^B\!J(\theta) \tag{5-71}
$$

### Singularity

$$
det(J(\theta)) = 0
$$

- Workspace-boundary singularities: when it is fully stretched out or folded back
- Workspace-interior singularities: when multiple joints line up

### Static force

According to the principle of virtual work:
$$
\tau = J^T \mathcal{F}
$$
$\mathcal{F}$ consists of force and moment at the end, which can be mapped to joint torque by jacobian transpose
