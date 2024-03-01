#Quick sort! Takes an array along with the lower and upper indicies within said array that need to be
#sorted. The first call will be the first and last indicies of the array, and after that quicksort recursively
#calls itself to sort its subarrays after a pivot element has been selected.
def quicksort(arr, low = None, high = None):
    if low == None or high == None:
        low = 0
        high = len(arr)-1
    if high <= low:
        return
    pivot = partition(arr, low, high)
    quicksort(arr, low, pivot-1)
    quicksort(arr, pivot+1, high)

#Partitions the passed array into two subarrays; everything greater than or equal to the pivot is placed
#to the pivot's right, while everything less than the pivot is maintained. The index of the pivot is
#then returned. 
def partition(arr, low, high):

    #Chooses the pivot as the last element of the array. Could realistically be any element of the array,
    #but I thought that choosing the last element was quick and easy.
    pivot = arr[high]
    i = high
    j = low

    #Scans through the elements in the partition.
    for k in range(low, high):

        #If an element is larger than the pivot, place it to the right of the pivot. Elements smaller
        #than the pivot are left untouched. Also updates the position of the pivot.
        if arr[j] >= pivot:
            i -= 1
            val = arr.pop(j)
            arr.insert(i+1, val)
        else:
            j += 1

    #Returns the index of the pivot.
    return i