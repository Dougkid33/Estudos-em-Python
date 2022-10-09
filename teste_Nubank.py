# Python3 program to find the cost
# to make a string Panagram
 
# Function to return the total cost
# required to make the string Pangram
def pangramCost(arr, string) :
     
    cost = 0
    occurred = [False] * 26
 
    # Mark all the alphabets that
    # occurred in the string
    for i in range(len(string)) :
        occurred[ord(string[i]) - ord('a')] = True
 
    # Calculate the total cost for
    # the missing alphabets
    for i in range(26) :
        if (not occurred[i]) :
            cost += arr[i]
 
    return cost
 
# Driver Code
if __name__ == "__main__" :
 
    arr = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,
            10, 11, 12, 13, 14, 15, 16,
            17, 18, 19, 20, 21, 22, 23,
            24, 25, 26 ]
    string = "abcd"
 
    print(pangramCost(arr, string))
 
# This code is contributed by Ryuga