# q2.py  — Temperature for CSVs (months as columns)

import os, csv, math # importing temp folder

MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"] # months 

def month_to_season(m):  # converting months to seasons 
    if m in (12, 1, 2):  # dec, jan, feb = summer
        return "Summer"
    if m in (3, 4, 5):
        return "Autumn"  # march , april, may = autumn
    if m in (6, 7, 8):
        return "Winter" # june, july, aug = winter 
    if m in (9,10,11):
        return "Spring" # sept , oct , nov = spring
    return None
def safe_float(x):
   # Try converting string x to a float.
    #Returns (ok, value):
      # ok=False if NaN or conversion fails
      # ok=True if conversion successful
    try:
        v = float(x)
        if math.isnan(v):
            return False, 0.0
        return True, v
    except:
        return False, 0.0

def stddev(values):
    
    #Compute the population standard deviation for a list of values.
    #Returns 0.0 if there are fewer than 2 values.
    
    n = len(values)
    if n < 2:
        return 0.0
    mean = sum(values) / n
    var = 0.0
    for v in values:
        diff = v - mean
        var += diff * diff
    var /= n  # population variance
    return math.sqrt(var)