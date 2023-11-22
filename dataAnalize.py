# 파일 이름: data_analysis_visualization.py

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 생성
np.random.seed(0)
data = np.random.randn(100, 2)
variable_1, variable_2 = data[:, 0], data[:, 1]

# 플로팅 설정
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Descriptive Statistics: Mean and Median
axes[0, 0].bar(['Mean', 'Median'], [np.mean(variable_1), np.median(variable_1)], color='blue', alpha=0.7, label='Variable 1')
axes[0, 0].bar(['Mean', 'Median'], [np.mean(variable_2), np.median(variable_2)], color='green', alpha=0.7, label='Variable 2')
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')
axes[0, 0].legend()

# Correlation Analysis
correlation_matrix = np.corrcoef(data.T)
sns.heatmap(correlation_matrix, annot=True, ax=axes[0, 1])
axes[0, 1].set_title('Correlation Analysis')

# Histogram of Variables
axes[1, 0].hist([variable_1, variable_2], bins=15, color=['blue', 'green'], alpha=0.7, label=['Variable 1', 'Variable 2'])
axes[1, 0].legend()
axes[1, 0].set_title('Histogram of Variables')

# Scatter Plot of Variable 1 vs Variable 2
axes[1, 1].scatter(variable_1, variable_2, alpha=0.7)
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')

# 레이아웃 조정 및 플로팅
plt.tight_layout()
plt.show()

