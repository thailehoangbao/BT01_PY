# S = 1 + 2 + 3 + 4 + ... + n

# def tingTong(n):  # 3

#     if n == 0:
#         return 0

#     return n + tingTong(n - 1)


# print(tingTong(3))

# n = 3
# f(3) = 3 + f(n-1) = 3 + 3 = 6
# f(2) = 2 + f(n-1) = 2 + 1 = 3
# f(1) = 1 + f(n-1) = 1 + 0 = 1
# f(0) = 0


# lstResult = [{"id": 1}, {"id": 2}, {"id": 3}, {"id": 4}, {"id": 5}]
# # [1,2,3] + [4,5,6] => [1,2,3,4,5,6]
# # extend()

def flatten_ids(lst):
    result = []
    for item in lst:
        result.append({"id": item["id"]})
        if item["value"]:
            result.extend(flatten_ids(item["value"]))
    return result

lstDemo = [
    {
        "id": 1,
        "value": [
            {
                "id": 2,
                "value": [
                    {
                        "id": 3,
                        "value": [
                            {
                                "id": 4,
                                "value": []
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": 5,
        "value": []
    }
]

lstResult = flatten_ids(lstDemo)
print(lstResult)