from series import fibonnaci, lucas, sum_series


def test_fib_one():
  expected = 1
  actual = fibonnaci(1)
  assert actual == expected

def test_fib_two():
  expected = 1
  actual = fibonnaci(2)
  assert actual == expected

def test_fib_three():
  expected = 2
  actual = fibonnaci(3)
  assert actual == expected

def test_fib_six():
  expected = 8
  actual = fibonnaci(6)
  assert actual == expected

def test_lucas_one():
  expected = 2
  actual = lucas(0)
  assert actual == expected

def test_lucas_two():
  expected = 1
  actual = lucas(1)
  assert actual == expected

def test_lucas_four():
  expected = 7
  actual = lucas(4)
  assert actual == expected

def test_sum_one():
  expected = 1
  actual = sum_series(1)
  assert actual == expected

def test_sum_two():
  expected = 13
  actual = sum_series(7)
  assert actual == expected

def test_sum_three():
  expected = 36
  actual = sum_series(6,4,2)
  assert actual == expected

def test_sum_four():
  expected = 78
  actual = sum_series(6,6,6)
  assert actual == expected

def test_sum_five():
  expected = 966
  actual = sum_series(11,3,9)
  assert actual == expected