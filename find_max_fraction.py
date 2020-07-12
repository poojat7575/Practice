def solution(X, Y):
    dict_fraction = dict()
    for i in range(len(X)):
       val = str(X[i] / Y[i])
       if val in dict_fraction.keys():
           dict_fraction[val] = dict_fraction[val] + 1
       else:
           dict_fraction[val] = 1
    return max(dict_fraction.values())
    
    
if __name__ == "__main__":
    print(solution([1, 2, 3, 1, 2], [2, 4, 6, 5, 10]))
