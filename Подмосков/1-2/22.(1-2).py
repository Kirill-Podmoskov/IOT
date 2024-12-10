melt = {"Ag2O": 160, "Al2O3": 2053, "O2": 218, "AsH3": 117, "B2O3": 450}

melting_points = [melt[oxide] for oxide in melt if "O" in oxide]

melting_points_str = " ".join(str(x) for x in melting_points)

print(melting_points_str) 