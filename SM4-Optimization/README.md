# SM4 Optimization

## 1. 算法简介
SM4是一种**32轮不平衡Feistel结构**的分组密码，分组长度128位，密钥128位。其核心包括S盒变换与线性变换。

## 2. 优化实现
### (1) T-Table
通过预计算S盒与线性变换的组合（T表）减少每轮运算。
### (2) AES-NI & GFNI
利用Intel AES-NI指令和GFNI指令集实现硬件加速。
### (3) GCM模式
基于Galois域乘法的Galois/Counter Mode，适合高速加密与完整性保护。

## 3. 性能优化思路
- **循环展开**：减少分支与循环开销
- **SIMD并行**：在多块数据加密时批量执行
- **内存优化**：减少寄存器-内存切换

## 4. 运行方式
```bash
gcc src/sm4_basic.c -o sm4 && ./sm4
python benchmark/perf_compare.py
```
