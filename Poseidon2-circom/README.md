# Poseidon2 Hash Circuit

## 1. 算法简介
Poseidon2是为zkSNARK优化的哈希函数，基于GF(p)域的置换。

## 2. Circom电路实现
- **参数**: (n,t,d)=(256,3,5)
- **证明系统**: Groth16

## 3. 使用方法
```bash
bash scripts/compile_and_setup.sh
bash scripts/generate_proof.sh
bash scripts/verify_proof.sh
```
