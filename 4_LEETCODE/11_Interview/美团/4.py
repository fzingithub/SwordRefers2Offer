class UnionFindSet(object):
    def __init__(self, data_list):
        self.father_dict = {}
        self.size_dict = {}

        for node in data_list:
            self.father_dict[node] = node
            self.size_dict[node] = 1

    def find(self, node):
        father = self.father_dict[node]
        if(node != father):
            if father != self.father_dict[father]:
                self.size_dict[father] -= 1
            father = self.find(father)
        self.father_dict[node] = father
        return father

    def is_same_set(self, node_a, node_b):
        return self.find(node_a) == self.find(node_b)

    def union(self, node_a, node_b):
        if node_a is None or node_b is None:
            return

        a_head = self.find(node_a)
        b_head = self.find(node_b)

        if(a_head != b_head):
            a_set_size = self.size_dict[a_head]
            b_set_size = self.size_dict[b_head]
            if(a_set_size >= b_set_size):
                self.father_dict[b_head] = a_head
                self.size_dict[a_head] = a_set_size + b_set_size
            else:
                self.father_dict[a_head] = b_head
                self.size_dict[b_head] = a_set_size + b_set_size

if __name__ == '__main__':

    N, M = map(int,input().split())

    nums = []
    for _ in range(M):
        tempTwoNum = list(map(int, input().split()))
        nums.append(tempTwoNum)

    union_find_set = UnionFindSet(list(range(1, N+1)))
    # print(union_find_set.father_dict)
    for i in range(M):
        union_find_set.union(nums[i][0], nums[i][1])

    res_dict = {}
    for i in union_find_set.father_dict:
        rootNode = union_find_set.find(i)
        if rootNode in res_dict:
            res_dict[rootNode].append(i)
        else:
            res_dict[rootNode] = [i]

    print(len(res_dict.keys()))

    for i in res_dict:
        res = ' '.join(map(str, sorted(res_dict[i])))
        print(res)