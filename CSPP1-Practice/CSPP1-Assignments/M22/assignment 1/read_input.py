'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def main():
    '''main method'''
    val = int(input())
    for i in range(val):
        ans = input()
        print(ans)
        i += 1 #line written only to satisfy pylint, code has no effect
if __name__ == '__main__':
    main()
