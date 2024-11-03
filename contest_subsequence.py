from math import comb

def main():
    temp = int(input())
    for _ in range(temp):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))

        if len(set(arr)) == 1:  
            num_combinations = comb(n, k)
            median = arr[0]
            final = num_combinations * median
        else:
            final = 0
            from itertools import combinations

            for subseq in combinations(arr, k):
                sorted_subseq = sorted(subseq)
                median_index = (k - 1) // 2
                median = sorted_subseq[median_index]
                final += median

        print(final)

if __name__ == "__main__":
    main()

