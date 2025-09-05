"""
Hit137: DAN_EXT40

Assignment 2: Ouestion 2

Program: O2.py

Auhors: Maharun Momo Islam, Moneya Islam, Andrew Morris, Kudzaishe Mutyasira


This program analyses Australian temperature data collected from mutliple
weather stations across multiple years. it processes all .csv files located in 
the 'temperatures' folder, ignores missing values (NaN) and computes:
- seasonal averages saved to 'average_temp.txt'
- largest temperature range saved to 'largest_temp_range_station.txt'
- temperature stability saved to 'temperature_stability_stations.txt'

"""

import os, csv, math  # Importing temp folder

MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]  # Months 

def main():
    station_to_values, month_to_values = load_temperatures("temperatures")

    write_season_averages(month_to_values, "average_temp.txt")
    write_largest_range(station_to_values, "largest_temp_range_station.txt")
    write_stability(station_to_values, "temperature_stability_stations.txt")


def month_to_season(m):  
          
    # Converting months to seasons 
          
    if m in (12, 1, 2):  # Dec, Jan, Feb = Summer
        return "Summer"
    if m in (3, 4, 5):
        return "Autumn"  # March , April, May = Autumn
    if m in (6, 7, 8):
        return "Winter"  # June, July, Aug = Winter 
    if m in (9,10,11):
        return "Spring"  # Sept , Oct , Nov = Spring
    return None


def safe_float(x):  # Try converting string x to a float
    try:
        v = float(x)
        if math.isnan(v):
            return False, 0.0
        return True, v
    except:
        return False, 0.0


def stddev(values):
    
    # Compute the population standard deviation for a list of values.
    # Returns 0.0 if there are fewer than 2 values.
    
    n = len(values)
    if n < 2:
        return 0.0
    mean = sum(values) / n
    var = 0.0
    for v in values:
        diff = v - mean
        var += diff * diff
    var /= n  # Population variance
    return math.sqrt(var)


def load_temperatures(folder="temperatures"):

    # Reads all csv files and collects values by station and by month. 
    
    station_to_values = {}
    month_to_values = {i+1: [] for i in range(12)}  

    STATION_KEY = "STATION_NAME"
  # Loop through each file in the folder

    for fname in os.listdir(folder):
        if not fname.lower().endswith(".csv"):
            continue
        path = os.path.join(folder, fname)
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if not reader.fieldnames:
                continue

            # Find month columns 
                  
            month_cols = [m for m in MONTHS if m in reader.fieldnames]
            if not month_cols:
                continue

            for row in reader:
                st = (row.get(STATION_KEY) or "UNKNOWN").strip() or "UNKNOWN"
                for m in month_cols:
                    ok, v = safe_float(row.get(m, ""))
                    if ok:
                        station_to_values.setdefault(st, []).append(v)
                        mi = MONTHS.index(m) + 1  
                        month_to_values[mi].append(v)

    return station_to_values, month_to_values

 # computes avg temp. writes results in txt file
def write_season_averages(month_to_values, out="average_temp.txt"):
    seasons = {"Summer": [], "Autumn": [], "Winter": [], "Spring": []}
       # Group values into seasons
    for m, vals in month_to_values.items():
        s = month_to_season(m)
        if s:
            seasons[s].extend(vals)
           # output file
    with open(out, "w", encoding="utf-8") as f:
        for s in ["Summer","Autumn","Winter","Spring"]:
            if seasons[s]:
                avg = sum(seasons[s]) / len(seasons[s])
                f.write(f"{s}: {avg:.1f}°C\n")
            else:
                f.write(f"{s}: n/a\n")

 # largest tenp range writes into txt file
def write_largest_range(station_to_values, out="largest_temp_range_station.txt"):
    best, max_range = [], -1.0
    meta = {}
    for st, vals in station_to_values.items():
        if not vals:
            continue
        r = max(vals) - min(vals)
        meta[st] = (r, max(vals), min(vals))
        if r > max_range:
            best, max_range = [st], r
        elif abs(r - max_range) < 1e-12:
            best.append(st)
    with open(out, "w", encoding="utf-8") as f:
        if not best:
            f.write("No data\n")
            return
        for st in sorted(best):
            r, mx, mn = meta[st]
            f.write(f"{st}: Range {r:.1f}°C (Max: {mx:.1f}°C, Min: {mn:.1f}°C)\n")

# computes standard deviation 
def write_stability(station_to_values, out="temperature_stability_stations.txt"):
    stds = {st: stddev(vals) for st, vals in station_to_values.items() if vals}
    if not stds:
        with open(out, "w", encoding="utf-8") as f:
            f.write("No data\n")
        return
    min_std = min(stds.values()); max_std = max(stds.values())
    #identifies for most stable
    most_stable   = [st for st, s in stds.items() if abs(s - min_std) < 1e-12]
    most_variable = [st for st, s in stds.items() if abs(s - max_std) < 1e-12]
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"Most Stable: {', '.join(sorted(most_stable))}: StdDev {min_std:.1f}°C\n")
        f.write(f"Most Variable: {', '.join(sorted(most_variable))}: StdDev {max_std:.1f}°C\n")


if __name__ == "__main__":
    main()
