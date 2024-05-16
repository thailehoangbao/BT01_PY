# Danh sách từ
arrChar = ["car", "bat", "card", "man", "women", "bag"]

# Nhập từ muốn kiếm
getChar = input("Nhập từ muốn kiếm: ")

# Danh sách kết quả
results = []

# Duyệt qua từng phần tử trong danh sách arrChar
for word in arrChar:
    # Kiểm tra nếu từ bắt đầu bằng chuỗi ký tự nhập vào
    if word.startswith(getChar):
        # Thêm từ vào danh sách kết quả
        results.append(word)

# In kết quả
print("Kết quả:", results)

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
