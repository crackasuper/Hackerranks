#swapping cases from lower to upper and from upper to lowerr

def swap_case(s):
    return "".join([chr.lower() if chr.isupper() else chr.upper() for chr in s])
    

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
