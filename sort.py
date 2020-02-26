def validate_data(self, vals, dataType, dataPlace):
    """initialize given information and check for errors
    
    Arguments:
        vals {list} -- list of information to be sorted
        dataType {str} -- type of data in vals; n for numbers, s for sets of information
        dataPlace {int} -- location of metadata if sequence mode entered
    
    Raises:
        TypeError: If data-type in vals completely unrecognized
        TypeError: If data-type in vals not a valid number type when in number mode
        TypeError: If data-type in vals not a valid set type when in sequence mode
        IndexError: If passed location of metadata does not exist
        TypeError: If metadata type not a valid number type
        ValueError: If data-type mode not recognized
    
    Returns:
        list -- list of valid sortable data
    """
    for i in vals:
        if type(i) not in (int, float, list, tuple):
            raise TypeError('type of entered data not recognized')

    if dataType == 'n':
        for i in vals:
            if type(i) not in (int, float):
                raise TypeError(f'entered data-type(int, float) does not match type of entered data: {type(i)}')
        metaVals = [[v] for v in vals]
        return metaVals

    elif dataType == 's':
        for i in vals:
            if type(i) not in (list, tuple):
                raise TypeError(f'entered data-type(list, tuple) does not match type of entered data: {type(i)}')
            if len(i) < dataPlace:
                raise IndexError('metadata location outside of metadata tags')
            if type(i[dataPlace]) not in (int, float):
                raise TypeError(f'specified metadata is of unknown type: {type(i[dataPlace])}')
        return vals

    else:
        raise TypeError(f'dataType mode \'{dataType}\' not recognized')


def encode(vals, dataType):
    """Reformat list to be used more conventionally.
    
    Arguments:
        vals {list} -- list of unformatted, sorted values
        dataType {str} -- formatting type of items in vals
    
    Raises:
        Exception: If errors are not caught during validate_data
    
    Returns:
        list -- correctly formatted list
    """
    if dataType == 'n':
        return [i for l in vals for i in l]
    if dataType == 's':
        return vals
    raise Exception('Unexpected Exception occured')



class BubbleSort():
    def ascending(self, vals, dataType='n', dataPlace=0):
        """Sort given items 'vals' in acending order.
        
        Arguments:
            vals {list} -- list of data to be sorted
        
        Keyword Arguments:
            dataType {str} -- data-type of items in vals (default: {'n'})
            dataPlace {int} -- location of metadata if present(default: {0})
        
        Returns:
            list -- list of sorted data
        """
        # error testing
        vals = validate_data(vals, dataType, dataPlace)

        # sorting algorithm
        ns = len(vals)
        while ns > 0:
            try:
                for i in range(len(vals)):
                    if vals[i][dataPlace] > vals[i+1][dataPlace]:
                        vals[i], vals[i+1] = vals[i+1], vals[i]
            except IndexError:
                ns -= 1
        return encode(vals, dataType)
        

    def descending(self, vals, dataType='n', dataPlace=0):
        """Sort given items 'vals' in descending order.
        
        Arguments:
            vals {list} -- list of data to be sorted
        
        Keyword Arguments:
            dataType {str} -- data-type of items in vals (default: {'n'})
            dataPlace {int} -- location of metadata if present(default: {0})
        
        Raises:
            Exception: If somehow the error testing up top didnt work
        
        Returns:
            list -- list of sorted data
        """
        # error testing
        vals = self._validate_data(vals, dataType, dataPlace)

        # sorting algorithm
        ns = len(vals)
        while ns > 0:
            try:
                for i in range(len(vals)):
                    if vals[i][dataPlace] < vals[i+1][dataPlace]:
                        vals[i], vals[i+1] = vals[i+1], vals[i]
            except IndexError:
                ns -= 1
        return encode(vals, dataType)


def merge(vals):
    pass

def insertion(vals):
    pass

def quick(vals):
    pass

def shell(vals):
    pass


if __name__ == '__main__':
    unsorted1 = [(6, 3), (2, 5), (5, 2), (1, 1), (1, 4), (4, 0)]
    unsorted2 = [6, 4, 2, 3, 1, 5, 0]

    bubble = BubbleSort()
    print(f'Bubble Sort:')
    print(bubble.ascending(unsorted2))
    print(bubble.descending(unsorted2))
    print(bubble.ascending(unsorted1, 's', 1))
    print(bubble.descending(unsorted1, 's', 1))

    insert = 
    print(f'Insertion Sort:')
    print(bubble.ascending(unsorted2))
    print(bubble.descending(unsorted2))
    print(bubble.ascending(unsorted1, 's', 1))
    print(bubble.descending(unsorted1, 's', 1))