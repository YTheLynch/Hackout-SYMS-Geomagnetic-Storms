import requests
import csv
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://wdc.kugi.kyoto-u.ac.jp/dst_realtime/202310/dst2310.for.request'

    response = requests.get(url)

    lines = response.text.split('\n')

    data = [line.split() for line in lines if line]
    #print (data)

    df = pd.DataFrame(data)

    df = df.iloc[:-1]
    df = df.drop(df.columns[[0,1]], axis=1)
    df = df.drop(df.columns[24], axis=1)
    df.columns = ['hour' + str(i) for i in range(1, len(df.columns)+1)]
    print(df)

    # def dosaid(s):    
    #     with open(s, "r") as f:
    #         obj = csv.reader(f)
    #         rows = []
    #         for row in obj:
    #             rows.append(row)


    #     for i in range(1, len(rows)):
    #         rows[i][0] = i


    #     with open(s, "w", newline = "") as f:
    #         csvwriter = csv.writer(f)
    #         csvwriter.writerows(rows)

    df.to_csv('dst_values.csv', index=False)
    # dosaid('dst_values.csv')
    return render_template('source.html', output_message= "hello you work")

if __name__ == '__main__':
    app.run(debug=True)
