import numpy as np
def linear_interpolate(x,x_list,y_list):
	for i in range(len(x_list)):
		if x > x_list[i] and x < x_list[i+1]:
			y = y_list[i] + ((y_list[i+1] - y_list[i])/(x_list[i+1] - x_list[i])) * (x - x_list[i])
	return float(y)

print('Output: ')
print('input x:',end=' ')
x = float(input())
y = linear_interpolate(x,[-1,0,1,3.5],[1,0,1,12.25])
print(y)