def selectionSort(array):

  for i in range(0, len(array)-1):
    
    # i is a barrier that will leave only smallest 
    # integers behid once it moves to the right
    index = i

    # here we are trying to find smallest number 
    # on the right side from i to move it behind i to the left 
    for j in range(i+1, len(array)):

    #index is constantly looking for smaller number than i within this for loop

      if array[j] < array[index]:
        index = j

    # if index == i -> i is smallest number 
    # and no need to swap
    if not index == i:
      temp = array[index]
      array[index] = array[i]
      array[i] = temp

  return array


array = [2,654,3,45,3,234,76,45,23]

print(selectionSort(array))