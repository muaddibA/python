def merge(*arrs):
    array = []
    for i in arrs:
        array += i
    for i in range(1, len(array)):
        current = array[i]
        before_current = i - 1
        while (before_current >= 0 and current 
< array[before_current]): 
            array[before_current + 1] = array[before_current]
            before_current -= 1
            array[before_current + 1] = current
    return array 