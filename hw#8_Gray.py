import time
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
        return result
    return timed

def memoize(f):
    memo = {}
    # @timeit
    def helper(x,y):
        if x+y not in memo:            
            memo[x+y] = f(x,y)
        return memo[x+y]
    return helper



# @memoize
def lev(s,t):
	if s == "":
		return len(t)
	if t == "":
		return len(s)
	if s[-1]==t[-1]:
		cost = 0
	else:
		cost = 1
	result = min([lev(s[:-1], t) + 1, lev(s, t[:-1])+1, lev(s[:-1], t[:-1]) + cost])

	return result


ans = ""
while True:
	first = input("Please enter the first string: ")
	second = input("Please enter the second string: ")
    
	ts = time.time()
	l = lev(first,second)
	te = time.time()
	
	print('%2.2f ms' % ((te - ts) * 1000))
	print("There are {} operations required to convert \"{}\" to \"{}\"".format(l, first, second))