import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor('white')

# Simple tasks — 7 items only
tasks = [
    ('Research & Planning',    0.0, 1.0, '#3498DB'),
    ('Data Analysis & EDA',    0.5, 1.5, '#E67E22'),
    ('Preprocessing',          1.0, 1.0, '#E67E22'),
    ('Model Training',         1.5, 1.5, '#2ECC71'),
    ('Model Evaluation',       2.5, 0.5, '#2ECC71'),
    ('Web App Development',    2.5, 1.5, '#F1C40F'),
    ('Testing & Documentation',3.0, 1.0, '#9B59B6'),
]

tasks.reverse()

bar_height = 0.55
y_positions = list(range(len(tasks)))

for i, (name, start, dur, color) in enumerate(tasks):
    ax.barh(y_positions[i], dur, left=start, height=bar_height,
            color=color, edgecolor='white', linewidth=1.5,
            alpha=0.85, zorder=3, 
            )
    # Label inside bar
    ax.text(start + dur / 2, y_positions[i], name,
            ha='center', va='center', fontsize=9.5,
            fontweight='bold', color='white', fontfamily='sans-serif',
            zorder=4)

# Week boundaries
for x in [0, 1, 2, 3, 4]:
    ax.axvline(x=x, color='#D5D8DC', linewidth=0.8, linestyle='-', zorder=1)

# Week labels
for w in range(4):
    ax.text(w + 0.5, len(tasks) + 0.15, f'Week {w+1}',
            ha='center', va='bottom', fontsize=13,
            fontweight='bold', fontfamily='sans-serif', color='#2C3E50')

# Milestones (diamond markers)
milestones = [
    (1.0, 'Proposal\nApproved', '#2C3E50'),
    (2.0, 'Dataset\nReady', '#E67E22'),
    (3.0, 'Models\nTrained', '#2ECC71'),
    (4.0, 'Project\nSubmitted', '#9B59B6'),
]

for mx, label, color in milestones:
    ax.plot(mx, -0.9, marker='D', markersize=10, color=color, zorder=5)
    ax.text(mx, -1.5, label, ha='center', va='top', fontsize=8,
            fontweight='bold', color=color, fontfamily='sans-serif')

# Milestone label
ax.text(-0.3, -0.9, 'Milestones:', ha='right', va='center', fontsize=9,
        fontweight='bold', fontstyle='italic', color='#7F8C8D',
        fontfamily='sans-serif')

# Styling
ax.set_xlim(-0.3, 4.3)
ax.set_ylim(-2.2, len(tasks) + 0.6)
ax.set_yticks([])
ax.set_xticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Title
ax.set_title('Project Gantt Chart',
             fontsize=16, fontweight='bold', fontfamily='sans-serif',
             color='#2C3E50', pad=25)

# Thin separator line above milestones
ax.axhline(y=-0.45, color='#D5D8DC', linewidth=0.8, zorder=1)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15, top=0.88)

path = r'd:\Tele-Health\Gantt_Chart_Clean.png'
plt.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
print(f'Saved: {path}')
plt.close()
