# def solution(id_list, report, k):
#     report = set(report) 
#     report = list(report)
#     banned_user=[]
#     result=[]
#     count=0
#     for i in id_list:
#         for j in report:
#             if j.endswith(i):
#                 count+=1
#         if count>=k:
#             banned_user.append(i)
#         count=0
#     for i in id_list:
#         for j in report:
#             for p in banned_user:
#                 if j.startswith(i) and j.endswith(p):
#                     count+=1
#         result.append(count)
#         count=0
#     return result
# 런타임에러 