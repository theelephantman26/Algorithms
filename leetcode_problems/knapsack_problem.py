# def knapSack(N , s_list, n):
#     # Base Case
#     if n == 0 or N == 0 :
#         return 0
#
#     # If weight of the nth item is more than Knapsack of capacity
#     # W, then this item cannot be included in the optimal solution
#     if (s_list[n-1] > N):
#         return knapSack(N , s_list, n-1, True)
#
#     # return the maximum of two cases:
#     # (1) nth item included
#     # (2) not included
#     else:
#         return max(s_list[n-1] + knapSack(N-s_list[n-1] , s_list, n-1, True),
#                    knapSack(N , s_list, n-1, True))
#
# print(knapSack(457, [11, 23, 37, 48, 94, 152, 230, 312, 339, 413]))
n=10
dict_ = [[0]*n for i in range(n)]
dict_[1][1] = 'hello'
print(dict_)
