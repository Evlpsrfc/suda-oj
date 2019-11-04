import string, re
def func(s):
#your code begin
    s = ' '.join(s.split())
    pattern = f'[{string.punctuation}](?=[a-zA-Z])'
    repl = '\g<0> '
    return re.sub(pattern, repl, s)
#your code end
