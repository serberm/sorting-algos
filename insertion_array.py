def insertionSort(array):

  for i in range(0,len(array)):

    j=i

    while j > 0 and array[j-1] > array[j]:
      temp = array[j]
      array[j] = array[j-1]
      array[j-1] = temp
      j -= 1

  return array



array = [2,654,3,45,3,234,76,45,23]

print(insertionSort(array))
