import csv
import json
import os
import pandas as pd

df=pd.read_json('robertson.json')
print(df)
df.to_csv("robertson.csv")

# def flattenjson( b, delim ):
#     val = {}
#     for i in b.keys():
#         if isinstance( b[i], dict ):
#             get = flattenjson( b[i], delim )
#             for j in get.keys():
#                 val[ i + delim + j ] = get[j]
#         else:
#             val[i] = b[i]
#
#     return val
#
#
#
# indir = "C:\\Users\\Sarah Hackney\\Documents\\GitHub\\alienabductions\\Sentiment JSON"
# for root, dirs, filenames in os.walk(indir):
#     for f in filenames:
#
#         with open(indir+"\\"+str(f), "r", encoding="utf-8") as d:
#
#             flattenjson(d, "_")
#             input = map( lambda x: flattenjson( x ), input )
#
#             columns = map( lambda x: x.keys(), input )
#             columns = reduce( lambda x,y: x+y, columns )
#             columns = list( set( columns ) )
#
#             with open( sentiments, 'wb' ) as out_file:
#                 csv_w = csv.writer( out_file )
#                 csv_w.writerow( columns )
#
#                 for i_r in input:
#                     csv_w.writerow( map( lambda x: i_r.get( x, "" ), columns ) )
