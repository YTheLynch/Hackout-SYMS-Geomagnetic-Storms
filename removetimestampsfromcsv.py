import csv

def dosaid(s):    
    with open(s, "r") as f:
        obj = csv.reader(f)
        rows = []
        for row in obj:
            rows.append(row)


    for i in range(1, len(rows)):
        rows[i][0] = i


    with open(s, "w", newline = "") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(rows)



# dosaid("dscovr_mag_1s.csv")
# dosaid("planetary_k_index_1m.csv")
# dosaid("rtsw_mag_1m.csv")
# dosaid("rtsw_wind_1m-vxvyvzgsegsm.csv")
# dosaid("rtsw_wind_1m.csv")

dosaid("kp_index_prediction_test1000.csv")