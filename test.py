class Map():
    def __init__(self, key):
        self.key = key
        self.load_map_keys()
        self.load_map_data()

    def load_map_keys(self):
        self.map_keys = {"\n" : "new_z_level"}
        f = open(f"data/keys.txt")
        key = ""
        value = ""
        value_done = False
        for i in f.read():
            if i != "\n":
                if i == ";":
                    self.map_keys[key] = value
                    value = ""
                    key = ""
                    value_done = False

                if value_done == True:
                    key += i

                if i == ":":
                    value_done = True

                if i != ":" and value_done == False and i != ";":
                    value += i                
            

    def load_map_data(self):
        self.map_data = []
        f = open(f"data/{self.key}.txt")
        temp_row = []
        temp_z_level = []
        for i in f.read():
            if self.map_keys[i] == "new_z_level":
                temp_z_level.append(temp_row)
                temp_row = []
            elif self.map_keys[i] == "new_y_level":
                self.map_data.append(temp_z_level)
            else:
                temp_row.append(self.map_keys[i])

    
    def build_from_map_data(self):
        self.blocks = []
        for y in map.map_data:
            for z in y:
                for x in z:
                    pass

map = Map("scene2")
print(map.map_keys)
for y in map.map_data:
    for z in y:
        for x in z:
            print(x, end = "")
        print()
    print()