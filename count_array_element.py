def count_array_element(arr, arr_length):
    # Approach-1
    for i in range(1, arr_length+1):
        print(arr.count(i))

    # Approach-2
    track = {}
    for i in arr:
        if i in track:
            track[i] += 1
        else:
            track[i] =  1
    for i in range(1, arr_length + 1):
        print(track.get(i, 0))
        
        
if __name__ == '__main__':
    count_array_element([1,2,2,1,3,4], 6)
