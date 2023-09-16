'''
Binary Search
Created by Julian Payne
This program defines a class that accepts an array(arr), array size(n),
and an integer(k) as attributes. It then uses a lambda function to determine
what the index of k is within the array. The program then prints this solution
as a string representation of the class object that was created. In this case,
the class is being instantiated with an array of [1,2,3,4,5], a size of 5, and
the integer 4. 
'''

class Solution:

    def __init__(self, arr, n, k):
        self.arr = arr
        self.n = n
        self.k = k
        self.find_index = lambda i: i.index(self.k)


    def __str__(self):
        return f'{self.find_index(self.arr)}'



def main():
    index = Solution([1,2,3,4,5], 5, 4)
    print(index)

if __name__ == '__main__':
    main()