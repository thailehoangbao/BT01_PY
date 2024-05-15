while (i<n):            # N = N
    while (a<n):        # N = N^2
        while (b <n):   # N = N^3
            b=b+1;      # N = N^3
        a=a+1;          # N = N^2
    while c<n:          # N = N^2
        c=c+1;          # N = N^2
    i=i+100;            # N = N/100

# F(N) = N + N^2 + N^3 + N^3 + N^2 + N^2 + N/100
# Độ phức tạp thời gian chạy của đoạn code trên là O(N^3)