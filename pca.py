from datascience import *
from scipy import stats
import numpy as np
from numpy import linalg as la

a = Table.read_table('pca_data.csv')

#calculating zero mean data

x_std = a.column('x')
y_std = a.column('y')
x_std-=np.mean(x_std)
y_std-=np.mean(y_std)
print("Zeromean x is: ",x_std)
print("Zero mean y is: ",y_std)

#calculating covariance matrix

covariance = np.cov(x_std, y_std)
print("Covariance matrix is: ",covariance)

#calculating eigen values and eigen vectors

eigen_values, eigen_vectors = la.eig(covariance)
print("Eigen values are: ",eigen_values)
print("Eigen vectors are: ",eigen_vectors)

#finding transpose of eigen vectors and zero mean data

transpose_ev = np.transpose(eigen_vectors)

temp = np.column_stack((x_std, y_std))
transpose_zm = np.transpose(temp)

#multiplication of transpose matrices

result = np.dot(transpose_ev, transpose_zm)
finalx = result[1]
finaly = result[0]
answer = Table().with_columns(['x', finalx, 'y', finaly])
print("\nFinal answer is: ")
print(answer)