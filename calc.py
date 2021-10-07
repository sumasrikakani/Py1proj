'''
The 'calc' library contains the 'add2' function that takes 2 values and adds them together.If either value
is a string (or both of them are) 'add2' ensures they are both strings, therby resulting in a concatenated result.
NOTE: If a value submitted t the 'add2' function is a float,it must be done so in qoutes (i.e as a string)
'''

#If 'value' is not an integer, convert it to a float and faling that, a string
def conv(value):
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

#The 'add2' function itsels
def add2(arg1,arg2):
    #convert arg1 and arg2 to their appropriate types
    arg1conv=conv(arg1)
    arg2conv=conv(arg2)
    #if either arg1 or arg2 is a string, ensure they're both strings
    if isinstance(arg1conv,str) or isinstance(arg2conv,str):
        arg1conv=str(arg1conv)
        arg2conv=str(arg2conv)
    return arg1conv+arg2conv