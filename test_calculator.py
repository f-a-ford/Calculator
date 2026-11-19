from calculator import add, subtract, multiply, divide, CircleArea

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_subtract():
	assert subtract(10, 2) == 8

def test_multiply(): # arrange = 5, 3; act = multiply(); assert = == 15
	assert multiply(5, 3) == 15

def test_multiply_zero():
	assert multiply(5, 0) == 0

def test_CircleArea():
	assert CircleArea(-4) == "Error"
