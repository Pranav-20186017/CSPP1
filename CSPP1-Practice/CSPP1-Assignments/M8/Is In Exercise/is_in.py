def is_found(low_val, high_val, char, sorted_str):
    middle_val = (low_val + high_val) // 2
    if sorted_str[middle_val] == char:
        return True
    elif middle_val == low_val or middle_val == high_val:
        return False
    else:
        if sorted_str[middle_val] < char:
            return is_found(middle_val, high_val, char, sorted_str)
        elif sorted_str[middle_val] > char:
            return is_found(low_val, middle_val, char, sorted_str)
def isIn(char, aStr):
    sorted_str = sorted(aStr)
    sorted_str = ''.join(sorted_str)
    low_val = 0
    high_val = len(sorted_str)
    x = is_found(low_val, high_val, char, sorted_str)
    return x
def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))
if __name__ == "__main__":
    main()