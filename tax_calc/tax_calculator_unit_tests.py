import pytest
from .tax_calculator import calculate_tax

def test_calculate_tax_with_100_cents():
    assert calculate_tax(100) == 19

def test_calculate_tax_with_1_cents():
    assert calculate_tax(1) == 0

def test_calculate_tax_with_4_cents():
    assert calculate_tax(4) == 1

def test_calculate_tax_with_0_cents():
    assert calculate_tax(0) == 0

def test_calculate_tax_with_negativ_100_cents():
    assert calculate_tax(-100) == None