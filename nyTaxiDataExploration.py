import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


train = pd.read_csv('C:\Users\ppa3551\Documents\GitHub\NY Taxi data exploration\\train.csv')
test = pd.read_csv('C:\Users\ppa3551\Documents\GitHub\NY Taxi data exploration\\test.csv')

print "Training Samples: ", train.shape[0]
print "Testing Samples: ", test.shape[0]
