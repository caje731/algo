""" In-place implementation of the merge-sort algorithm """

def merge(the_list, start, mid, end):
    """
    Merge two sorted segments of the_list

    Indices for Segment A -> start to mid
    Indices for Segment B -> mid+1 to end
        where end < length(the_list)

    """
    start_a = start
    start_b = mid
    
    print 'merging -> ', the_list[start_a:mid], the_list[start_b:end]
    
    while the_list[start_a:mid] and the_list[start_b:end]:
        if the_list[start_b] < the_list[start_a]:
            # The first element of segment B needs to be placed before
            # all elements of the current segment A
            temp = the_list[start_b]
            the_list[start_a+1:start_b+1] = the_list[start_a:start_b]
            the_list[start_a] = temp

            # Everything moved up by one - first elements from both
            # segments are in their place
            start_a = start_a + 1
            start_b = start_b + 1
            mid = mid + 1
        
        else:
            # Since the first element of segment A is already in it's place
            # shorten the segment for the next iteration
            start_a = start_a + 1

    print 'merged -> ', the_list[start:end]

def merge_sort(the_list, start=0, end=None):
    """ Sort a list by the Merge Sort algorithm """

    if end is None:
        end = len(the_list)

    # if the list is already sorted, do nothing
    if len(the_list[start:end]) <= 1:
        return
    
    # Break the list down the middle
    midpoint = (start + end) / 2
    
    print 'broken up -> ', the_list[start:midpoint], the_list[midpoint:end]

    # Sort both parts individually
    merge_sort(the_list, start, midpoint)
    merge_sort(the_list, midpoint, end)

    # Both segments have been sorted, merge them
    merge(the_list, start, midpoint, end)

if __name__ == '__main__':
    my_list = [8,7,6,5,3,2,-1]
    merge_sort(my_list)
    print my_list

    my_list = [2,3,4,1,2,3,4,5,1,3,4,5,6]
    merge_sort(my_list)
    print my_list

