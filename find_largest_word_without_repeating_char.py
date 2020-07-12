
 import itertools
 
 def solution(A):
    concat_length = 0
    all_combinations = []
    for r in range(len(A)+1):
        combinations = itertools.combinations(A, r)
        all_combinations.extend(list(combinations))

    for comb in all_combinations:
        if len(comb) >= 2:
            concat_str = "".join(comb)
            if len(concat_str) != len("".join(list(set(concat_str)))):
                continue
            if len(concat_str) > concat_length:
                concat_length = len(concat_str)
    return concat_length

if __name__ == "__main__":
    print(solution(["co", "dil", "ity", "abc", "pqr"]))
