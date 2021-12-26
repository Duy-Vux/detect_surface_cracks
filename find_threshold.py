#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 2 

Template File for find_threshold()

@author: *** Solution by CTC *** 
"""

# import
import numpy as np 

def find_threshold(concrete_image, num_points = 20):
    
    # Note: The step number corresponds to those in the 
    # algorithmic description 
    
    # Step 1. Compute the maximum and minimum 
    brightness_max = np.max(concrete_image)
    brightness_min = np.min(concrete_image)
    
    # Step 2: Array of potential thresholds
    potential_threshold_list = np.linspace(brightness_min,brightness_max,num_points)
    
    # Step 3: Calculate the cost 
    # Note: Boolean indexing and elementwise arithmetic operators
    #       are useful here
    cost_list = np.zeros((num_points,))
    for k in range(num_points):
        potential_threshold = potential_threshold_list[k]
        c0 = (brightness_min + potential_threshold)/2
        c1 = (brightness_max + potential_threshold)/2
        
        # Use Boolean indexing to find all points below threshold
        # Similarly, for all points >= threshold 
        cost_0 = np.sum((concrete_image[concrete_image <  potential_threshold] - c0)**2)
        cost_1 = np.sum((concrete_image[concrete_image >= potential_threshold] - c1)**2)
        cost_list[k] = cost_0 + cost_1
    
    # Step 4: argmin() is useful here    
    threshold_to_use = potential_threshold_list[np.argmin(cost_list)]
    
    return threshold_to_use
