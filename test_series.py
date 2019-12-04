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
  actual = lucas(1)
  assert actual == expected

def test_lucas_two():
  expected = 1
  actual = lucas(2)
  assert actual == expected

def test_lucas_four():
  expected = 4
  actual = lucas(4)
  assert actual == expected

def test_sum_one():
  expected = 0
  actual = sum_series(1)
  assert actual == expected

def test_sum_two():
  expected = 8
  actual = sum_series(7)
  assert actual == expected

def test_sum_three():
  expected = 22
  actual = sum_series(6,4,2)
  assert actual == expected

def test_sum_three():
  expected = 597
  actual = sum_series(11,3,9)
  assert actual == expected

def test_sum_four():
  expected = 48
  actual = sum_series(6,6,6)
  assert actual == expected