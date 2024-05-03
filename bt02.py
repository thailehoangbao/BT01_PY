class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = []

    def dangKyKhoaHoc(self, khoaHoc):
        self.khoaHoc.append(khoaHoc)

    def hienThiKhoaHoc(self):
        if self.khoaHoc:
            print(f"Danh sách khóa học đã đăng ký của học viên {self.tenHV}:")
            for kh in self.khoaHoc:
                print(kh.tenKhoaHoc)
        else:
            print(f"Học viên {self.tenHV} chưa đăng ký khóa học nào.")
    def xoaKhoaHoc(self,maKhoaHoc):
        index = 0
        for kh in self.khoaHoc:
            if kh.maKhoaHoc == maKhoaHoc:
                self.khoaHoc.pop(index)
                print('Xóa thành công khóa học với' + maKhoaHoc)
                break
            index += 1


class KhoaHoc:
    def __init__(self, maKhoaHoc, tenKhoaHoc, hinhThuc, hocPhi):
        self.maKhoaHoc = maKhoaHoc
        self.tenKhoaHoc = tenKhoaHoc
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi

    def thongTinKhoaHoc(self):
        print(f" ----- Thông tin khóa học {self.tenKhoaHoc}: -----")
        print(f"+ Mã khóa học: {self.maKhoaHoc}")
        print(f"+ Hình thức: {self.hinhThuc}")
        print(f"+ Học phí: {self.hocPhi}")

# Tạo các đối tượng học viên
hocvien1 = HocVien("HV001", "Nguyễn Văn A", "01/01/2000")
hocvien2 = HocVien("HV002", "Trần Thị B", "15/05/2001")
hocvien3 = HocVien("HV003", "Lê Thanh C", "15/05/2002")

# Tạo các đối tượng khóa học
khoahoc1 = KhoaHoc("KH001", "Lập trình Python cơ bản", "Offline", 2000000)
khoahoc2 = KhoaHoc("KH002", "Machine Learning", "Online", 3000000)
khoahoc3 = KhoaHoc("KH003", "Lập trình Java cơ bản", "Offline", 1800000)
khoahoc4 = KhoaHoc("KH004", "Lập trình PHP nâng cao", "Online", 2500000)


# Thực hiện đăng ký khóa học cho học viên
hocvien1.dangKyKhoaHoc(khoahoc1)
hocvien1.dangKyKhoaHoc(khoahoc2)

hocvien2.dangKyKhoaHoc(khoahoc1)
hocvien2.dangKyKhoaHoc(khoahoc3)
hocvien2.dangKyKhoaHoc(khoahoc4)


# Hiển thị danh sách khóa học đã đăng ký của học viên
hocvien1.hienThiKhoaHoc()
hocvien2.hienThiKhoaHoc()
hocvien3.hienThiKhoaHoc()

# Hiển thị thông tin chi tiết về khóa học
khoahoc1.thongTinKhoaHoc()
khoahoc2.thongTinKhoaHoc()

hocvien2.hienThiKhoaHoc()
print('-------------')
hocvien2.xoaKhoaHoc("KH001")
print('-------------')
hocvien2.hienThiKhoaHoc()
