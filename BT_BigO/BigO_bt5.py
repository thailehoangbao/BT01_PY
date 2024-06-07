for a in range(0,n):        # N = N
    for b in range(a,n):    # N = N^2
        print("a")          # N = N^2
    for c in range(0,n):    # N = N^2
        for d in range(0,n):   # N = N^3
            print("a")         # N = N^3
# F(N) = N^2 + N^2 + N^2 + N^3
# kết luận độ phức tạp thời gian chạy của đoạn code trên là O(N^3)