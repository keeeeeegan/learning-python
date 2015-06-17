def remove_duplicates(alist):
    new_list = []
    for n in alist:
        if not (n in new_list):
            new_list.append(n)
    return new_list

print remove_duplicates([1,2,3,2,3,4,5,6,7])
