
#Time Complexity -- O(2^n)
def subsets(array, subsets = [[]]):
    for el in array:
        Set = []
        for subset in subsets:
            temp = subset[:]
            temp.append(el)
            Set.append(temp)
        subsets.extend(Set)
    return subsets


#Time Complexity -- O(2^n)
def subsets_r(array, index, subsets, subset = []):
    if index == len(array):
        subsets.append(subset)
        return
    subsets_r(array, index + 1, subsets, subset + [array[index]])
    subsets_r(array, index + 1, subsets, subset)

