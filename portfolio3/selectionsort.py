#Selection sort! Scans through an array and at each element, scans the array again to see which of
#the unsorted elements is smallest. Then, swaps the current element with the minimum element and iterates
#the outer loop.
def selectionsort(arr):
    i = 0

    #Outer scan; loops through all the elements of the array.
    while i < len(arr):
        j = i

        #Assigns the 'min' value, as well as a pointer to its position in the array.
        min = arr[j]
        min_pos = j

        #Inner scan; loops through all the elements of the array to the right of the element that the
        #outer scan is currently on.
        while j < len(arr):

            #If a smaller element is located, update min and min_pos
            if arr[j] < min:
                min = arr[j]
                min_pos = j
            j += 1
        
        #After scanning through the whole array, swap the currently selected element and the minimum
        #element.
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
        i += 1
    return arr
