# q2.py  — Temperature analysis for wide CSVs (months as columns)

import os, csv, math

# ---- helpers ----
MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

def month_to_season(m):  # m = 1..12
    if m in (12, 1, 2):
        return "Summer"
    if m in (3, 4, 5):
        return "Autumn"
    if m in (6, 7, 8):
        return "Winter"
    if m in (9,10,11):
        return "Spring"
    return None