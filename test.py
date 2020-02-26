class insertionSort():
    def ascending(self, vals, dataType='n', dataPlace=0):
        ns = len(vals)
        while ns > 0:
            for i in range(len(vals)):
                x = i
                while x > 0:
                    if vals[x] < vals[x-1]:
                        vals[x], vals[x-1] = vals[x-1], vals[x]
                        x -= 1
                        print(vals)
                    else:
                        break
                ns -= 1
        return vals
                    
                

    def descending(self, vals, dataType='n', dataPlace=0):
        ns = len(vals)
        while ns > 0:
            for i in range(len(vals)):
                x = i
                while x > 0:
                    if vals[x] > vals[x-1]:
                        vals[x], vals[x-1] = vals[x-1], vals[x]
                        x -= 1
                        print(vals)
                    else:
                        break
                ns -= 1
        return vals

unsorted = [6, 5, 4, 3, 2, 1, 0]

insert = insertionSort()
print('Insertion sort:')
print(insert.ascending(unsorted))


