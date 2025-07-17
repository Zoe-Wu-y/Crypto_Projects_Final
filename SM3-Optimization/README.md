# SM3 Optimization

## 1. 算法简介
SM3基于Merkle-Damgård构造，输出256位哈希值。

## 2. 优化实现
- **SIMD优化**：批量处理多块消息
- **长度扩展攻击PoC**：验证Merkle-Damgård的固有缺陷
- **Merkle树构造**：支持存在性与不存在性证明

## 3. 运行方式
```bash
gcc src/sm3_basic.c -o sm3 && ./sm3
```
