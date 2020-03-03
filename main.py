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
d_point_1 = 7
d_point_2 = 3.0
d_point_3 = 4.5
d_point_4 = 1.2

col=['sepal_length','sepal_width','petal_length','petal_width','type']

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
    global dataset
    global pd_set
    pd_set = panda.read_csv(file_name, sep=',', header=None)
    dataset = panda.read_csv(file_name, sep=',').values
    print(dataset)

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
    for i in range(len(x) - 1):
        euclidean_distances.append(math.sqrt( (x[i][0] - d_point_1)**2 + (x[i][1] - d_point_2)**2 + (x[i][2] - d_point_3)**2 + (x[i][3] - d_point_4)**2 ))


if __name__ == "__main__":
    open_csv_file('iris.csv')
    #open_arff_file('iris.arff')
    calculate_euclidean_distance(dataset)
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
        print("Response")
        print(neighbors[x], response)
        if response in counts:
            counts[response] += 1
        else:
            counts[response] = 1
  
    print("Counts")
    print(counts)
    sortedVotes = sorted(counts.items(), key=operator.itemgetter(1), reverse=True)
    print("Sorted votes")
    print(sortedVotes[0][0], neighbors)


