---
layout: post
title:  "Cross Validation with scikit-learn"
subtitle: ""
date:   2020-01-15 00:00:00 -0600
categories: snippets
imgpath: ""
keywords: "python, cross-validation, scikit-learn, machine-learning"
code_folder: /assets/code/cross-validation
---


{% highlight python %}

import sklearn.datasets as datasets
from sklearn.model_selection import StratifiedKFold
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import numpy as np

RANDOM_SEED = 123

digits = datasets.load_digits()

X = digits.images.reshape((-1, 8*8))
y = digits.target

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_SEED)
train_val_index_list = [(train_i, val_i) for train_i, val_i in skf.split(X, y)]

models = []
fold_accuracy = []
for fold, indexes in enumerate(train_val_index_list, 1):
    print(f"Training fold {fold}")

    train_index, val_index = indexes

    X_train = X[train_index, :]
    y_train = y[train_index]
    X_val = X[val_index, :]
    y_val = y[val_index]

    model = MLPClassifier(random_state=RANDOM_SEED)
    model.fit(X_train, y_train)
    models.append(model)

    y_pred = model.predict(X_val)
    val_acc = accuracy_score(y_val, y_pred)

    print(f"val accuracy: {val_acc:4f}")

    fold_accuracy.append(val_acc)
    models.append(model)

print(f"Cross-validation accuracy: {np.mean(fold_accuracy):4f}")

{% endhighlight %}
