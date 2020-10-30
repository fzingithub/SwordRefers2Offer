# line = "食品(neg)药品50万(pos)限制"
# import re
# text_list = re.split("\(pos\)|\(neg\)", line)
# print(text_list)

# lamb = lambda x,y,z: (x+8)*y-z
# print(lamb(3,9,2))
import sys

def solve(filename:str):

    '''
    核心点一： python 大文件读取使用 对可迭代对象 f，进行迭代遍历：for line in f，
    会自动地使用缓冲IO（buffered IO）以及内存管理，而不必担心任何大文件的问题。
    '''

    with open(filename, 'rb+') as f:
        base = 0
        for line in f:
            words = line.split()
            length = sys.getsizeof(words)
            f.seek(base,0)
            base += length
            s = ' '.join(sorted(words))
            f.write(s)

solve('foo.txt')

