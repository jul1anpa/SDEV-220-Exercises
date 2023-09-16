'''
Sorting Arrays
Created by Julian Payne
This program defines a class that accepts an array(arr) and array size(n)
as attributes. It then sorts the given array in ascending order using the 
sorted function and returns it as output. In this case, the class is being
instantiated with the array [0,1,0,2,1] and an array size of 5.
'''

class Solution:

    def __init__(self, arr, n):
        self.n = n
        self.arr = sorted(arr)

    def __str__(self):
        return f"{self.arr}"
        


def main():
    array = Solution([0,1,0,2,1], 5)
    print(array)

if __name__ == '__main__':
    main()