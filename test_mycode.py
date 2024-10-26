# test_mycode.py
from mycode import david_function


# Тесты для 1 задачки

def test_function_david():
    assert david_function(2) == 1
    assert david_function(10) == 1
    assert david_function(5) == 1
    assert david_function(7) == 1


#Тесты для 2 задачки



from mycode import max_money

def test_gorgona_max_money():
    assert max_money(3, [100, 200, 300], 100) == 350
    assert max_money(4, [500, 500, 500, 500], 0) == 1000
    assert max_money(5, [10**9, 10**9, 10**9, 10**9, 10**9], 10**9) == 3500000000
    assert max_money(2, [1, 1], 1) == 2
    assert max_money(3, [100, 200, 300], 0) == 300
