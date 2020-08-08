

# K-means for clustering

Generate 60 data points, and divide them into 4 clusters. Centers of each cluster randomly chosen.

```python
n = 60
x_train, y_train, x_test, y_test = generate_data(n)
K = 4

# initialization
center_indices, cluster_indices = [], []
for i in range(K):
    center_indices.append(random.randint(0, len(x_train)-1))
    cluster_indices.append([])
```

Assigning label for all the samples

```python
for i in range(len(x_train)):
    sample = x_train[i]
    nearest_label = 0
    for label in range(K):
        center_index = center_indices[label]
        if distance(sample, x_train[center_index]) < distance(sample, x_train[center_indices[nearest_label]]):
            nearest_label = label
    cluster_indices[nearest_label].append(i)
```

Computing the new center

```python
flag = False
for i in range(K):
    pos_mean = np.mean(x_train[cluster_indices[i]], axis=0)
    nearest_index = 0
    for index in range(len(x_train)):
        if distance(pos_mean, x_train[index]) < distance(pos_mean, x_train[nearest_index]):
            nearest_index = index
    if center_indices[i] != nearest_index:
        flag = True
    center_indices[i] = nearest_index
```

Result:

![](result.png)