import argparse #docs: https://docs.python.org/3/library/argparse.html
import time #docs: https://docs.python.org/3/library/time.html
import random #docs: https://docs.python.org/3/library/random.html

#Importing the necessary sorting algorithms. They are identical to the ones in portfolio 3.
from quicksort import quicksort, partition
from mergesort import mergesort, merge
from selectionsort import selectionsort

####################
#   starter code   #
####################

# helper function for generating inputs
def inputGenerator(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(0, n-1))
    return lst

# define positional arguments
parser = argparse.ArgumentParser()
parser.add_argument('sizeMin', type=int, help="Minimum input size to test")
parser.add_argument('sizeIncr', type=int, help="Increment for input size")
parser.add_argument('sizeMax', type=int, help="Maximum input size to test")
parser.add_argument('numTrials', type=int, help="Number of trials for each input size")

# define optional arguments
parser.add_argument('--whichsorts', '-w',
                    nargs='+',
                    type=str,
                    help="One or more sorts to test. Default is to test all sorts."
                    )

# parse command line arguments based on definitions
args = parser.parse_args()

# uncomment the lines below for an example of how to access the parsed arguments
#   (comment them out again when you're ready to proceed)

print("parsing arguments from command line...")
print(f'args.sizeMin: {args.sizeMin}')
print(f'args.sizeIncr: {args.sizeIncr}')
print(f'args.sizeMax: {args.sizeMax}')
print(f'args.numTrials: {args.numTrials}')
print(f'args.whichsorts: {args.whichsorts}')


#############################
#   write your code below   #
#############################

#Simple timekeeper class to look after all of my values and calculate things.
class timekeeper:
    def __init__(self):
        #Names are pretty self-explanatory; start_times holds start times for trials, end_times holds
        #end times for trials, and results holds the results.
        self.start_times = []
        self.end_times = []
        self.results = []
    
    #Helper function to append a start/end pair to the timekeeper. Takes as input the sort function
    #itself as a string, the size of the input, the start time and the end time.
    def time_append(self, sort, size, start_value, end_value):
        self.start_times.append([sort, size, start_value])
        self.end_times.append([sort,size,end_value])

    #Another helper function that calculates the average time of a given sort at a particular size.
        
    #TODO: there's something fucky going on here that means the results are wack.
    def calc(self, sort, size):
        if len(self.start_times) == 0 or len(self.end_times) == 0:
            return
        times = []
        for i in range(0,len(self.start_times)-1):
            if self.start_times[i][0] == sort and self.start_times[i][1] == size:
                times.append(self.end_times[i][2]-self.start_times[i][2])
        average = sum(times)/len(times)
        return average

    #Helper function that cleans the start and end times.
    def clear(self):
        self.start_times = []
        self.end_times = []
        self.results = []
    
    #Additional helper function to append the result of a given sorting algorithm at a particular size.
    def results_append(self,sort,size,result):
        self.results.append([sort, size, result])
    
    #Prints the results in a pretty table.
    def print_results(self):
        if args.whichsorts == None:
            args.whichsorts = ['mergesort','quicksort','selectionsort']
        headers = ['N']
        for i in args.whichsorts:
            headers.append(i)
        quick_results = {}
        merge_results = {}
        selection_results = {}
        for i in self.results:
            if i[0] == 'quicksort':
                quick_results[i[1]] = i[2]
            elif i[0] == 'mergesort':
                merge_results[i[1]] = i[2]
            elif i[0] == 'selectionsort':
                selection_results[i[1]] = i[2]
            else:
                continue
        result_string = ""
        for i in headers:
            if i == 'N':
                result_string += i + "\t\t\t"
            else:
                result_string += i + "\t\t\t\t"
        result_string += "\n"
        current_size = self.results[0][1]
        result_string += str(current_size) + "\t\t\t"
        for i in self.results:
            if i[1] != current_size:
                current_size = i[1]
                result_string += "\n" + str(current_size) + "\t\t\t"
            result_string += str(i[2]) + "\t\t\t"
        print(result_string)   

#Runner takes as inputs the sort as a function, the sort as a string for the purposes of putting it
#into the timekeeper, the number of trials you want to run, the size you want to run, and a timekeeper.
#It then runs the input sort the number of times you request, appending each result to the timekeeper.
def runner(sort, sort_str, trials, size, timer):
    j = 0
    while j < trials:
        arr = inputGenerator(size)
        start = time.perf_counter()
        sort(arr)
        end = time.perf_counter()
        timer.time_append(sort_str,size,start,end)
        j += 1

def driver():
    timer = timekeeper()
    if args.whichsorts == None:
        args.whichsorts = ['mergesort','quicksort','selectionsort']
    else:
        quicksort(args.whichsorts)
    size = args.sizeMin
    while size <= args.sizeMax:
        for i in args.whichsorts:
            if i == 'mergesort':
                runner(mergesort,'mergesort',args.numTrials,size,timer)
                result = timer.calc('mergesort',size)
                timer.results_append('mergesort',size,result)
            elif i == 'quicksort':
                runner(quicksort,'quicksort',args.numTrials,size,timer)
                result = timer.calc('quicksort',size)
                timer.results_append('quicksort',size,result)
            elif i == 'selectionsort':
                runner(selectionsort,'selectionsort',args.numTrials,size,timer)
                result = timer.calc('selectionsort',size)
                timer.results_append('selectionsort',size,result)
            else:
                continue
        size += args.sizeIncr
    timer.print_results()
    
driver()
