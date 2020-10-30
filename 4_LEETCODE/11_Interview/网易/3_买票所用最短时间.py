class Solution:
    def minTime(self, m:int, a:list, b:list)->'str as 08:00:40 am':
        '''
        双路dp：
        W[i] 第i个人买票单独买 前i个人所用的最短时间
        M[i] 第i个人和前人一起买 前i个人所用的最短时间


        W[i] = min(M[i-京东], W[i-京东]) + a[i-京东]
        M[i] = W[i-京东]-a[i-2]+b[i-京东]


        res = min(W[-京东], M[-京东])
        '''

        def dpPro(m:int, a:list, b:list):
            if m<1:
                return 0

            W = [0] * (m+1)
            M = [0] * (m+1)
            W[1] = a[0]
            M[1] = a[0]

            for i in range(2, m+1):
                W[i] = min(M[i - 1], W[i - 1]) + a[i - 1]
                M[i] = W[i - 1] - a[i - 2] + b[i - 2]

            return min(W[-1], M[-1])

        def change(time):
            sec = time%60
            minute = time//60
            hour = minute//60
            minute = minute%60

            flag_pm = False
            if hour>4:
                flag_pm = True
                hour = hour+8-12
            else:
                hour = hour+8

            hour = '0'+str(hour) if hour<10 else str(hour)
            minute = '0' + str(minute) if minute < 10 else str(minute)
            sec = '0' + str(sec) if sec < 10 else str(sec)

            return hour+':'+minute+':'+sec+' pm' if flag_pm else hour+':'+minute+':'+sec+' am'

        sec = dpPro(m,a,b)
        time = change(sec)

        return time


if __name__ == '__main__':
    test = Solution()

    m = 2
    a = [25, 20]
    b = [40]

    res = test.minTime(m,a,b)

    print(res)
