#ohhhhhh yeahhhhhh

def bubbleSort(array):
  for i in range(0, len(array)-1):
    for j in range(0, len(array)-1-i):
      if array[j] > array[j+1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
  
  return array


array = [2,654,3,45,3,234,76,45,23]

print(bubbleSort(array))