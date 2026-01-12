import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 设置中文字体（避免中文乱码，如不需要可注释）
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 1. 生成x轴数据：避开0和1（因Beta(0.1,0.1)在0/1处密度无穷大），取0.001到0.999的精细点
x = np.linspace(0.001, 0.999, 1000)

# 2. 计算Beta(0.1, 0.1)的概率密度值
alpha, beta = 0.1, 0.1
pdf = stats.beta.pdf(x, alpha, beta)

# 3. 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(x, pdf, color='#2E86AB', linewidth=2.5, label=f'Beta({alpha}, {beta}) 概率密度函数')

# 添加标注：标注中点、峰值趋势
plt.axvline(x=0.5, color='#A23B72', linestyle='--', linewidth=1.5, label='中点 x=0.5（最小值）')
plt.annotate('密度向0和1趋近于无穷', xy=(0.05, pdf[10]), xytext=(0.2, 8),
             arrowprops=dict(arrowstyle='->', color='red'), fontsize=10)
plt.annotate('密度向0和1趋近于无穷', xy=(0.95, pdf[-10]), xytext=(0.7, 8),
             arrowprops=dict(arrowstyle='->', color='red'), fontsize=10)

# 设置图形属性
plt.title('Beta(0.1, 0.1) 分布概率密度函数', fontsize=14, pad=20)
plt.xlabel('x (取值范围 [0,1])', fontsize=12)
plt.ylabel('概率密度', fontsize=12)
plt.xlim(0, 1)
plt.ylim(0, 10)  # 限制y轴范围，让图形更易读
plt.grid(alpha=0.3)
plt.legend(loc='upper center')

# 显示图形
plt.tight_layout()
plt.show()