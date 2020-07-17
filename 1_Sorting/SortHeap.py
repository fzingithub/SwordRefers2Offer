
import numpy as np
import time

class Sort():
    def heap_sort(self, data):    # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行对调整过程。
        heap = self.build_max_heap(data)
        for i in range(len(heap)-1,-1,-1):   #  从后往前倒着取
            heap[0], heap[i] = heap[i], heap[0]
            self.max_heapify(heap, i, 0)
        return heap    # 此时数据已排序好， 这里的 heap 不代表堆

    def build_max_heap(self, data):
        heap_size = len(data)
        for i in range((heap_size - 2)//2, -1, -1):   # 从第一个非叶节点进行比较
            self.max_heapify(data, heap_size, i)
        return data    # 堆已建好

    def max_heapify(self, data, heap_size, root):   # 在堆中做结构调整使得父节点的值大于子节点
        '''

        :param data: 待排序的堆。
        :param heap_size: 堆中的元素数目  但是数组下标 小于 heap_size 值。
        :param root:  堆顶元素下标
        :return:  原地建堆 返回值为 None
        '''
        left = 2 * root +1
        right = left + 1
        larger = root
        if left < heap_size and data[larger] < data[left]:
            larger = left
        if right < heap_size and data[larger] < data[right]:
            larger = right
        if larger != root:   # 如果做了堆调整则larger的值等于左节点或者右节点的，这个时候做对调值操作
            data[larger], data[root] = data[root], data[larger]
            self.max_heapify(data, heap_size, larger)


if __name__ == '__main__':
    randomNum = np.random.randint(0, 100000, size=10000)

    test = Sort()
    start = time.time()
    res = test.heap_sort(randomNum)
    end = time.time()

    print('time', end-start)
    print(res)