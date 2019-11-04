from datetime import datetime
def func1(s1, s2):
#your code begin
    _format = '%H:%M:%S'
    t1 = datetime.strptime(s1, _format)
    t2 = datetime.strptime(s2, _format)
    return int(abs((t1 - t2).total_seconds()))
#your code end
