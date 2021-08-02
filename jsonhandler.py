import json
import datetime

fx = {"EUR":1.192, "GBP":1.41}
al = {"EUR":0.782, "GBP":0.915}
metadata = {"size":826401, "date":"2021-08-02"}
data = {"root":[{"fx":fx,"al":al},{"metadata": metadata}]}
data_string = json.dumps(data)

load_data = json.loads(data_string)
test1 = load_data["root"][0]["fx"]

a = 1

