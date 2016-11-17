


def	safe_division_c(number,	divisor,*,ignore_overflow,ignore_zero_division=False):
    print(number+divisor)

safe_division_c(1,2, ignore_overflow=True)

#shit will work as long as your kwargs have a name by the time the function runs then it's fine

#in this case, ignore zero is given a value in the function assignment and ignore overflow
#is defined during the function call, but we don't use either of them because I'm a bad person
