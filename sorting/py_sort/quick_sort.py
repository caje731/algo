""" Implementation of the Quick Sort algorithm """


def quick_sort(the_list, start=0, end=None):
    """
    Sort a segment defined by the `start` and `end` indices of `the_list` 
    by the Quick Sort algorithm. 
    """

    if end is None:
        end = len(the_list) - 1

    # Base case: do nothing if the list has just one element / is empty
    if end <= start:
        return

    split_point = partition(the_list, start, end)

    quick_sort(the_list, start, split_point-1)
    quick_sort(the_list, split_point+1, end)

def partition(the_list, start, end):
    """
    Break the_list into two segments and return the split-point.

    This implementation makes use of the first value as the pivot.
    """
    # Choose an data-point for value-comparison (a.k.a. pivot)
    pivot = the_list[start]

    left_marker = start + 1
    right_marker = end
    
    done = False
    while not done:
        # Keep moving the left_marker rightwards until a value
        # greater than the pivot is met.
        while left_marker <= right_marker and the_list[left_marker] <= pivot:
            left_marker += 1

        # Keep moving the right_marker leftwards until a value
        # smaller than the pivot is met.
        while the_list[right_marker] >= pivot and right_marker >= left_marker:
            right_marker -= 1

        if right_marker < left_marker:
            # markers have crossed - iteration complete
            done = True
        else:
            # Swap the values at both markers
            temp = the_list[right_marker]
            the_list[right_marker] = the_list[left_marker]
            the_list[left_marker] = temp

    # The right_marker now points to the last element that's smaller than pivot.
    # All elements after the right_marker are greater than pivot.
    # We need to put the pivot value into it's rightful place.
    temp = the_list[right_marker]
    the_list[right_marker] = the_list[start]
    the_list[start] = temp

    # The right_marker now holds a value that's in the correct place.
    # So the_list is now split into two unsorted parts by the right_marker
    # Therefore, the split-point we're looking for is the right_marker

    return right_marker
    

if __name__ == '__main__':
    my_list = [8,7,6,5,3,2,-1]
    quick_sort(my_list)
    print my_list

    my_list = [2,3,4,1,2,3,4,5,1,3,4,5,6]
    quick_sort(my_list)
    print my_list