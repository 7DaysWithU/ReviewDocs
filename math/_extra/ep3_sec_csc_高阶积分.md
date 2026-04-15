# sec、csc的高阶积分

## 一、$\sec x$ 的幂次积分

### 1. $n = 1$

$$
\int \sec x \, dx = \ln \left| \sec x + \tan x \right| + C
$$

> **技巧**：乘以 $\frac{\sec x + \tan x}{\sec x + \tan x}$，化为对数导数。

---

### 2. $n = 2$

$$
\int \sec^2 x \, dx = \tan x + C
$$

> **直接由导数反推**：$\frac{d}{dx}(\tan x) = \sec^2 x$

---

### 3. $n = 3$

$$
\int \sec^3 x \, dx = \frac{1}{2} \left( \sec x \tan x + \ln \left| \sec x + \tan x \right| \right) + C
$$

> **推导**：分部积分法  
> 设 $u = \sec x$, $dv = \sec^2 x\,dx$，则 $du = \sec x \tan x\,dx$, $v = \tan x$  
> 得到：$\int \sec^3 x\,dx = \sec x \tan x - \int \sec x \tan^2 x\,dx$  
> 再用 $\tan^2 x = \sec^2 x - 1$ 化简，最终解出原积分。

---

### 4. $n = 4$

$$
\int \sec^4 x \, dx = \tan x + \frac{1}{3} \tan^3 x + C
$$

> **技巧**：利用 $\sec^2 x = 1 + \tan^2 x$  
> $$
> \int \sec^4 x\,dx = \int \sec^2 x \cdot \sec^2 x\,dx = \int (1 + \tan^2 x)\, d(\tan x)
> $$  
> 令 $u = \tan x$，则积分为 $\int (1 + u^2)\,du = u + \frac{u^3}{3} + C$

---

## 二、$\csc x$ 的幂次积分

### 1. $n = 1$

$$
\int \csc x\,dx = \ln \left| \csc x - \cot x \right| + C
$$

> **推导**：类似 $\sec x$，乘以 $\frac{\csc x + \cot x}{\csc x + \cot x}$，注意导数符号。

---

### 2. $n = 2$

$$
\int \csc^2 x \, dx = -\cot x + C
$$

> 因为 $\frac{d}{dx}(\cot x) = -\csc^2 x$

---

### 3. $n = 3$

$$
\int \csc^3 x \, dx = -\frac{1}{2} \left( \csc x \cot x + \ln \left| \csc x - \cot x \right| \right) + C
$$

> **推导**：与 $\sec^3 x$ 对称，用分部积分  
> 设 $u = \csc x$, $dv = \csc^2 x\,dx$，则 $du = -\csc x \cot x\,dx$, $v = -\cot x$  
> 最终得到类似结构，注意符号。

---

### 4. $n = 4$

$$
\int \csc^4 x \, dx = -\cot x - \frac{1}{3} \cot^3 x + C
$$

> **技巧**：$\csc^2 x = 1 + \cot^2 x$，且 $d(\cot x) = -\csc^2 x\,dx$  
> 所以：
> $$
> \int \csc^4 x\,dx = \int (1 + \cot^2 x) \csc^2 x\,dx = -\int (1 + u^2)\,du \quad (u = \cot x)
> $$  
> 结果为 $-u - \frac{u^3}{3} + C$

---

## 三、总结表格（便于记忆）

| 幂次 $n$ | $\displaystyle\int \sec^n x\,dx$ | $\displaystyle\int \csc^n x\,dx$ |
|------------|-----------------------------------|-----------------------------------|
| 1 | $\ln\lvert\sec x + \tan x\rvert + C$ | $\ln\lvert\csc x - \cot x\rvert + C$ |
| 2 | $\tan x + C$ | $-\cot x + C$ |
| 3 | $\frac{1}{2}(\sec x \tan x + \ln\lvert\sec x + \tan x\rvert) + C$ | $-\frac{1}{2}(\csc x \cot x + \ln\lvert\csc x - \cot x\rvert) + C$ |
| 4 | $\tan x + \frac{1}{3}\tan^3 x + C$ | $-\cot x - \frac{1}{3}\cot^3 x + C$ |

---

## 四、通用递推公式（进阶参考）

如果你需要更高次幂，可以用递推：

- 对 $n \geq 2$，
  $$
  \int \sec^n x\,dx = \frac{\sec^{n-2} x \tan x}{n-1} + \frac{n-2}{n-1} \int \sec^{n-2} x\,dx
  $$
- 类似地，
  $$
  \int \csc^n x\,dx = -\frac{\csc^{n-2} x \cot x}{n-1} + \frac{n-2}{n-1} \int \csc^{n-2} x\,dx
  $$

这些递推式可快速推出任意正整数次幂的积分。
