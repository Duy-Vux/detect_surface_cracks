#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENGG1811 20T1 Assignment 2 

Template File for classify_a_pixel()

@author: *** Solution by CTC *** 
"""
import numpy as np 

def classify_a_pixel(concrete_crack_bool,i,j):
    
    # displacement needed to move to the neighbouring pixel
    disp_list = np.array([[-1, 0],
                          [ 0, 1],
                          [ 1, 0],
                          [ 0,-1]])
    
    # Classifying the pixel
    if concrete_crack_bool[i,j]: # It's in the crack
        # Check whether all the neighbouring pixels are in the crack too
        
        # Create a list to store whether the neighbours are in the crack
        # Only append the list if the neighbour exists
        # E.g. a corner pixel will only have 2 elements 
        neighbour_crack_status = [] # True if in crack, else False
        
        for k in range(len(disp_list)):
            neighbour_i = i + disp_list[k][0] # 0-coordinate of the neighbour
            neighbour_j = j + disp_list[k][1] # 1-coordinate of the neighbour
            if 0 <= neighbour_i < concrete_crack_bool.shape[0] and \
               0 <= neighbour_j < concrete_crack_bool.shape[1]:
                   neighbour_crack_status.append(concrete_crack_bool[neighbour_i,neighbour_j])
        
        # if all the elements in neighbour_crack_status are True,
        # then it is an interior (Type 2) pixel         
        if all(neighbour_crack_status):
            pixel_status = 2    # Interior
        else:    
            pixel_status = 1    # Perimeter 
    else:
        pixel_status = 0        # Not in the crack
        
    return pixel_status 
