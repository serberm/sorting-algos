def quickSort(array):

  if len(array) <= 1:
    return array

  pivot = array[len(array)//2]

  left = [x for x in array if x < pivot]
  mid = [x for x in array if x == pivot]
  right = [x for x in array if x > pivot]

  return quickSort(left) + mid + quickSort(right)



array = [2,654,3,45,3,234,76,45,23]

print(quickSort(array))