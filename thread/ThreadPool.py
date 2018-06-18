# author_li
# create time :2018/6/18
from concurrent.futures import ThreadPoolExecutor

def foo():
    print("hello")

def foo_1(name):
    print("hello %s"%name)

##############################################################
# 第一种用法
# 单一函数，无参
with ThreadPoolExecutor(max_workers=12) as e:
    k = 0
    while (k < 13):
        e.submit(foo)
        k += 1


#############################################################
# 第二种用法
# 单一函数，有不同参
arg = ['liyang','python','java','php','ruby','c++','golang']

with ThreadPoolExecutor(max_workers=12) as e:
    e.map(foo_1,arg)

with ThreadPoolExecutor(max_workers=12) as e:
    {e.submit(foo_1,i) for i in arg}


###############################################################
# 第三种用法
# 不同函数，无参
'''
不同的函数写进列表即可
'''

list = [foo,foo,foo,foo,foo]
with ThreadPoolExecutor(max_workers=12) as e:
    {e.submit(i) for i in list}  # 可以换成 []



############################################################
# 第四种用法
# 不同函数，不同参数（同一参数）都行
'''
不同函数，不同参数，分别写入列表
'''
arg = ['liyang','python','java','php','ruby','c++','golang']

list_1 = [foo_1,foo_1,foo_1,foo_1,foo_1,foo_1,foo_1] #有参函数

with ThreadPoolExecutor(max_workers=12) as e:
    {e.submit(i, (j)) for i, j in zip(list_1, arg)}








