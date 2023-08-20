def compare_dicts(dict1, dict2):
    common_keys = set(dict1) & set(dict2)
    for key in common_keys: 
        if dict1[key] == dict2[key]: 
            print(f"{key}: {dict1[key]} is present in both x and y")

x = {'key1': 1, 'key2': 1, 'key3': 2}
y = {'key1': 1, 'key2': 2}

compare_dicts(x, y)