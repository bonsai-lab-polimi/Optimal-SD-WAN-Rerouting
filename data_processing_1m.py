import pandas as pd
import numpy
from influxdb_client import InfluxDBClient



url="http://10.10.5.101:8086"
token="qMUeAlYWsvFj9yWmKFy4eh5_yLlXbqgj-8bdauCjg0d25UVbFsqW-cWYklQfJnk47izpidwnVmPL76JvTwAJFA=="
org="Poli"
bucket= "Poli"


client = InfluxDBClient(url=url, token=token, org=org)



query ="""from(bucket:"Poli")
  |> range(start: -3m, stop: now())
  |> filter(fn: (r) => r["url"] == "10.0.0.4" or r["url"] == "10.0.0.5" or r["url"] == "10.0.0.6" or r["url"] == "10.0.0.7")
  |> filter(fn: (r) => r["_field"] == "average_response_ms")
  |> filter(fn: (r) => r["_measurement"] == "ping")
  |> filter(fn: (r) => r["host"] == "bonsai207")
  |> aggregateWindow(every: 10s, fn: mean, createEmpty: false)
  |> yield(name: "mean") |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")"""


  
  
result = client.query_api().query_data_frame(org=org, query=query)
#print(result[0])
#result=pd.concat(result, ignore_index=True)
#print("----------------------------------")
result[0].to_csv('Tesi/out6.csv', index=False, columns=result[0].columns) 
