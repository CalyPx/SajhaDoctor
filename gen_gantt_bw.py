import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(14, 7), dpi=300)
fig.patch.set_facecolor('white')

phases = [
    {"name": "Phase 1", "sub": "Research & Planning", "start": 0, "end": 1, "row": 4, "milestone": "Proposal approved, Environment ready"},
    {"name": "Phase 2", "sub": "Data Analysis & Preprocessing", "start": 0, "end": 2, "row": 3, "milestone": "Clean dataset ready for training"},
    {"name": "Phase 3", "sub": "Model Development", "start": 1, "end": 3, "row": 2, "milestone": "All four models trained & evaluated"},
    {"name": "Phase 4", "sub": "Deployment", "start": 2, "end": 4, "row": 1, "milestone": "Working web application live"},
    {"name": "Phase 5", "sub": "Testing & Documentation", "start": 3, "end": 4, "row": 0, "milestone": "Final report submitted, Demo done"},
]

# Simple black/white fills to distinguish bars
fills = ['black', 'white', 'black', 'white', 'black']
text_colors = ['white', 'black', 'white', 'black', 'white']

ax.set_xlim(-0.2, 5.8)
ax.set_ylim(-0.8, 5.8)
ax.set_aspect('auto')

# Grid lines
for x in range(5):
    ax.axvline(x=x, color='black', linewidth=0.4, linestyle='-', alpha=0.3)

# Week labels
for i in range(4):
    ax.text(i + 0.5, -0.45, f"Week {i+1}", ha='center', va='center',
            fontsize=11, fontweight='bold', family='serif')

# Bottom axis line
ax.axhline(y=-0.15, color='black', linewidth=0.8, xmin=0.03, xmax=0.72)

# Draw bars
bar_height = 0.5
for i, p in enumerate(phases):
    x = p["start"]
    w = p["end"] - p["start"]
    y = p["row"]
    
    rect = FancyBboxPatch((x + 0.02, y - bar_height/2), w - 0.04, bar_height,
                           boxstyle="round,pad=0.03",
                           facecolor=fills[i], edgecolor='black', linewidth=1.5)
    ax.add_patch(rect)
    
    tc = text_colors[i]
    ax.text(x + w/2, y + 0.07, p["name"], ha='center', va='center',
            fontsize=10, fontweight='bold', color=tc, family='serif')
    ax.text(x + w/2, y - 0.15, p["sub"], ha='center', va='center',
            fontsize=8, color=tc, family='serif')
    
    # Milestone
    ax.text(4.15, y, "- " + p["milestone"], ha='left', va='center',
            fontsize=7.5, color='black', family='serif', style='italic')

# Title
ax.text(2.0, 5.5, "Earthquake Building Damage Prediction - Project Gantt Chart",
        ha='center', va='center', fontsize=13, fontweight='bold', family='serif')
ax.text(2.0, 5.1, "AI/ML Microdegree | Code for Change, Pokhara | Rohit Poudel & Keshav KC | Supervisor: Mr. Diwash Sapkota",
        ha='center', va='center', fontsize=7.5, color='black', family='serif')

# Milestones header
ax.text(4.15, 4.85, "Milestones", ha='left', va='center', fontsize=10,
        fontweight='bold', family='serif')

# Legend
legend_y = -0.75
items = [
    ("Phase 1 - Research & Planning", 'black'),
    ("Phase 2 - Data Analysis", 'white'),
    ("Phase 3 - Model Development", 'black'),
    ("Phase 4 - Deployment", 'white'),
    ("Phase 5 - Testing & Docs", 'black'),
]
for j, (label, fc) in enumerate(items):
    lx = j * 1.1 - 0.1
    rect = plt.Rectangle((lx, legend_y - 0.08), 0.15, 0.16,
                          facecolor=fc, edgecolor='black', linewidth=0.8)
    ax.add_patch(rect)
    ax.text(lx + 0.2, legend_y, label, ha='left', va='center',
            fontsize=6.5, family='serif')

ax.axis('off')
plt.tight_layout()
plt.savefig(r'd:\Tele-Health\gantt_chart_bw.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none', pad_inches=0.3)
plt.close()
print("Done!")
