# Danh sách từ
arrChar = ["cat", "banana", "obama", "batman", "car", "cow","alibaba"]

# Nhập từ muốn kiếm
getChar = input("Nhập từ muốn kiếm: ")

# Danh sách kết quả
results = []
vitri = []

i = 0
# Duyệt qua từng phần tử trong danh sách arrChar
for word in arrChar:
    # Kiểm tra nếu từ bắt đầu bằng chuỗi ký tự nhập vào
    if word.startswith(getChar):
        # Thêm từ vào danh sách kết quả
        results.append(word)
        vitri.append(i)
    i+=1

# In kết quả
print("Kết quả: ", results)
print("Vị trí: ", vitri)
#Trie Cấu trúc
root = {
    "c": {
        "a" : {
            "r" :{
                "endWord": True
            },
            "t" : {
                "endWord": True
            },
            "endWord": False
        },
        "endWord": False
    },
    "d" : {
        "o": {
            "n": {
                "e" : {
                    "endWord": True
                },
                "endWord": False
            },
            "endWord": True
        },
        "endWord": False
    }
}
