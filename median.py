def median(sequence):
    print sequence
    sequence.sort()
    length = len(sequence)
    print sequence

    if length % 2 == 0:
        median_num = len(sequence) / 2
        median_num2 = median_num - 1
        return (sequence[median_num] + sequence[median_num2]) / 2.0
    else:
        return sequence[len(sequence) / 2]

print median([5, 2, 3, 1, 4])
print median([10 ,99 ,103 ,4 , 6, 78])
print median([10 ,2 ,43 ,23 , 6, 78])
print median([4, 5, 5, 4])
