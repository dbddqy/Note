# Bayesian Decision Theory

## Probabilistic Signal Model

$\omega \in \lbrace \omega_1,\omega_2,...,\omega_c\rbrace$ : unknown true class. 

$\underline{x} \in \mathbb{R}^d$ : feature vector

$P(\omega=\omega_i) = P(\omega_i)$ : a priori probability

$P(\underline{x}|\omega=\omega_i) = P(\underline{x}|\omega_i)$ : likelihood

$P(\underline{x},\omega=\omega_i) = P(\underline{x},\omega_i)$ : joint PDF of x and w

$P(\underline{x})$ : marginal PDF of x, called evidence

$P(\omega=\omega_i|\underline{x}) = P(\omega_i|\underline{x})$ : a posteriori probability

## Bayesian Theorem:

$$
P(\omega_i|\underline{x}) = \frac{P(\underline{x}|\omega_i)P(\omega_i)}{P(\underline{x})}
$$

## Loss Matrix:

$$
\underline{\underline{L}} = [l_{ij}]_{c\times c} \\\\
l_{ij}=loss(w=i,\hat{w}=j)
$$

Of course diagonal elements are 0, means correct decision.

## Minimum Bayesian Risk (MBR):

Bayesian Risk = Loss Matrix * Posterior
$$
\left[ \begin{array}{c}
R(\hat{\omega}=\omega_1|\underline{x}) \\
... \\
R(\hat{\omega}=\omega_c|\underline{x}) 
\end{array} 
\right ] = \underline{\underline{L}}
\left[ \begin{array}{c}
P(\hat{\omega}=\omega_1|\underline{x}) \\``
... \\
P(\hat{\omega}=\omega_c|\underline{x}) 
\end{array} 
\right ] \\\\
$$

## Maximum A Posteriori (MAP):

Assuming 0-1 loss, MAP is special case of MBR.

## Maximum Likelihood (ML)

With equal priors, ML is special case of MAP.