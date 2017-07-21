# This NYC taxi data is avilable at kaggle

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

print("Training Samples: ", train.shape[0])
print("Testing Samples: ", test.shape[0])


# Let's look at the train data first
print("A view of the train dataframe")
print(train.head())
print("\nColumns in train dataset : ", train.columns)
print("Overall description of the train dataset")
print(train.info())


# Okay  we have an overview of the train dataset. Before exploring further, let's see if the id column has some overlap with the test ids or not
train_id = set(train['id'].values)
test_id = set(test['id'].values)
print("Number of unique id in train dataset : ", len(train_id))
print("Number of unique id in test dataset : ", len(test_id))
common_ids = train_id.intersection(test_id)
print("Number of common id in the train and test datasets : ", len(common_ids))



# Let's have a look at the traget variable(trip duration) first
target = train['trip_duration']
print("Longest trip duration {} or {} minutes: " .format(np.max(target.values), np.max(target.values)//60))
print("Smallest trip duration {} or {} minutes: ".format(np.min(target.values),np.min(target.values)//60))
print("Average trip duration : {} or {} minutes".format(np.mean(target.values), np.mean(target.values)//60))

#Visualization is always better 
f = plt.figure(figsize=(8,6))
plt.scatter(range(len(target)), np.sort(target.values), alpha=0.5)
plt.xlabel('Index')
plt.ylabel('Trip duration in seconds')
plt.show()