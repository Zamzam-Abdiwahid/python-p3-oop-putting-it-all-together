#!/usr/bin/env python3

from shoe import Shoe

import io
import sys

class TestShoe:
    '''Shoe in shoe.py'''

    def test_has_brand_and_size(self):
        '''has the brand and size passed to __init__, and values can be set to new instance.'''
        stan_smith = Shoe("Adidas", "Running", 9, "Black")
        assert(stan_smith.brand == "Adidas")
        assert(stan_smith.style == "Running")
        assert(stan_smith.size == 9)
        assert(stan_smith.color == "Black")

    def test_requires_int_size(self):'''prints "Size must be a positive number" if size is not an integer.'''
    captured_out = io.StringIO()
    sys.stdout = captured_out
    try:
        Shoe("Adidas", "Running", "not an integer", "Black")
    except ValueError as e:
        assert str(e) == "Size must be a positive number"
        
    def test_can_cobble(self):
        '''says that the shoe has been repaired.'''
        stan_smith = Shoe("Adidas", "Running", 9, "Black")
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.cobble()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Your shoe is as good as new!\n")
    
    def test_cobble_makes_new(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        stan_smith = Shoe("Adidas", "Running", 9, "Black")
        stan_smith.cobble()
        assert(stan_smith.condition == "New")