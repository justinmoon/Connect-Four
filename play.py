class MyException(Exception):
    pass

def check_10(x):
	if x == 10: raise MyException('please enter non-ten number!')