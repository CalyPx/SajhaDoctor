import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('white')

# Tasks (bottom to top in chart)
tasks = [
    # Phase 5
    ('Presentation & submission', 3.5, 0.5, '#9B59B6', False),
    ('Final report writing', 3.0, 1.0, '#9B59B6', False),
    ('Functional & accuracy testing', 3.5, 0.5, '#8E44AD', False),
    ('Phase 5: Testing & Documentation', 3.5, 0.5, '#6C3483', True),
    # Phase 4
    ('Integration testing', 3.5, 0.5, '#F1C40F', False),
    ('Web form frontend', 2.5, 1.5, '#F1C40F', False),
    ('FastAPI backend', 2.5, 1.5, '#F39C12', False),
    ('Save model (joblib)', 2.5, 0.5, '#F39C12', False),
    ('Phase 4: Deployment', 2.5, 1.5, '#D68910', True),
    # Phase 3
    ('Model evaluation & comparison', 2.5, 0.5, '#2ECC71', False),
    ('Hyperparameter tuning', 2.0, 1.0, '#2ECC71', False),
    ('Train RF & XGBoost', 1.5, 1.5, '#27AE60', False),
    ('Train DT & KNN', 1.5, 0.5, '#27AE60', False),
    ('Feature selection', 1.5, 0.5, '#1E8449', False),
    ('Phase 3: Model Development', 1.5, 1.5, '#196F3D', True),
    # Phase 2
    ('Train-test split & scaling', 1.5, 0.5, '#E67E22', False),
    ('Data preprocessing & encoding', 1.0, 1.0, '#E67E22', False),
    ('Exploratory Data Analysis', 0.5, 1.5, '#E67E22', False),
    ('Dataset download & merging', 0.5, 0.5, '#D35400', False),
    ('Phase 2: Data Analysis', 0.5, 1.5, '#A04000', True),
    # Phase 1
    ('Dataset study & tool setup', 0.0, 1.0, '#5DADE2', False),
    ('Literature review & proposal', 0.0, 1.0, '#5DADE2', False),
    ('Phase 1: Research & Planning', 0.0, 1.0, '#2471A3', True),
]

tasks.reverse()

y_positions = []
y = 0
for i, (name, start, dur, color, is_phase) in enumerate(tasks):
    y_positions.append(y)
    y += 1

bar_height = 0.6

for i, (name, start, dur, color, is_phase) in enumerate(tasks):
    y = y_positions[i]
    
    if is_phase:
        ax.barh(y, dur, left=start, height=bar_height + 0.1,
                color=color, edgecolor='white', linewidth=1.5,
                alpha=0.95, zorder=3)
        ax.text(-0.05, y, name, ha='right', va='center',
                fontsize=10, fontweight='bold', fontfamily='sans-serif',
                color='#2C3E50')
    else:
        ax.barh(y, dur, left=start, height=bar_height,
                color=color, edgecolor='white', linewidth=1,
                alpha=0.8, zorder=3, 
                )
        ax.text(-0.05, y, name, ha='right', va='center',
                fontsize=9, fontfamily='sans-serif',
                color='#555555')

# Grid and styling
ax.set_xlim(-0.1, 4.1)
ax.set_ylim(-0.8, len(tasks) - 0.2)

# Week labels on top
week_positions = [0.5, 1.5, 2.5, 3.5]
week_labels = ['Week 1', 'Week 2', 'Week 3', 'Week 4']

ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(['', '', '', '', ''])

# Week boundaries
for x in [0, 1, 2, 3, 4]:
    ax.axvline(x=x, color='#BDC3C7', linewidth=0.8, linestyle='-', zorder=1)

# Week labels at top
for pos, label in zip(week_positions, week_labels):
    ax.text(pos, len(tasks) - 0.1, label, ha='center', va='bottom',
            fontsize=12, fontweight='bold', fontfamily='sans-serif',
            color='#2C3E50')

# Horizontal grid
for i in range(len(tasks)):
    ax.axhline(y=i - 0.4, color='#EAECEE', linewidth=0.5, zorder=1)

ax.set_yticks([])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_color('#BDC3C7')

# Title
ax.set_title('Project Gantt Chart — Earthquake Building Damage Prediction',
             fontsize=14, fontweight='bold', fontfamily='sans-serif',
             color='#2C3E50', pad=30)

# Legend
legend_items = [
    mpatches.Patch(color='#2471A3', label='Phase 1: Research & Planning'),
    mpatches.Patch(color='#A04000', label='Phase 2: Data Analysis'),
    mpatches.Patch(color='#196F3D', label='Phase 3: Model Development'),
    mpatches.Patch(color='#D68910', label='Phase 4: Deployment'),
    mpatches.Patch(color='#6C3483', label='Phase 5: Testing & Docs'),
]

ax.legend(handles=legend_items, loc='lower right', fontsize=9,
          framealpha=0.9, edgecolor='#BDC3C7', ncol=2)

# Responsible labels at bottom
ax.text(0.5, -0.7, 'Both', ha='center', va='center', fontsize=8,
        fontstyle='italic', color='#7F8C8D')
ax.text(1.0, -0.7, 'Keshav KC', ha='center', va='center', fontsize=8,
        fontstyle='italic', color='#7F8C8D')
ax.text(2.0, -0.7, 'Rohit Poudel', ha='center', va='center', fontsize=8,
        fontstyle='italic', color='#7F8C8D')
ax.text(3.5, -0.7, 'Both', ha='center', va='center', fontsize=8,
        fontstyle='italic', color='#7F8C8D')

plt.tight_layout()
plt.subplots_adjust(left=0.32, top=0.92, bottom=0.08)

path = r'd:\Tele-Health\Gantt_Chart.png'
plt.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
print(f'Saved: {path}')
plt.close()
