# Probability

## Notations and Definitions

Consider a random experiment, **outcome** $\xi$ describes one particular result. **Event** *A* is a set of outcome. **Sample space**  $\Omega$ is set of all possible outcomes. 
$$
\xi \in \Omega
\\\\ A \subset \Omega
$$

## Conditional Probability

Conditional probability reduces the sample space $\Omega$ to a subset of it, denoted as *B* here:
$$
P(A|\Omega) = \frac{P(A\cap \Omega)}{P(\Omega)} = P(A)
\\\\ P(A|B) = \frac{P(A\cap B)}{P(B)}
$$

## Bayes Rule

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$



## Law of Total Probability

Given:
$$
B_i \cap B_j \neq \empty, \forall i \neq j
\\\\  A \subset \cup_{i}^{}{B_i}
$$ {/end}
then:
$$
P(A) = \sum_{i}P(A|B_i)P(B_i)
$$

## Chain Rule of Probability

$$
P(A_1\cap A_2\cap \cdots \cap A_N) = P(A_1|A_2\cap \cdots \cap A_N)\cdots P(A_{N-1}|A_N)P(A_N)
$$
## Independent

A and B are independent, then:
$$
P(A|B)=P(A)
\\\\ P(A,B)=P(A)P(B)
$$
So if A<sub>1</sub>,  A<sub>2</sub>, ...,  A<sub>N</sub> are independent, then:
$$
P(A_1\cap A_2\cap \cdots \cap A_N) = P(A_1)\cdots P(A_{N-1})P(A_N)
$$

