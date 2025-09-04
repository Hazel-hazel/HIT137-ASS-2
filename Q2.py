# q2.py  — Temperature for CSVs (months as columns)

import os, csv, math # importing temp folder

MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"] # months 

def main():
    station_to_values, month_to_values = load_temperatures("temperatures")

    write_season_averages(month_to_values, "average_temp.txt")
    write_largest_range(station_to_values, "largest_temp_range_station.txt")
    write_stability(station_to_values, "temperature_stability_stations.txt")

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
def safe_float(x): # Try converting string x to a float.
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

def load_temperatures(folder="temperatures"):
# Reads all csv files and collects values by station and by month. 
    station_to_values = {}
    month_to_values = {i+1: [] for i in range(12)}  

    STATION_KEY = "STATION_NAME"

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

def write_season_averages(month_to_values, out="average_temp.txt"):
    seasons = {"Summer": [], "Autumn": [], "Winter": [], "Spring": []}
    for m, vals in month_to_values.items():
        s = month_to_season(m)
        if s:
            seasons[s].extend(vals)
    with open(out, "w", encoding="utf-8") as f:
        for s in ["Summer","Autumn","Winter","Spring"]:
            if seasons[s]:
                avg = sum(seasons[s]) / len(seasons[s])
                f.write(f"{s}: {avg:.1f}°C\n")
            else:
                f.write(f"{s}: n/a\n")

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

def write_stability(station_to_values, out="temperature_stability_stations.txt"):
    stds = {st: stddev(vals) for st, vals in station_to_values.items() if vals}
    if not stds:
        with open(out, "w", encoding="utf-8") as f:
            f.write("No data\n")
        return
    min_std = min(stds.values()); max_std = max(stds.values())
    most_stable   = [st for st, s in stds.items() if abs(s - min_std) < 1e-12]
    most_variable = [st for st, s in stds.items() if abs(s - max_std) < 1e-12]
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"Most Stable: {', '.join(sorted(most_stable))}: StdDev {min_std:.1f}°C\n")
        f.write(f"Most Variable: {', '.join(sorted(most_variable))}: StdDev {max_std:.1f}°C\n")

if __name__ == "__main__":
    main()
