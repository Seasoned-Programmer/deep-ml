import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	#matrix = np.asarray(matrix)

	det_matrix = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	trace_matrix = matrix[0][0] + matrix[1][1]
	#print(det_matrix)
	#print(trace_matrix)
	e1 =  trace_matrix + np.sqrt((trace_matrix*trace_matrix)-4*det_matrix)
	e1 =e1/2
	e2 =  trace_matrix - np.sqrt((trace_matrix*trace_matrix)-4*det_matrix)
	e2= e2/2

	#print(e1,e2)
	return [e1,e2]