# n = 10
# def example():
#     n=20
#     print(n)
# print(n)
# example()


# example = lambda x,y: x+y
# print(example(2,4))
# def example2(x,y):
#     return x + y

# print(example2(2,4))


# def get_filter(a,filter=None):
#     if filter is None:
#         return a
#     res = []
#     for x in a:
#         if filter(x):
#             res.append(x)
#     return res
# res = get_filter(range(1,10), lambda x:x % 2 == 0)
# print(res)


# def example(n):
#     print(n)
#     return example(n+1)
# example(1)


# def factorila(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorila(n - 1)


# print(factorila(5))
def get_sum(n):
    if n < 99 and n > 1000:
        return "99 dan 999 gacha son kiriting"
    else:
        
