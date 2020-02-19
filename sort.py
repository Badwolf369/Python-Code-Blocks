def insertion(vals, place, order='a'):
    """Insertion sort algorithm.
    
    Arguments:
        vals {list} -- unsorted list; must have sortable data attached to each item
        place {int} -- place of metadata to sort by in lists of that type
    
    Returns:
        list -- input list, reordered based on specifications
    """
    ns = len(vals)  # initialize unsorted digit counter
    # while not sorted
    while ns != 0:
        # run though every digit
        for i in range(len(vals)):
            
            # handle the index error at the end of each set of numbers
            try:
                # if ordering ascending
                if order == 'a':
                    # if digit greater than next digit
                    if vals[i] > vals[i+1]:
                        # swap with next digit
                        vals[i], vals[i+1] = vals[i+1], vals[i]
                    # otherwise leave be and move on
                # if ordering decending
                elif order == 'd':
                    # if digit less than next digit
                    if vals[i] < vals[i+1]:
                        # swap with next digit
                        vals[i], vals[i+1] = vals[i+1], vals[i]
                    # otherwise leave be and move on
                else:
                    raise SyntaxError(f'{order} is not recognized.')
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


unsorted = [6, 2, 5, 3, 1, 4, 0]
print(f'Insertion: {insertion(unsorted)}')