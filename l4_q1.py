import numpy as np
def lagrange(x,x_list,y_list):
	x_arr = [[x**n for n in range(len(x_list))] for x in x_list]
	x_list = np.array(x_arr)
	y_list = np.array(y_list)
	x_ = np.array([x**n for n in range(len(x_list))])
	x_inv = np.linalg.inv(x_list)
	a = x_inv @ y_list
	ans = x_ @ a
	return float(ans)

print('Output: ')
print('input x:',end=' ')
x = float(input())
y = lagrange(x,[-1,0,1,3.5],[1,0,1,12.25])
print(y)