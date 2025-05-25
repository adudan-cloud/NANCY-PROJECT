def countdown(n):
   # print countdown from n to 0
    for i in range(n,0, -1):
        print (i)



def clear_list(lst):
    #clear all elements in a list
    lst.clear()


def print_square(num):
    #print the square of a number
    print(f"the square of {num} is {num**2}")


def update_dict(d, key, value):
    #update a dictionary with a key-value pair
    d[key] = value
