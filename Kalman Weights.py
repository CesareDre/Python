# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:20:49 2020

@author: Joris Dreesen
"""


import matplotlib.pyplot as plt
weights = [158.0, 164.2, 160.3, 159.9, 162.1, 164.6, 169.6, 167.4, 166.4, 171.0, 171.2, 172.6]
time_step = 1.0 # day
scale_factor = 4.0/10
def predict_using_gain_guess(weight, gain_rate, do_print=False):
    # store the filtered results
    estimates, predictions = [weight], []
    
    for z in weights:
        prediction = weight + gain_rate * time_step
        
        #Update filter
        weight = prediction + scale_factor * (z - prediction)
        
        #Save
        estimates.append(weight)
        predictions.append(predictions)
        if do_print:
           print("estimates;",estimates, "Prediction:", prediction,"Prediction:", weight)

    return estimates, predictions

initial_guess = 160

estimates, predictions = predict_using_gain_guess(
weight=initial_guess, gain_rate=1, do_print=True)

            