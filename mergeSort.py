def mergeSort(array):
  if len(array) == 1:
    return

  middle = len(array)//2

  #divide arrays into left/right
  left = array[:middle]
  right = array[middle:]

  #keep dividing until 1 element left
  #and start performing merge 
  mergeSort(left)
  mergeSort(right)

  i = 0
  j = 0
  k = 0

  #conquer, start merging 
  while i < len(left) and j < len(right):

    #find which element between two sorted arrays (left and right) is smaller
    #insert it in merged array and go for next index that just had smaller element
    if left[i] < right[j]:
      array[k] = left[i]
      i += 1
    else:
      array[k] = right[j]
      j += 1

    k += 1

  #if left and right arrays are different size 
  #keep adding elements from remaining array
  #they are already sorted
  while i < len(left):
    array[k] = left[i]
    k += 1
    i += 1

  while j < len(right):
    array[k] = right[j]
    k += 1
    j += 1
  
  return array





array = [2,654,3,45,3,234,76,45,23]

print(mergeSort(array))
  
