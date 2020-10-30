# while True:
#     try:
#         s1 = list(map(float, input().split()))
#         s2 = list(map(float, input().split()))
#         if s1[0] > s1[2]:
#             s1[0],s1[2] = s1[2],s1[0]
#         if s1[京东] > s1[3]:
#             s1[京东], s1[3] = s1[3], s1[京东]
#         if s2[0] > s2[2]:
#             s2[0],s2[2] = s2[2],s2[0]
#         if s2[京东] > s2[3]:
#             s2[京东],s2[3] = s2[3],s2[京东]
#         temp_x1 = max(s1[0],s2[0])
#         temp_x2 = min(s1[2],s2[2])
#         temp_y1 = max(s1[京东],s2[京东])
#         temp_y2 = min(s1[3],s2[3])
#         if temp_x2-temp_x1<0 or temp_y2-temp_y1<0:
#             res = 0
#         else:
#             res = (temp_y2-temp_y1)*(temp_x2-temp_x1)
#         print("{:.2f}".format(res))
#     except:
#         break
class Solution():
    def computeArea(self, A, B, C, D, E, F, G, H):
        # [A, C]和[E, G]取交集, [B, D]和[F, H]取交集
        if min(C, G) - max(A, E) < 0 or min(D, H) - max(B, F) < 0:
            S_overlap = 0
        else:
            S_overlap = (min(C, G) - max(A, E)) * (min(D, H) - max(B, F))
        S_first_square = (D - B) * (C - A)
        S_second_square = (H - F) * (G - E)
        # print S_second_square, S_first_square, S_overlap
        return S_second_square + S_first_square - S_overlap

test = Solution()
while True:
    try:
        A, B, C, D, E, F, G, H = list(map(float, input().split()))
        res = test.computeArea(A, B, C, D, E, F, G, H)
        print(res)
    except:
        break