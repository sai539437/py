# function
def median(lst):
    x=len(lst)
    if x%2==0:
        middle_value=x/2
    else:
        middle_value=(x+1)/2
    print(middle_value)
      # list_name.sort()
    lst.sort()
    print(lst)
    print("middle_value of list is",lst[middle_value]-1)

        
        

# main program

lst = [1.4, 2.4, 3.5, 6.9, 7.3, 1.4]
median(lst)