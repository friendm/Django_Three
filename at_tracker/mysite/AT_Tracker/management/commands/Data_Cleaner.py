def string_clean(x):
    x = str(x)
    x = x.translate(None,"(',')")
    return x
#this cleans the data in the string
#of extra modifiers
