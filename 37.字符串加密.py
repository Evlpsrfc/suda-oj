import re
def func(n, s):
#your code begin
    orda = lambda ch: ord('a') if ch.islower() else ord('A')
    def repl(match):
        c = match.group(0)
        if c.isdigit():
            return str(n * int(c))
        return chr(orda(c) + (ord(c) - orda(c) + n) % 26)
    return ''.join(re.sub('\d+|\w', repl, s))
#your code end
