# Machine Learning Basics

## Estimate of PDF and CDF from data

x(n), n=1,2,...,N are i.i.d. samples drawn from $p(x) \thicksim N(0, 1)$. The empirical PDF and CDF can be calculated as:
$$
\hat{p}(x)=\frac{1}{N}\sum_{x=1}^N \delta(x-x(n))
\\\\ \hat{F}(x)=\frac{1}{N}\sum_{x=1}^N u(x-x(n))
$$
u(x) is the unit step function and $\delta$(x) is Dirac function.

![](pics/pdf_cdf_from_data.png)

## Kullback–Leibler Divergence

Let p(x) and q(x) be two distribution of random vector **x**
$$
D_{KL}(p||q) = \int p(x)ln(\frac{p(x)}{q(x)})dx = E_{x\thicksim p}\frac{p(x)}{q(x)} \overset{disc}{=} \sum_{i=1}^cln(\frac{p(x)}{q(x)})
$$
Properties:

1. non-negative
2. equality $D_{KL}(p||q)=0 \Leftrightarrow p(x)=q(x)$
3. asymmetry $D_{KL}(p||q) \ne D_{KL}(p||q)$

Minimizing D_KL is equivalent to minimizing **Cross Entropy**
$$
H(p,q)=-\int_{-\infty}^{\infty}p(x)ln(q(x))dx
$$
