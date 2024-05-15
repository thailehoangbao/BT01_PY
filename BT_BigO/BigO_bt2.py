# Xác định độ phức tạp thời gian chạy (Big O notation) của một đoạn code dưới đây.
i = 0         # N = 1
while i < n:  # N = N/100
    i+= 100   # N = N/100

# F(N) = 1 + N/100 + N/100
# Độ phức tạp thời gian chạy của đoạn code trên là O(N)