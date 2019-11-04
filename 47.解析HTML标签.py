import re
def func(s):
#your code begin
    pattern = '<(.*?)>(.*?)</\\1>'
    repl = '\\1:\\2'
    return re.sub(pattern, repl, s)
#your code end
