# defining function to find duplicates
def dup(str:list, n:int) -> int:
    i=0

    # iterating while loop over the list  till length n
    while (i < n):

        # check for duplicates over consecutive indexes
        # and removing them using pop function
        if (str[i] == str[i-1]):
            str.pop(i)

        else:
            i += 1

    print(f'List after removing duplicates is {str}')

# driver code 
if __name__  == "__main__":
    
    # inialising list as a variable 'string'
    string= [ ]
    length= int(input("Enter length of list: "))

    print("Enter elements in list: ")

    # for loop for taking elements of list as input
    for i in range(0, length):
        ele= int(input())
        # adding elements at the end of list
        string.append(ele)
    
    # sort the list in ascending order
    string.sort()
    print(f'List inputed by is {string}')
    
    # calling the function
    dup(string, length) 
