# Image Watermark Detection

## 1. 算法简介
利用DCT或空间叠加嵌入数字水印，并在图片被翻转、裁剪、对比度变化等攻击后检测水印是否仍存在。

## 2. 鲁棒性测试
实现包括翻转、平移、对比度调整、裁剪等测试。

## 3. 运行方式
```bash
python src/embed_watermark.py
python src/robustness_test.py
```
