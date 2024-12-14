#!/usr/bin/env python3

from ipdb_debugging import plus_two

class TestIpdbDebugging:
    '''Tests for ipdb_debugging.py'''

    def test_adds_two(self):
        '''adds_two() adds 2 to the input arg and returns sum.'''
        assert plus_two(3) == 5
