import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch

fig, ax = plt.subplots(1, 1, figsize=(12, 10), dpi=300)
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')
fig.patch.set_facecolor('white')

def draw_rect(ax, x, y, w, h, fill='#ffffff', border='#333333', lw=1.5, radius=0.1):
    box = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={radius}",
                          facecolor=fill, edgecolor=border, linewidth=lw)
    ax.add_patch(box)

def draw_text(ax, x, y, text, size=10, bold=False, color='#222222'):
    weight = 'bold' if bold else 'normal'
    ax.text(x, y, text, ha='center', va='center', fontsize=size,
            fontweight=weight, color=color, family='serif')

def draw_arrow(ax, x1, y1, x2, y2, label=None):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#333333', lw=1.5))
    if label:
        mx, my = (x1+x2)/2, (y1+y2)/2
        ax.text(mx + 0.15, my, label, ha='left', va='center', fontsize=8,
                color='#444444', family='serif', style='italic')

# ============================================================
# LAYER 1: FRONTEND (top)
# ============================================================
draw_rect(ax, 0.5, 7.0, 8.5, 2.5, fill='#f2f2f2', border='#333333', lw=2)
draw_text(ax, 1.6, 9.1, 'Frontend', size=13, bold=True)
draw_text(ax, 1.6, 8.7, '(HTML/CSS/JS)', size=9)

# Web Form box
draw_rect(ax, 2.5, 7.5, 3.0, 1.5, fill='#ffffff', border='#555555', lw=1.2)
draw_text(ax, 4.0, 8.55, 'Web Form', size=8, color='#555555')
draw_text(ax, 4.0, 8.15, 'Building Feature', size=10, bold=True)
draw_text(ax, 4.0, 7.8, 'Input Form', size=10, bold=True)

# Prediction Result box
draw_rect(ax, 6.0, 7.5, 2.5, 1.5, fill='#ffffff', border='#555555', lw=1.2)
draw_text(ax, 7.25, 8.3, 'Prediction Result', size=10, bold=True)
draw_text(ax, 7.25, 7.9, 'Display', size=10, bold=True)

# ============================================================
# LAYER 2: BACKEND (middle)
# ============================================================
draw_rect(ax, 0.5, 3.8, 8.5, 2.8, fill='#e6e6e6', border='#333333', lw=2)
draw_text(ax, 1.6, 6.2, 'Backend', size=13, bold=True)
draw_text(ax, 1.6, 5.8, '(FastAPI)', size=9)

# API Endpoint box
draw_rect(ax, 3.2, 5.5, 2.8, 0.8, fill='#ffffff', border='#555555', lw=1.2)
draw_text(ax, 4.6, 5.95, 'API Endpoint', size=10, bold=True)
draw_text(ax, 4.6, 5.65, '/predict', size=9)

# Model Loader box
draw_rect(ax, 2.5, 4.2, 2.3, 0.9, fill='#ffffff', border='#555555', lw=1.2)
draw_text(ax, 3.65, 4.75, 'Model Loader', size=10, bold=True)
draw_text(ax, 3.65, 4.45, '(joblib)', size=9)

# Data Validator box
draw_rect(ax, 5.5, 4.2, 2.3, 0.9, fill='#ffffff', border='#555555', lw=1.2)
draw_text(ax, 6.65, 4.75, 'Data Validator', size=10, bold=True)
draw_text(ax, 6.65, 4.45, '', size=9)

# Arrow: Features label between API and boxes
draw_text(ax, 5.2, 5.25, 'Features', size=8, color='#555555')

# ============================================================
# LAYER 3: ML ENGINE (bottom)
# ============================================================
draw_rect(ax, 0.5, 0.5, 8.5, 2.9, fill='#d4d4d4', border='#333333', lw=2)
draw_text(ax, 1.6, 3.0, 'ML Engine', size=13, bold=True)

# Trained Model box
draw_rect(ax, 2.5, 1.6, 2.5, 1.2, fill='#ffffff', border='#555555', lw=1.2)
draw_text(ax, 3.75, 2.3, 'Trained Model', size=10, bold=True)
draw_text(ax, 3.75, 1.95, '(.pkl file)', size=9)

# scikit-learn / XGBoost box
draw_rect(ax, 2.5, 0.7, 2.5, 0.7, fill='#ffffff', border='#555555', lw=1.2)
draw_text(ax, 3.75, 1.05, 'scikit-learn / XGBoost', size=9, bold=True)

# Dataset box
draw_rect(ax, 5.5, 1.6, 2.5, 1.2, fill='#ffffff', border='#555555', lw=1.2)
draw_text(ax, 6.75, 2.3, 'Dataset', size=10, bold=True)
draw_text(ax, 6.75, 1.95, '(DrivenData CSV)', size=9)

# ============================================================
# JUPYTER NOTEBOOK (side box)
# ============================================================
draw_rect(ax, 9.5, 0.8, 2.0, 2.5, fill='#ffffff', border='#555555', lw=1.2)
draw_text(ax, 10.5, 2.6, 'Jupyter', size=9, bold=True)
draw_text(ax, 10.5, 2.25, 'Notebook -', size=9, bold=True)
draw_text(ax, 10.5, 1.85, 'Training &', size=9)
draw_text(ax, 10.5, 1.5, 'Evaluation', size=9)
draw_text(ax, 10.5, 1.15, 'Pipeline', size=9)

# Dotted line from Jupyter to ML Engine
ax.plot([9.5, 9.0], [2.0, 2.0], '--', color='#777777', lw=1.2)

# ============================================================
# ARROWS BETWEEN LAYERS
# ============================================================
# Frontend -> Backend (Request)
draw_arrow(ax, 4.0, 7.0, 4.0, 6.6, 'Request')

# Backend -> Frontend (Prediction)
draw_arrow(ax, 7.0, 6.6, 7.0, 7.0, 'Prediction')

# Backend -> ML Engine (Load from)
draw_arrow(ax, 3.65, 3.8, 3.65, 3.4, 'Load from')

plt.tight_layout()
plt.savefig(r'd:\Tele-Health\system_architecture.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none', pad_inches=0.3)
plt.close()
print("Done! Saved to d:\\Tele-Health\\system_architecture.png")
