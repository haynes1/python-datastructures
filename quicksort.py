def qs(arr):

  quickSort(arr,0,len(arr)-1)

def quickSort(arr,left,right):

    index = partition(arr, left, right)
    print "index: ", index
    print "partitioned: ", arr

    if left < index -1:
        quickSort(arr,left,index-1)
    if index < right:
        quickSort(arr,index + 1,right)


def partition(arr,first,last):

  pivotvalue = arr[first]
  left = first+1
  right = last

  while left <= right:
      while left <= right and arr[left] <= pivotvalue:
          left = left + 1

      while arr[right] >= pivotvalue and right >= left:
          right = right -1

      if left < right:
          temp = arr[left]
          arr[left] = arr[right]
          arr[right] = temp

  temp = arr[first]
  arr[first] = arr[right]
  arr[right] = temp

  return right

arr = [6,0,2,3,4,9,6]
print "original: ", arr
qs(arr)
print(arr)