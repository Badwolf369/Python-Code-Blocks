def bubble_sort(vals, place=0, pattern='ascending'):
    """Insertion sort algorithm to sort integers or floating point numbers in ascending or decending order.
    
    Arguments:
        vals {list} -- list of numbers, lists, or tuples with numbers at specified index
    
    Keyword Arguments:
        place {int} -- index of metadata if present, leave blank for no metadata (default: {0})
        pattern {str} -- ordering pattern of digits, can be ascending or descending (default: {'ascending'})
    
    Raises:
        SyntaxError: if ordering pattern is not recognized
        IndexError: if place value is out of range of metadata
        ValueError: if data to be sorted is not numbers
    
    Returns:
        list -- list sorted based on specifications
    """
    ns = len(vals)  # initialize unsorted digit counter
    # if no metadata attached, add metadata
    if place == 0:
        vals = [[v] for v in vals]
    # check for metadata errors
    if place > len(vals[0])-1:
        raise IndexError('Metadata placement out of range of metadata tags')
    for i in vals:
        if type(i[place]) != (int or float):
            raise ValueError('Sortable data must be integer or floating point')

    # while not sorted,
    while ns != 0:
        # run though every digit
        for i in range(len(vals)):
            try:
                # if pattern ascending, and current digit more than next digit, swap with next digit
                if pattern == 'ascending':
                    if vals[i][place] > vals[i+1][place]:
                        vals[i], vals[i+1] = vals[i+1], vals[i]
                # if pattern decending, and  current digit less than next digit, swap with next digit
                elif pattern == 'descending':
                    if vals[i][place] < vals[i+1][place]:
                        vals[i], vals[i+1] = vals[i+1], vals[i]
                # otherwise leave be and move on

                # if ordering pattern not recognized,
                else:
                    # raise an error
                    raise SyntaxError(f'Ordering pattern not recognized')

            # if at the end of the list
            except IndexError:
                pass
        # after last digit, remove it from the unsorted digit counter
        ns -= 1
    return vals


class BubbleSort():
    def _validate_data(self, vals, dataType, dataPlace):
        if dataType == 'n':
            for i in vals:
                if type(i) not in (int, float):
                    raise TypeError('data type does not match entered data')
            metaVals = [[v] for v in vals]
            return metaVals
        elif dataType == 's':
            for i in vals:
                if type(i) not in (list, tuple):
                    raise TypeError('data type does not match entered data')
            for i in vals:
                if len(i) < dataPlace:
                    raise IndexError('metadata location outside of metadata tags')
            return vals
        else:
            raise TypeError(f'dataType argument \'{dataType}\' not recognized')


    def ascending(self, vals, dataType='n', dataPlace=0):
        vals = self._validate_data(vals, dataType, dataPlace)

        ns = len(vals)
        while ns > 0:
            try:
                for i in range(len(vals)):
                    if vals[i] < vals[i+1]:
                        vals[i], vals[i+1] = vals[i+1], vals[i]
            except IndexError:
                ns -= 1
        return vals

    def descending(self, vals):
        ns = len(vals)
        while ns > 0:
            try:
                for i in range(len(vals)):
                    if vals[i] < vals[i+1]:
                        vals[i], vals[i+1] = vals[i+1], vals[i]
            except IndexError:
                ns -= 1
        return vals


def merge(vals):
    pass

def insertion(vals):
    pass

def quick(vals):
    pass

def shell(vals):
    pass


unsorted = [(6, 3), (2, 5), (5, 2), (1, 1), (1, 4), (4, 0)]
bubble = BubbleSort()
srtd = bubble.ascending(unsorted)
print(f'Bubble Sort: {srtd}')