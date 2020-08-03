# Model Capacity and Overfitting

## Regularization

add penalty terms P(W)
$$
L_r(\theta)=L(\theta)+P(W)
$$


- L2: prefer smaller weight 
  $$
  P(W) = ||vector(W)||_2^2
  $$

- L1: 
  $$
  P(W) = ||vector(W)||_1
  $$
  

## Early Stopping

stop when testing error begins to increase

## Data Augmentation

easy for classification, modify input sample a bit without changing class label

## Dropout

During each minibatch, randomly set the output of some neurons in layer l to zero.

## Hyperparameter Optimization

Grid search, try and error. Require a validation set.