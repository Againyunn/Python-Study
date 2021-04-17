import re

def get(expr):
    pat = re.compile(r'(?:(?<=[^\d\.])(?=\d)|(?=[^\d\.]))', re.MULTILINE)
    token_list = [x for x in re.sub(pat, ' ', expr).split(' ' ) if x]

    return token_list

expr=input()
print(get(expr))
