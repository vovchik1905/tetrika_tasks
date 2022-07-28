from typing import Any


def bin_search_zero(ones_and_zeros: list) -> Any:
    n = len(ones_and_zeros)
    left = -1
    right = n

    while right - left > 1:
        middle = (left + right) // 2

        if ones_and_zeros[middle] == 0:
            right = middle

        else:
            left = middle
    if right < n:
        return right
    else:
        return None

def main():
    arr = list(
        map(int, list(input("Please enter a sequence of ones and zeros: "))))
    first_zero_index = bin_search_zero(arr)
    if first_zero_index is not None:
        print(f"Index of the first zero: {first_zero_index}")
    else:
        print("The list does not contain zero.")


if __name__ == "__main__":
    main()
