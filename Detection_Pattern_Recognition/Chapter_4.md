# Supervised Learning

## Template Matching

### Nearest Mean

![](pics/nearest_mean.png)

Note:

- **Mahalanobis Distance** is robust to feature transforms
- multi-class classifier
- fails in **non-linear-separable** dataset.

### K-Nearest Neighbor

![](pics/k_nearesr_neighbor.png)

Note:

- simple and very robust
- k=1 always leads to overfitting
- multi-class classifier
- search for nearest neighbor is super expensive, need special data structure like kd-tree, octree to speed up.

## Bayes plug-in

### Gaussian Classifier

![](pics/gaussian_classifier.png)

Note:

- becomes nearest mean if all classes have identical C and $\mu$
- need lots of data, usually around 10 times the vector length d
- fails in **non-linear-separable** dataset.

### Naive Gaussian

just assume C is diagonal, reduce training time and amount of required data.

### Gaussian Mixture Model (GMM)

![](pics/GMM_0.png)

![](pics/GMM_1.png)

Note:

- versatile, can approximate many real-life distributions
- sensitive to the choice or estimation of model orders Mj
- nonconvex optimization, possible convergence to local optimum, sensitive to initialization of EM

## Discriminant Function

This approach can be considered as directly modeling posteriori with estimating the likelihood.

### Neural Network

see course deep learning

### Support Vector Machine

basic ideas:

- binary classifier
- use a linear discriminant function

new ideas:

- non-linear feature mapping (kernel functions)
- maximum margin (instead of least squares)
- convex optimization

**Hard margin SVM:**

![](pics/hard_SVM.png)

Note:

- dataset **must be linear separable**

**Soft margin SVM:**

![](pics/soft_SVM.png)

![](pics/soft_SVM_2.png)

Note:

- can solve significantly larger set of problems
- sensitive to the choice of hyperparameters $\gamma$ and C. They have to be optimized

**Multi-class SVM:** 

1. one against one
   - need to train $\tbinom{c}{2}$ SVMs for all pairs of class
   - the class with most wins wins

2. one against the rest
   - need to train c SVMs
   - choose the class with the highest f(x)

3. hierarchical


## Validation

k-fold cross validation: (k − 2)/1/1 folds for training/validation/test