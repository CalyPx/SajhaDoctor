import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(13, 5.5))
fig.patch.set_facecolor('white')

# 7 tasks — 1 color per phase
tasks = [
    ('Research & Planning',       0.0, 1.0, '#3498DB'),   # Phase 1 blue
    ('Data Analysis & EDA',       0.5, 1.5, '#E67E22'),   # Phase 2 orange
    ('Preprocessing',             1.0, 1.0, '#E67E22'),   # Phase 2 orange
    ('Model Training',            1.5, 1.5, '#2ECC71'),   # Phase 3 green
    ('Model Evaluation',          2.5, 1.0, '#2ECC71'),   # Phase 3 green — extended
    ('Web App Development',       2.5, 1.5, '#F1C40F'),   # Phase 4 yellow
    ('Testing & Documentation',   3.0, 1.0, '#9B59B6'),   # Phase 5 purple
]

tasks.reverse()

bar_height = 0.55
y_positions = list(range(len(tasks)))

for i, (name, start, dur, color) in enumerate(tasks):
    ax.barh(y_positions[i], dur, left=start, height=bar_height,
            color=color, edgecolor='white', linewidth=1.5,
            alpha=0.85, zorder=3)
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

# Milestones — centered exactly on week lines
milestones = [
    (1.0, 'Proposal\nApproved'),
    (2.0, 'Dataset\nReady'),
    (3.0, 'Models\nTrained'),
    (4.0, 'Project\nSubmitted'),
]

milestone_colors = ['#2C3E50', '#E67E22', '#2ECC71', '#9B59B6']

for (mx, label), mc in zip(milestones, milestone_colors):
    ax.plot(mx, -0.9, marker='D', markersize=11, color=mc, zorder=5)
    ax.text(mx, -1.55, label, ha='center', va='top', fontsize=8.5,
            fontweight='bold', color=mc, fontfamily='sans-serif')

ax.text(-0.35, -0.9, 'Milestones:', ha='right', va='center', fontsize=9,
        fontweight='bold', fontstyle='italic', color='#7F8C8D',
        fontfamily='sans-serif')

# Separator line
ax.axhline(y=-0.45, color='#D5D8DC', linewidth=0.8, zorder=1)

# Legend
legend_items = [
    mpatches.Patch(color='#3498DB', label='Phase 1: Research'),
    mpatches.Patch(color='#E67E22', label='Phase 2: Data'),
    mpatches.Patch(color='#2ECC71', label='Phase 3: Modeling'),
    mpatches.Patch(color='#F1C40F', label='Phase 4: Deployment'),
    mpatches.Patch(color='#9B59B6', label='Phase 5: Testing'),
]
ax.legend(handles=legend_items, loc='upper right', fontsize=8,
          framealpha=0.95, edgecolor='#D5D8DC', ncol=1,
          bbox_to_anchor=(1.01, 1.0))

# Styling
ax.set_xlim(-0.4, 4.35)
ax.set_ylim(-2.3, len(tasks) + 0.6)
ax.set_yticks([])
ax.set_xticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Title
ax.set_title('Gantt Chart \u2013 Earthquake Building Damage Prediction Project',
             fontsize=15, fontweight='bold', fontfamily='sans-serif',
             color='#2C3E50', pad=25)

plt.tight_layout()
plt.subplots_adjust(bottom=0.15, top=0.88)

path = r'd:\Tele-Health\Gantt_Chart_Final.png'
plt.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
print(f'Saved: {path}')
plt.close()
