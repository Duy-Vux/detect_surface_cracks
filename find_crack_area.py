#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 2 

Template File for find_crack_area()

@author: *** Solution by CTC *** 
"""

import numpy as np 

def find_crack_area(concrete_crack_bool):
    return np.sum(concrete_crack_bool)