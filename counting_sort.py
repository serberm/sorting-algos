def countingSort(array):

  max_num = max(array)
  min_num = min(array)

  #creating empty array where indexes will represent nubers from given array
  #and elements will represent amount of same numbers occurrence
  count_array = [0] * (max_num - min_num+1)

  #will map number of occurrence of each number
  for element in array:
    count_array[element-min_num] += 1

  z = 0

  #will rewrite array by number of occurrence from count_array
  for index in range(0,len(count_array)):
    count = count_array[index]

    while count > 0:
      array[z] = index + min_num
      z += 1
      count -= 1

  return array

array = [2,654,3,45,3,234,76,45,23]

print(countingSort(array))

