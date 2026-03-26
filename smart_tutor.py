streamlit==1.32.0
numpy==1.26.4
pandas==2.1.4
plotly==5.18.0
networkx==3.2.1
Cloud 优化版本

# 核心框架 - 使用兼容版本
streamlit>=1.28.0,<1.40.0
numpy>=1.24.0,<2.0.0
# scipy  # 未使用，已移除

# 数据处理
pandas>=2.0.0,<2.2.0
openpyxl>=3.1.0

# 可视化
plotly>=5.15.0,<6.0.0
matplotlib>=3.7.0,<3.9.0

# 图像处理 - 基础版本
pillow>=10.0.0

# 知识图谱
networkx>=3.1,<3.4

# 工具
python-dateutil>=2.8.0

# OCR功能 - 可选依赖（Streamlit Cloud可能不支持）
# 如需OCR功能，请在本地安装：
# pip install paddlepaddle paddleocr opencv-python
# 注意：Streamlit Cloud 上 OCR 功能将自动禁用
