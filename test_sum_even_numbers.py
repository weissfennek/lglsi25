import pytest
from sum_even_numbers import sum_even_numbers

def test_sum_even_numbers():
    
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12  
    
    
    assert sum_even_numbers([2, 4, 6, 8]) == 20  
    
    
    assert sum_even_numbers([1, 3, 5, 7]) == 0  
    
    
    assert sum_even_numbers([]) == 0  
    
    
    assert sum_even_numbers([10]) == 10  
    
    
    assert sum_even_numbers([9]) == 0  
   
    assert sum_even_numbers([-2, -4, -6]) == -12  # -2 + -4 + -6 = -12