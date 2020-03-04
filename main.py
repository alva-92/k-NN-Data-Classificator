import arff
import numpy as np
import pandas as panda
import math
import operator

k = None
number_of_attributes = None
dataset = None
euclidean_distances = []
pd_set = None
d_point_1 = 5.3
d_point_2 = 3.7
d_point_3 = 1.5
d_point_4 = 0.2

"""
This function opens and loads the data set provided as a arff file
"""
def open_arff_file(file_name):
    global dataset
    # read arff data
    with open(file_name) as f:
        # load reads the arff db as a dictionary with
        # the data as a list of lists at key "data"
        dataDictionary = arff.load(f)
        f.close()

    # extract data and convert to numpy array
    dataset = np.array(dataDictionary['data'])
    print(dataset.head())
    print("Columns ", dataset.columns)

"""
This function opens and loads the data set provided as a CSV file
"""
def open_csv_file(file_name):
    global pd_set
    pd_set = panda.read_csv(file_name, sep=',', header=None)
    print(pd_set)

"""
Calculates the euclidean distance between the provided data 
points and the existing data points.
"""
def calculate_euclidean_distance(x):
    global euclidean_distances
    global d_point_1
    global d_point_2
    global d_point_3
    global d_point_4

    for i in range(len(x) - 2):
        euclidean_distances.append(math.sqrt( (float(x[0][i+1]) - d_point_1)**2 + (float(x[1][i+1]) - d_point_2)**2 + (float(x[2][i+1]) - d_point_3)**2 + (float(x[3][i+1]) - d_point_4)**2 ))

if __name__ == "__main__":
    open_csv_file('iris.csv')
    #open_arff_file('iris.arff')
    calculate_euclidean_distance(pd_set)
    distances = {}
    for x in range(len(euclidean_distances)):
        distances[x] = euclidean_distances[x]

    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
    #by using it we store indices also
    sorted_d1 = sorted(distances.items())
    neighbors = []
    
    k=5
    # Extracting top k neighbors
    for x in range(k):
        neighbors.append(sorted_d[x][0])
    
    counts = {"Iris-setosa":0,"Iris-versicolor":0,"Iris-virginica":0}
    
    # Calculating the most freq class in the neighbors
    for x in range(len(neighbors)):
        response = pd_set.iloc[neighbors[x]][4]
        if response in counts:
            counts[response] += 1
        else:
            counts[response] = 1
  
    print("Total Counts")
    print(counts)
    sortedVotes = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    print("Results:")
    print("Identified as: " + sortedVotes[0][0], "\nClosest neighbors:", neighbors)


