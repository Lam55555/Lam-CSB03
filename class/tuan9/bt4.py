students_details = {
    "Alice": {"age": 20, "score": 85},
    "Bob": {"age": 22, "score": 92},
    "Charlie": {"age": 21, "score": 78},
    "David" : {"age": 22, "score": 92}
}

if "David" in students_details:
    print(students_details['David'])
else:
    print('David không có trong danh sách')

for i in students_details.values():
    a = sorted(i['score'])
    print(a)