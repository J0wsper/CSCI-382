#Merge sort! Takes an array with a lower and upper bound to sort. The function finds the midpoint of
#the subarray given by low and high and then recursively mergesorts the left and right subarrays. Once
#this has been completed, it then calls merge, a helper function that takes two sorted subarrays of
#arr, partitioned by low, mid and high, and then combines them in the correct order. 
def mergesort(arr, low, high):
    if low >= high:
        return
    
    #Finding the midpoint of the subarray.
    mid = (high+low)//2

    #Recursive calls
    mergesort(arr, low, mid)
    mergesort(arr, mid+1, high)

    #Merges the two sorted halves of the array into a sorted whole.
    merge(arr, low, mid, high)

#Function that takes an array that has been partitioned into two sorted subarrays and recombines them
#in sorted order.
def merge(arr, low, mid, high):
    left_arr = []
    right_arr = []

    #Creates the subarrays. I tried array slicing but I could not get it to work properly with the
    #indicies.
    for i in range(low, mid+1):
        left_arr.append(arr[i])
    for j in range(mid+1, high+1):
        right_arr.append(arr[j])
    i = 0
    j = 0
    k = low

    #Scans the subarrays to see which element at the front is smaller, then adds that to the main array.
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    #If either of the two subarrays is longer than the other, just append the remaining elements onto the
    #the end of the sorted array.
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
