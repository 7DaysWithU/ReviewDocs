# 一元函数微分学物理应用

## 1 知识点

* 物理应用
  * $速度=\dfrac{\mathrm{d}位移}{\mathrm{d}时间}$

  * $加速度=\dfrac{\mathrm{d}速度}{\mathrm{d}时间}$
  * 不涉及时间时，使用该式亦可求加速度： $a(t)=\dfrac{\mathrm{d}v}{\mathrm{d}t}=\dfrac{\mathrm{d}v}{\mathrm{d}s}\cdot\dfrac{\mathrm{d}s}{\mathrm{d}t}=\dfrac{\mathrm{d}v}{\mathrm{d}s}\cdot v(t)$
* 相关变化率
  * 研究 $\dfrac{\mathrm{d}A}{\mathrm{d}B}=\dfrac{\mathrm{d}A}{\mathrm{d}C}\cdot\dfrac{\mathrm{d}C}{\mathrm{d}B}$ ，其中 $\dfrac{\mathrm{d}A}{\mathrm{d}C}=\dfrac{\dfrac{\mathrm{d}A}{\mathrm{d}B}}{\dfrac{\mathrm{d}C}{\mathrm{d}B}}$ ， $\mathrm{d}C$ 常作为中间量

## 2 进阶

### 2.1 寻找并建立变化率等式 $\textcolor{LightSkyBlue}{\text{O} (盯住目标)}$

* 变化率等式 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{2} (脱胎换骨)}$
  * 错位法：$a(t)=\dfrac{\mathrm{d}v}{\mathrm{d}t}=\dfrac{\mathrm{d}v}{\mathrm{d}s}\cdot\dfrac{\mathrm{d}s}{\mathrm{d}t}=\dfrac{\mathrm{d}v}{\mathrm{d}s}\cdot v(t)$。利用幺元错位相乘，用于替换成已知的微分，消除部分不知道的微分
  * 二阶导：$a(t)=\dfrac{\mathrm{d}v}{\mathrm{d}t}=\dfrac{\mathrm{d}}{\mathrm{d}t}\left(\dfrac{\mathrm{d}x}{\mathrm{d}t}\right)=\dfrac{\mathrm{d}^2 x}{\mathrm{d}t^2}$。通过二阶导将一个微分转换成另一个微分

  * 根据题设写出物理微元 $\textcolor{Cyan}{\text{D}_\text{1} (常规操作) + \text{D}_\text{2} (脱胎换骨) + \text{D}_\text{22} (转换等价表述) + \text{D}_\text{42} (引入符号)}$
    * 细读题目并转化成数学语言。特别注意某些物理量的变化趋势，如下降、减少则是负的，一般取比例系数 $k>0$，这样在计算时不用担心不等式变号、分母不为零等问题，对此就需要注意物理量的正负，适当补负号
    * 使用错位法转化微分时，不用管转化出来的微分的物理意义，只需要计算方便就行

## 3 题目

* 基础30讲
  * 例7.1(相关变化率)
* 基础30讲课后题
  * 7.3(相关变化率、带初始参数)
* 1000题基础
  * 04(相关变化率、隐函数求导)
* 强化36讲
  * 例7.1(错位法)
  * 例7.2(细读题目转化成数学语言、注意物理概念的正负性)
* 1000题强化
