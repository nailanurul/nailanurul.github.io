import json

data = {"nama":"Moza","umur":10}
json_str = json.dumps(data)
print(json_str)

python_obj = json.loads(json_str)
print(python_obj["nama"])

#biar bisa ngeimport jangan pake nama file yg sama
#json itu ibarat wadah sementara python itu peralatannya
