class solution:
    def divisorGame(self, N):
        '''
        2, Ailis 胜
        3，Ailis 败
        4，Ailis 胜
        5，Ailis 败
        6，Ailis 胜

        N 为奇数的时候 Alice（先手）必败，NN 为偶数的时候 Alice 必胜。
        证明：
        N=1 和 N = 2 时结论成立。
        N>2 时，假设 N≤k 时该结论成立，则 N=k+1 时：
        如果 k 为偶数，则 k+1 为奇数，x 是 k+1 的因数，只可能是奇数，而奇数减去奇数等于偶数，且 k+1−x≤k，故轮到 Bob 的时候都是偶数。而根据我们的猜想假设 N≤k 的时候偶数的时候先手必胜，故此时无论 Alice 拿走什么，Bob 都会处于必胜态，所以 Alice 处于必败态。
        如果 k 为奇数，则 k+1 为偶数，x 可以是奇数也可以是偶数，若 Alice 减去一个奇数，那么 k+1−x 是一个小于等于 k 的奇数，此时 Bob 占有它，处于必败态，则 Alice 处于必胜态。
        综上所述，这个猜想是正确的。
        '''
        return not N%2