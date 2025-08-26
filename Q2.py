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