x = [[1,2,3],[4,5,6]]
y=x.copy()
print('y= ',y)
x[0][1]=9
print('\n얕은 복사 후 원소 값 변경 결과: ')
print('x= ',x)
print('y= ',y)

import copy
print('\n-------------reset-------------')
x = [[1,2,3],[4,5,6]]
y = copy.deepcopy(x)
print('y= ',y)
x[0][1]=9
print('\n깊은 복사 후 원소 값 변경 결과: ')
print('x= ',x)
print('y= ',y)