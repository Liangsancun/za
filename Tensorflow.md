Tensorflow

tensorflow

最早的ML形式之一：概率建模（probabilistic modeling）

> 1.朴素贝叶斯：基于贝叶斯定理的分类器
>
> > 朴素：假设输入数据的特征彼此独立
>
> 2.逻辑斯蒂回归：分类算法（而非回归算法）

早期训练神经网络的方法：反向传播算法（利用梯度下降）

核方法（kernel model）：一组分类算法

> 支持向量机（SVM: support vector machine）

```python
python/c++都采用命令式编程(Imperative):明确输入变量，根据程序逻辑逐步运算
tensorflow采用符号式编程/声明式编程(Symbolic)：将计算过程抽象为计算图，所有输入节点-运算节点-输出节点均符号化处理。

```

```python
tensor张量：数据容器，存储数据的容器，是矩阵向任意维度的推广（相当于数字，向量，矩阵通称为张量，不管是不是numpy数组，但是由于numpy数组进行矩阵计算更快，所以一般指numpy数组）。张量的维度(dimension)叫轴(axix)
张量的属性：
	1. 轴的个数（阶）：矩阵有2个轴，向量有1个轴。numpy数组可通过np_array.ndim查看
    2. 形状：整数元组，表示张量沿每个轴的维度大小（即每个轴的元素个数）。
    	2D张量 eg: shape=(2,3)
        1D张量 eg：shape=(2,)
    3. 数据类型(也即每个元素的类型，dtype)
    	float32,float64,uint8,char
       
    
标量scalar：0D 0维张量
	只有一个数字
向量vector：1D 1维张量 ：一个轴
	数字组成的数组
	3D向量不同于3D张量，为：1个轴，维度为3
矩阵matrix：2D 2维张量
	向量组成的数组
```



```python
#返回一个constant tensor(常量张量)，不可更改的张量
tf.constant(value,dtype=None,shape=None,name='Const',verify_shape=False)
'''
value是数或数组（不必非要为numpy数组）
value=2, value=[1,2]

dtype是tensor里每个元素的类型
dtype=tf.float32, dtype=tf.float64，dtype=None时为int32

shape是tensor的形状
shape=(2,3)
当value为一个数时，填充为shape形状
当value为数组时，元素个数要<=shape形状中的元素个数(eg：2*3)，重新将元素组成shape的形状，不够的位置填充上数组的最后一个元素

verify_shape=True 验证value形状和shape是否相同，如果不相同，则报错
'''

tf.Variable是一个可以通过在其身上进行op操作而更改值的Tensor
# 初始化所有Varibale(变量张量)操作 op，Variable需要初始化才能使用
init_op = tf.global_variables_initializer()
```

TensorFlow模型会保存在后缀为`.ckpt`的文件中。保存后在save这个文件夹中实际会出现3个文件，因为TensorFlow会将计算图的结构和图上参数取值分开保存。

`model.ckpt.meta`文件保存了TensorFlow计算图的结构，可以理解为神经网络的网络结构

`model.ckpt`文件保存了TensorFlow程序中每一个变量的取值

`checkpoint`文件保存了一个目录下所有的模型文件列表

```


Tensorflow训练后的模型可以保存checkpoint文件或pb文件。checkpoint文件是结构与权重分离的四个文件，便于训练；pb文件则是graph_def的序列化文件，类似于caffemodel，便于发布和离线预测。官方提供freeze_grpah.py脚本来将ckpt文件转为pb文件。
Checkpoint保存断点文件列表，可以用来迅速查找最近一次的断点文件；
meta文件是MetaGraphDef序列化的二进制文件，保存了网络结构相关的数据，包括graph_def和saver_def等；
index文件为数据文件提供索引，存储的核心内容是以tensor name为键以BundleEntry为值的表格entries，BundleEntry主要内容是权值的类型、形状、偏移、校验和等信息。Index文件由data block/index block/Footer等组成，构建时主要涉及BundleWriter、TableBuilder、BlockBuilder几个类，除了BundleEntry的序列化，还涉及了tensor name的编码及优化（比如丢弃重复的前缀）和data block的snappy压缩。
数据（data）文件保存所有变量的值，即网络权值6
```

