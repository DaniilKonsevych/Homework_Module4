def get_cats_info(path):
    data_list =  []
    with open(path, "r") as cat_info:
        for line in cat_info:
            dictionar = {"id:" : "" , "name" : "" , "age" : ""}

            line = [el.strip(",") for el in cat_info.readlines()]

            i_d = line[0]
            name = line[1]
            age = line[2]

            dictionar["id:"].append(i_d)
            dictionar["name"].append(name)
            dictionar["age"].append(age)

            data_list.append(dictionar)

print(get_cats_info("cats_info.txt"))