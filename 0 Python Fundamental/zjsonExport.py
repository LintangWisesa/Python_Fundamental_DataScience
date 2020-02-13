import json

# with open('zjson.json','r') as x:
#     data = json.load(x)
# print(data)

class jsonku():
    def __init__(self, file):
        self.file = file
    def buka(self):
        with open(self.file) as x:
            return json.load(x)