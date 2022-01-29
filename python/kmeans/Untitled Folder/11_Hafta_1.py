import numpy as np
array=np.array([1,2,3,4,5,6,7,8,9])
#vektör 9x1
print(array.shape)
a=array.reshape(3,3)
print("Boyutu: ",a.ndim)
print("Size: ",a.size)

array2=np.array([ [1,2,3,4] , [5,6,7,8] ])
array3=np.zeros( (3,4) )
array4=np.ones( (5,5) )
array4[0,0]=10
array5=np.arange(10,50,5)
array6=np.linspace(10,50,15)
print(array6)
v1=np.array([1,2,3])
v2=np.array([4,5,6])
print(v1+v2)#üstte yer alan dizideki sayıları sırası ile toplayarak yeni br