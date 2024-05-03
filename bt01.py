# Hãy xây dựng một list sinh viên với các thuộc tính sau: mã sinh viên, tên sinh viên, điểm toán, điểm văn, điểm hóa.

# + Tạo list gồm 5 sinh viên

# + In thông tin các sinh viên có điểm trung bình lớn hơn 5

# + In ra các sinh viên có điểm hoá dưới 5
# Tạo danh sách sinh viên
students = [
    {"mã sinh viên": "SV001", "tên sinh viên": "Nguyễn Văn A", "điểm toán": 7.5, "điểm văn": 8.0, "điểm hóa": 6.5},
    {"mã sinh viên": "SV002", "tên sinh viên": "Trần Thị B", "điểm toán": 6.0, "điểm văn": 7.0, "điểm hóa": 5.5},
    {"mã sinh viên": "SV003", "tên sinh viên": "Phạm Văn C", "điểm toán": 8.0, "điểm văn": 6.5, "điểm hóa": 4.0},
    {"mã sinh viên": "SV004", "tên sinh viên": "Lê Thị D", "điểm toán": 5.5, "điểm văn": 4.5, "điểm hóa": 6.0},
    {"mã sinh viên": "SV005", "tên sinh viên": "Hoàng Văn E", "điểm toán": 4.0, "điểm văn": 6.0, "điểm hóa": 3.5}
]

# In thông tin sinh viên có điểm trung bình lớn hơn 5
print("Sinh viên có điểm trung bình lớn hơn 5:")
for student in students:
    diem_tb = (student["điểm toán"] + student["điểm văn"] + student["điểm hóa"]) / 3
    if diem_tb > 5:
        print("- Mã sinh viên:", student["mã sinh viên"])
        print("  Tên sinh viên:", student["tên sinh viên"])
        print("  Điểm trung bình:", diem_tb)

# In thông tin sinh viên có điểm hóa dưới 5
print("\nSinh viên có điểm hóa dưới 5:")
for student in students:
    if student["điểm hóa"] < 5:
        print("- Mã sinh viên:", student["mã sinh viên"])
        print("  Tên sinh viên:", student["tên sinh viên"])
        print("  Điểm hóa:", student["điểm hóa"])
