import json

# Dữ liệu từ điển
data_dict = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}

# Lưu dữ liệu từ điển vào tệp JSON
with open('data.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4) # indent=4: thụt lề 4 khoảng trắng
# Thông báo lưu thành công
print('Lưu thành công')