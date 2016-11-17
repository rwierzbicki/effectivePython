

# here we want
# closure won't change found without nonlocal initialization of found
# python will only look outside the function if you tell it to

def sort_priority(values,group):
    found = False
    def helper(x):
        if x in group:
            nonlocal found
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}

sort_priority(numbers, group)
found = sort_priority(numbers,group)

print('Found: ', found)
print(numbers)
