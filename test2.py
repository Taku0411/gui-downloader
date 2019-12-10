from concurrent import futures

def ppp(a, k):
    print(a, k)

with futures.ThreadPoolExecutor() as exector:
    for i in range(5):
        k = i * 2
        exector.submit(ppp, i, k)
