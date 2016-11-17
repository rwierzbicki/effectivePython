
#this is just a general exploration of keyword argument features

a = "test"

def kwarg(a, dont=False, **keywords):
    ##if keywords:
    print("there are this many **kwargs: ", len(keywords))
    
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

    if dont==True:
        return "sorry no dude"
    else:
        return a

    
def cheeseshop(kind_of_cake, *arguments, **keywords):
    print("-- Do you have any", kind_of_cake, "?")
    print("-- I'm sorry, we're all out of", kind_of_cake)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])   


test = kwarg("test", dont=False)
print(test)

print("-  -  - - - - now for a totally different test")

test = kwarg(a,dont=True, c="def", g="hij")
print(test)

cheeseshop("orange", "banana", "paul", john="cleese", paul="steve")
