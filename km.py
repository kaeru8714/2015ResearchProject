import numpy as np

def loadDataSet(file_name):
	dataMat = []
	target = open(file_name)
	for line in target.readlines():
		current_line = line.strip().split('\t')
		float_line = list(map(float, current_line))
		dataMat.append(float_line)
	return dataMat

def get_distance(vec_A, vec_B):
	return sqrt(sum(power(vec_A - vec_B, 2)))

def random_centroid(dataSet, k):
	n = np.shape(dataSet)[1] # 'dataSet' array의 행렬 개수
	centroids = np.mat(np.zeros((k, n))) # n*k행렬
	print centroids
	for j in range(int(n)):
		minJ = min(dataSet[:, j])
		rangeJ = float(max(dataSet[:, J]) - minJ)
		centroids[:, j] = minJ + rangeJ*random.rand(k, 1)
	return centroids


def testing(dataSet, k):
	n = dataSet.shape()

dat = mat(km.loadDataSet('testSet.txt'))
