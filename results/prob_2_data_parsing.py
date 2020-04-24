import pandas as pd
import json

df = pd.read_csv("../data/data.csv")


df = df.rename(columns = {"Person Id":"person_id","Floor Access DateTime":"datetime","Floor Level":"floor_level","Building":"building"})

df['datetime']= pd.to_datetime(df['datetime'])
df['person_id'] = df['person_id'].astype(str)
df['datetime'] = df['datetime'].astype(str)



results = eval(df.to_json(orient="records"))


print("first floor event:")
print(results[0])

print("second floor event:")
print(results[1])

op_file_path = "../data/json_output_floor_event.json"
with open(op_file_path, "w") as write_file:
    json.dump(results, write_file)

print(f'the output json is stored in the location {op_file_path}')

