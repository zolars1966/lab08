import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch

# Границы отображения
x_min, x_max = -3, 8
y_min, y_max = -8, 3

fig, ax = plt.subplots(figsize=(8, 8))

# Область 0: x >= 5 и y >= -5 (зелёный)
ax.add_patch(Rectangle((5, -5), x_max - 5, y_max - (-5),
                       facecolor='#4daf4a', alpha=0.55, edgecolor='none'))

# Область 1: (x < 0 или y < 0) и не область 0 (красный)
# Кусок 1a: x < 0, y >= -5
ax.add_patch(Rectangle((x_min, -5), 0 - x_min, y_max - (-5),
                       facecolor='#e41a1c', alpha=0.55, edgecolor='none'))
# Кусок 1b: y < -5
ax.add_patch(Rectangle((x_min, y_min), x_max - x_min, -5 - y_min,
                       facecolor='#e41a1c', alpha=0.55, edgecolor='none'))
# Кусок 1c: 0 <= x < 5, -5 <= y < 0  <-- пропущенный центральный квадрат
ax.add_patch(Rectangle((0, -5), 5 - 0, 0 - (-5),
                       facecolor='#e41a1c', alpha=0.55, edgecolor='none'))
# Область 2: 0 <= x < 5, y >= 0 (синий)
ax.add_patch(Rectangle((0, 0), 5 - 0, y_max - 0,
                       facecolor='#377eb8', alpha=0.55, edgecolor='none'))

# Граничные прямые
ax.axvline(5, color='black', linestyle='--', linewidth=1)
ax.axhline(-5, color='black', linestyle='--', linewidth=1)
ax.axvline(0, color='gray', linestyle=':', linewidth=0.8)
ax.axhline(0, color='gray', linestyle=':', linewidth=0.8)

ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Множества значений для вывода 0, 1, 2')
ax.grid(True, alpha=0.3)

legend_elements = [
    Patch(facecolor='#4daf4a', alpha=0.55, label='0: x >= 5 и y >= -5'),
    Patch(facecolor='#e41a1c', alpha=0.55, label='1: x < 0 или y < 0 (и не 0)'),
    Patch(facecolor='#377eb8', alpha=0.55, label='2: 0 <= x < 5, y >= 0'),
]
ax.legend(handles=legend_elements, loc='lower left', fontsize=10)

plt.tight_layout()
plt.savefig('task8_regions.png', dpi=120)
print('Готово: task8_regions.png')