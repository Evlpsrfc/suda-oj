def func(s):
#your code begin
    if s.endswith('y'):
        return s[:-1] + 'ies'
    elif any(map(s.endswith, ['o', 'ch', 's', 'sh', 'x', 'z'])):
        return s + 'es'
    return s + 's'
#your code end
