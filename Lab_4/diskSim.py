import sys
import random

MAX = 4999  # max cylinder number 

def c_look(initial, sequence):
    total_distance = 0
    initial = abs(initial)

    copy_sequence = sequence.copy()
    copy_sequence.append(initial)
    copy_sequence.sort()
    index_initial = copy_sequence.index(initial)

    total_distance += abs(copy_sequence[len(copy_sequence)-1] - initial) 
    print(total_distance)
    if copy_sequence[0] < initial:
        total_distance += abs(copy_sequence[len(copy_sequence)-1] - copy_sequence[0])
        print(total_distance)
        total_distance += abs(copy_sequence[index_initial - 1] - copy_sequence[0])
        print(total_distance)
    
    return total_distance

def look(initial, sequence):
    total_distance = 0
    copy_sequence = sequence.copy()
    copy_sequence.sort()
    

    # only goes to right direction
    if initial < 0:     # moving left 
        initial = abs(initial)
        total_distance += abs(initial - copy_sequence[0]) 
        print(total_distance)
        if copy_sequence[len(copy_sequence)-1] > initial: 
            total_distance += abs(copy_sequence[len(copy_sequence)-1] - copy_sequence[0])
            print(total_distance)
    else:   # moving right
        initial = abs(initial)
        total_distance += abs(copy_sequence[len(copy_sequence)-1] - initial) 
        if copy_sequence[0] < initial:
            total_distance += abs(copy_sequence[len(copy_sequence)-1] - copy_sequence[0])
    
    return total_distance

def c_scan(initial, sequence):
    total_distance = 0

    copy_sequence = sequence.copy()
    copy_sequence.append(initial)
    copy_sequence.sort()
    index_initial = copy_sequence.index(initial)
    initial = abs(initial)

    total_distance += abs(MAX - initial)   # only goes to right direction
    if copy_sequence[0] < initial:
        total_distance += MAX
        total_distance += abs(copy_sequence[index_initial - 1] - 0)
    
    return total_distance

def scan(initial, sequence):
    total_distance = 0
    copy_sequence = sequence.copy()
    copy_sequence.sort()

    if initial < 0:     # moving left 
        initial = abs(initial)
        total_distance += abs(initial - 0) 
        if copy_sequence[len(copy_sequence)-1] > initial: 
            total_distance += abs(copy_sequence[len(copy_sequence)-1] - 0)
    else:   # moving right
        initial = abs(initial)
        total_distance += abs(MAX - initial) 
        if copy_sequence[0] < initial:
            total_distance += abs(MAX - copy_sequence[0])
    
    return total_distance

# find the next element that is closest to previous starting with head
def sstf(initial, sequence):
    total_distance = 0
    current = initial
    copy_sequence = sorted(sequence)
    initial = abs(initial)

    while len(copy_sequence) > 0:   # delete elements of it as we calculate 
        min_element =  min(copy_sequence, key=lambda element: abs(current - element))
        copy_sequence.remove(min_element)
        total_distance += abs(min_element - current)    # calculate distance
        current = min_element
    
    return total_distance

# the order they come in that's the order they will be processed 
def fcfs(initial, sequence):
    total_distance = 0
    current = initial
    initial = abs(initial)

    for i in range(len(sequence)):
        total_distance += abs(sequence[i] - current)
        current = sequence[i]
    return total_distance

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python diskSim.py INITIAL_POSITION [ACCESS_SEQUENCE_FILE]")
        sys.exit(-1)
        
    # mandatory initial position 
    initial_position = int(sys.argv[1]) 
    if initial_position <= -MAX or initial_position >= MAX: 
        print("Error: Initial Position should be an integer between -4999 and 4999 inclusive.")
    
    # non-mandatory initial position
    access_sequence = None
    if len(sys.argv) == 3:
        access_sequence_file = sys.argv[2]
        access_sequence = []
        with open(access_sequence_file) as file:
            for line in file: 
                disk_value = int(line.strip())
                if disk_value <= MAX or disk_value >= 0: 
                    access_sequence.append(disk_value)
                else:
                     print("Error: Disk cylinder value be an integer between 0 and 4999 inclusive.")
    else:
        access_sequence = [random.randint(0, MAX) for i in range(100)]
    
    print(access_sequence) 

    print("FCFS", fcfs(initial_position, access_sequence))
    print("SSTF", sstf(initial_position, access_sequence))
    print("SCAN", scan(initial_position, access_sequence))
    print("C-SCAN", c_scan(initial_position, access_sequence))
    print("LOOK", look(initial_position, access_sequence))
    print("C-LOOK", c_look(initial_position, access_sequence))


    