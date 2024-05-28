iphones = [
    {
        "price": 3000,
        "name": "iphone 12"
    },
    {
        "price": 2000,
        "name": "iphone 11"
    },
    {
        "price": 1000,
        "name": "iphone X"
    },
    {
        "price": 4000,
        "name": "iphone 8"
    },
    {
        "price": 300,
        "name": "iphone 7"
    }
]

# Lọc các mẫu iPhone có giá từ 3000 đến 5000
filtered_iphones = [iphone for iphone in iphones if 3000 <= iphone["price"] <= 5000]

# In ra danh sách các mẫu iPhone phù hợp
print("Danh Sách iPhones:")
for iphone in filtered_iphones:
    print(f"{iphone['name']} - Giá: {iphone['price']}")