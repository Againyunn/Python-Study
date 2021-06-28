def downHeap(self,array, i, n):
    if n ==0:
        return None
        
    current = i
    value = array[i]
    while(2*current + 1 < n):
        largerChild = 2*current +1

        if(largerChild +1)< n and array[largerChild +1] > array[largerChild]:
            largerChild += 1
            
        if value < array[largerChild]:
            array[current] = array[largerChild]
            current = largerChild

        else:
            break
            
    array[current] = value

def makeHeap(self,array):
    n = len(array)
    for i in range(n//2 -1, -1, -1):
        downHeap(array, n, i)