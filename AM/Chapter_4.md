# Random Variable

## Definition

RV is a function $X=X(\xi)$ that maps any outcome $\xi$ to a real number.

## CDF (Cumulative Distribution Function)

$$
F_X(x) = P(X\leq x)=P(\xi|X(\xi)\leq x)
$$

It is continuous from the right.

## PDF (Probability Density Function)

$$
f_X(x) = \frac{d}{dx}F_X(x)
\\\\ F_X(x) = \int_{-\infty}^{x}f_X(u)du
$$

For discrete RV, PDF consists of Dirac functions:
$$
\delta(x) = \begin{cases} 
     0， &x\ne0  
\\\\ \infty， &x=0  
\end{cases}
$$
Properties of Dirac function:
$$
\begin{align} \int_{-\infty}^{\infty}\delta(x)dx &= 1
\\\\ \int_{-\infty}^{\infty}f(x)\delta(x-x_0)dx &= f(x_0)
\end{align}
$$

## Gaussian Distribution

$$
X \thicksim N(\mu, \sigma^2)
\\\\ f_X(x) = \frac{1}{\sqrt{2\pi}\sigma}exp\lbrace{-\frac{(x-\mu)^2}{2\sigma^2}}\rbrace
$$

## Bivariate CDF and PDF

$$
F_{XY}(x,y)=P(X\leq x,Y\leq y)
\\\\  f_XY(x,y)= \frac{\partial^2F_{XY}(x,y)}{\partial x \partial y}
$$

"$F_{XY}(x,y)$ starts with 0, increases two-dimensionally and ends up with 1."

"$f_{XY}(x,y)$ is a nonnegative function with volume 1."

## Marginal CDF and PDF

CDF: set unneeded variable to $\infty$ :
$$
F_X(x) = F_{XY}(x, \infty)
\\\\  F_Y(y) = F_{XY}(\infty, y)
$$
PDF: integrate over unneeded variable:
$$
f_X(x) = \int_{-\infty}^{\infty}F_{XY}(x,y)dy
\\\\  f_Y(y) = \int_{-\infty}^{\infty}F_{XY}(x,y)dx
$$

## Multivariate Gaussian

$$
\boldsymbol{X} \thicksim N(\boldsymbol{\mu}, \boldsymbol{C})
\\\\  f_{\boldsymbol{X}}(\boldsymbol{x}) = \frac{1}{(2\pi)^{N/2}det(C)^{1/2}}exp\lbrace{-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu})^T\boldsymbol{C}^{-1}(\boldsymbol{x}-\boldsymbol{\mu})}\rbrace
$$

if ***C*** = ***I***:
$$
f_{\boldsymbol{X}}(\boldsymbol{x}) = \frac{1}{(2\pi)^{N/2}}exp\lbrace{-\frac{1}{2}\|\boldsymbol{x}\|^2}\rbrace
$$

## Conditional CDF and PDF Given Event

CDF of X given an event B:
$$
F_X(x|B) = P(X \leq x|B)=\frac{P(X\leq x \cap B)}{P(B)}
$$
PDF:
$$
f_X(x|B) = \frac{d}{dx}F_X(x|B)
$$
They share same properties as for the conditional probability.

Law of total CDF/PDF: if
$$
B_i \cap B_j \neq \empty, \forall i \neq j
\\\\  \cup_{i}^{}{B_i} = \Omega
$$
then
$$
F_X(x) = \sum_i F_X(x|B_i)P(B_i)
\\\\  f_X(x) = \sum_i f_X(x|B_i)P(B_i)
$$
Bayes rule:
$$
F_X(x|B) = P(B|X \leq x) \frac{F_X(x)}{P(B)}
\\\\  f_X(x|B) = P(B|X = x) \frac{f_X(x)}{P(B)}
$$

## Conditional CDF and PDF Given PDF/CDF

X and Y are two (continuous) random **vector**. Consider condition B is event {Y|Y<y}, then conditional CDF of X given Y:
$$
F_\boldsymbol{X}(\boldsymbol{x}|\boldsymbol{Y}<\boldsymbol{y})=P(\boldsymbol{X}<\boldsymbol{x}|\boldsymbol{Y}<\boldsymbol{y})=\frac{F_{\boldsymbol{X},\boldsymbol{Y}}(\boldsymbol{x},\boldsymbol{y})}{F_\boldsymbol{Y}(\boldsymbol{y})}
$$
PDF can be given with B = {y < Y < y + dy}, followed by dy->0:
$$
f_\boldsymbol{X}(\boldsymbol{x}|\boldsymbol{Y}=\boldsymbol{y})=\frac{f_{\boldsymbol{X},\boldsymbol{Y}}(\boldsymbol{x},\boldsymbol{y})}{f_\boldsymbol{Y}(\boldsymbol{y})}
$$
And Bayes rule:
$$
f_\boldsymbol{X}(\boldsymbol{x}|\boldsymbol{Y}=\boldsymbol{y})=f_\boldsymbol{Y}(\boldsymbol{y}|\boldsymbol{X}=\boldsymbol{x})\frac{f_{\boldsymbol{X},\boldsymbol{Y}}(\boldsymbol{x},\boldsymbol{y})}{f_\boldsymbol{Y}(\boldsymbol{y})}
$$

## Independent Random Vector

X and Y are independent:
$$
F_{\boldsymbol{X},\boldsymbol{Y}}(\boldsymbol{x},\boldsymbol{y})=F_\boldsymbol{X}(\boldsymbol{x})F_\boldsymbol{Y}(\boldsymbol{y})
\\\\  f_{\boldsymbol{X},\boldsymbol{Y}}(\boldsymbol{x},\boldsymbol{y})=f_\boldsymbol{X}(\boldsymbol{x})f_\boldsymbol{Y}(\boldsymbol{y})
$$
Properties:

P1: Conditional PDF is the same as unconditional ones.

P2: h(x) and g(y) also independent.
$$
f_\boldsymbol{X}(\boldsymbol{x}|\boldsymbol{y})=f_\boldsymbol{X}(\boldsymbol{x})
\\\\  f_{\boldsymbol{X},\boldsymbol{Y}}(h(\boldsymbol{x}),g(\boldsymbol{y}))=f_\boldsymbol{X}(h(\boldsymbol{x}))f_\boldsymbol{Y}(g(\boldsymbol{y}))
$$

## Expectation

$$
E(X)= \int xF_X(x)dx
$$

## Moments

$\boldsymbol{\mu}=E(\boldsymbol{X})$ : mean vector of ***X***

$r_{ij}=E(X_iX_j)$ : correlation between $X_i$ and $X_j$

$r_{ii}=E(X_i^2)$ : 2. moment of $X_i$

$\boldsymbol{R}=E(\boldsymbol{X}\boldsymbol{X}^T)$ : correlation matrix of ***X***

$c_{ij}=E((X_i-\mu_i)(X_j-\mu_j))$ : covariance between $X_i$ and $X_j$

$c_{ii}=E((X_i-\mu_i)^2)=\sigma_i^2$ : variance of $X_i$ 

$\boldsymbol{C}=E((\boldsymbol{X-\mu})(\boldsymbol{X-\mu})^T)$ : covariance matrix of ***X***