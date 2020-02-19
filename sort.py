def insertion(vals, place=0, ordering='ascending'):
    """Insertion sort algorithm to sort integers or floating point numbers in ascending or decending order.
    
    Arguments:
        vals {list} -- list of numbers, lists, or tuples with numbers at specified index
    
    Keyword Arguments:
        place {int} -- index of metadata if present, leave blank for no metadata (default: {0})
        ordering {str} -- ordering pattern of digits, can be ascending or descending (default: {'ascending'})
    
    Raises:
        SyntaxError: if ordering specification is not recognized
        IndexError: if place value is out of range of metadata
        ValueError: if data to be sorted is not numbers
    
    Returns:
        list -- list sorted based on specifications
    """
    ns = len(vals)  # initialize unsorted digit counter
    # if no metadata attached, add metadata
    if place == 0:
        vals = [[v] for v in vals]
    if place > len(vals[0])-1:
        raise IndexError('Metadata placement out of range of metadata tags')
    for i in vals:
        if type(i[place]) != (int or float):
            raise ValueError('Sortable data must be integer or floating point')

    # while not sorted
    while ns != 0:
        # run though every digit
        for i in range(len(vals)):
            try:
                # if ordering ascending, and digit more than next digit, swap with next digit
                if ordering == 'ascending':
                    if vals[i][place] > vals[i+1][place]:
                        vals[i], vals[i+1] = vals[i+1], vals[i]
                # if ordering decending, and digit less than next digit, swap with next digit
                elif ordering == 'descending':
                    if vals[i][place] < vals[i+1][place]:
                        vals[i], vals[i+1] = vals[i+1], vals[i]
                # otherwise leave be and move on

                # if ordering type not recognized,
                else:
                    # kill it
                    raise SyntaxError(f'Ordering pattern not recognized')
            # if at the end of the list
            except IndexError:
                pass
        # after last digit, remove it from the unsorted digit counter
        ns -= 1
    return vals


def shaker(vals):
    pass

def bubble(vals):
    pass

def quick(vals):
    pass

def radix(vals):
    pass

def tim(vals):
    pass


unsorted = [(6, 3), (2, 5), (5, 2), (1, 1), (1, 4), (4, 0)]
srtd = insertion(unsorted, 1)
print(f'Insertion: {srtd}')