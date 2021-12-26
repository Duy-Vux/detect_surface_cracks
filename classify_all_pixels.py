#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 2 

Template File for classify_all_pixels()

@author: *** Solution by CTC *** 
"""
# import 
import numpy as np 
import classify_a_pixel as classify_1

def classify_all_pixels(concrete_crack_bool):   
    image_pixel_status = np.zeros_like(concrete_crack_bool, dtype=int)
    
    for i in range(concrete_crack_bool.shape[0]):
        for j in range(concrete_crack_bool.shape[1]):   
            # Loop through all pixels
            image_pixel_status[i,j] = \
                  classify_1.classify_a_pixel(concrete_crack_bool,i,j)
     
    return image_pixel_status    