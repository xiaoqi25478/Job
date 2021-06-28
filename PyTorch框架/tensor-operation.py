"""
https://zhuanlan.zhihu.com/p/257389827
"""
import torch

"""
expand()
将现有张量沿着值为1的维度扩展到新的维度。
张量可以同时沿着任意一维或多维展开。
如果你不想沿着一个特定的维度展开张量，你可以设置它的参数值为-1。
"""
a = torch.tensor([[[1,2,3],[4,5,6]]])
print(a.size())

a.expand(2,2,3)
print(a)

"""
permute()
这个函数返回一个张量的视图，原始张量的维数根据我们的选择而改变。
例如，如果原来的维数是[1,2,3]，我们可以将它改为[3,2,1]。
该函数以所需的维数顺序作为参数。
当我们想要对不同维数的张量进行重新排序，
或者用不同阶数的矩阵进行矩阵乘法时，可以使用这个函数。
"""

