from typing import List, Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame


def intersection(l1, l2):
    return len(set(l1).intersection(l2))


# original data set
original_data = np.arange(1000)
data = original_data[:]

# permuting the data
np.random.shuffle(data)
np.random.shuffle(original_data)

# creating 10 sets of size=100
data = np.reshape(data, (10, 100))
df: DataFrame = pd.DataFrame(original_data)

for i in range(0, 10):
    df.append(pd.DataFrame(data[i]))

# contains all values whose sampling is true
list_item: List[List[Any]] = [[], [], [], []]
ctr = [{}, {}, {}, {}]
sampling_type = [False, True]

# for sampling without and with replacement
for st in sampling_type:
    # for k = 1, 2, 3, 4
    for t in range(1, 5):
        # for every sample value from 0 to 999
        for k in range(0, 1000):
            # for each sample running 1000 times
            for j in range(0, 1000):
                d1: DataFrame = df.sample(j, replace=st)
                d = d1.values.tolist()
                d = np.array(d)
                d = d.ravel()
                d.tolist()
                if (intersection(d, data[0]) >= t and intersection(d, data[1]) >= t and intersection(d, data[
                    2]) >= t and intersection(d, data[2]) >= t and
                        intersection(d, data[3]) >= t and intersection(d, data[4]) >= t and intersection(d, data[
                            5]) >= t and intersection(d, data[6]) >= t and
                        intersection(d, data[7]) >= t and intersection(d, data[8]) >= t and intersection(d,
                                                                                                         data[9]) >= t):
                    list_item[t - 1].append(j)
                    break
        list_item[t - 1].sort()
        ctr[t - 1] = {x: list_item[t - 1].count(x) for x in list_item[t - 1]}
        x = []
        y = []

        for key, value in ctr[t - 1].items():
            x.append(key)
            y.append(value)
        y1 = y[:]
        for s in range(1, len(y)):
            y[s] = y[s] + y[s - 1]

        y = [m / 1000 for m in y]
        plt.plot(x, y)
        plt.xlabel('Sample Space')
        plt.ylabel('Probability')
        plt.title("Sampling %s , k=%d" % ('Without Replacement' if st == False else 'With Replacement', t))
        # probability graph generation
        plt.show()

        t2 = []
        t1 = []
        for l in range(0, 100, 10):
            t1.append("%d-%d" % (0 + l, 9 + l))

        for l in range(0, 10):
            t2.append(0)

        for p in range(0, len(x)):
            t2[int(x[p] / 10)] += y1[p]
        plt.bar(t1, t2)
        plt.xlabel('Range')
        plt.ylabel('frequency')
        plt.title("frequency vs Sample Size, k=%d Sampling %s" % (
            t, 'Without Replacement' if st == False else 'With Replacement'))
        plt.show()

print("#########Program Ended########")
