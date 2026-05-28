import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(10, 14), dpi=300)
ax.set_xlim(0, 10)
ax.set_ylim(0, 16)
ax.axis('off')
fig.patch.set_facecolor('white')

def draw_box(ax, x, y, w, h, title, subtitle=None, fill='#f0f0f0', border='#333333', lw=1.5):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15", 
                          facecolor=fill, edgecolor=border, linewidth=lw)
    ax.add_patch(box)
    if subtitle:
        ax.text(x + w/2, y + h/2 + 0.12, title, ha='center', va='center', 
                fontsize=11, fontweight='bold', color='#222222', family='serif')
        ax.text(x + w/2, y + h/2 - 0.18, subtitle, ha='center', va='center', 
                fontsize=8.5, color='#555555', family='serif')
    else:
        ax.text(x + w/2, y + h/2, title, ha='center', va='center', 
                fontsize=11, fontweight='bold', color='#222222', family='serif')

def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle='->', color='#333333', lw=1.5))

# Layout
cx = 5.0  # center x
bw = 5.0  # box width
bh = 0.7  # box height
gap = 0.45  # gap between boxes

# Positions (top to bottom)
y_positions = []
y = 14.5

# 1. DrivenData Dataset
draw_box(ax, cx - bw/2, y, bw, bh, 'DrivenData Dataset', '260,601 buildings, 39 features')
y_positions.append(y)
y_prev = y

# Arrow
y -= (bh + gap)
draw_arrow(ax, cx, y_prev, cx, y + bh)

# 2. Exploratory Data Analysis
draw_box(ax, cx - bw/2, y, bw, bh, 'Exploratory Data Analysis', 'Distribution, correlation, class balance')
y_positions.append(y)
y_prev = y

# Arrow
y -= (bh + gap)
draw_arrow(ax, cx, y_prev, cx, y + bh)

# 3. Data Preprocessing
draw_box(ax, cx - bw/2, y, bw, bh, 'Data Preprocessing', 'Encoding, scaling, train-test split (80:20)')
y_positions.append(y)
y_prev = y

# Arrow
y -= (bh + gap)
draw_arrow(ax, cx, y_prev, cx, y + bh)

# 4. Feature Selection
draw_box(ax, cx - bw/2, y, bw, bh, 'Feature Selection', 'RF importance scores, threshold filtering')
y_positions.append(y)
y_prev = y

# Arrow
y -= (bh + gap)
draw_arrow(ax, cx, y_prev, cx, y + bh)

# 5. Model Training with GridSearchCV (wider box)
train_w = 6.0
draw_box(ax, cx - train_w/2, y, train_w, bh, 'Model Training with GridSearchCV', fill='#e8e8e8')
y_train = y
y_prev = y

# 4 model boxes below
y -= (bh + 0.25)
model_w = 1.25
model_h = 0.55
models = ['Decision\nTree', 'KNN', 'Random\nForest', 'XGBoost']
model_start_x = cx - (4 * model_w + 3 * 0.2) / 2

for i, name in enumerate(models):
    mx = model_start_x + i * (model_w + 0.2)
    draw_box(ax, mx, y, model_w, model_h, name, fill='#ffffff', border='#555555', lw=1.2)
    # line from training box to each model
    draw_arrow(ax, mx + model_w/2, y_train, mx + model_w/2, y + model_h)

y_model_bottom = y
y_prev = y

# Arrow from models to evaluation (from center two models)
y -= (model_h + gap)
draw_arrow(ax, cx, y_model_bottom, cx, y + bh)

# 6. Model Evaluation
draw_box(ax, cx - bw/2, y, bw, bh, 'Model Evaluation', 'F1-Score, Accuracy, Precision, Recall, Confusion Matrix')
y_positions.append(y)
y_prev = y

# Arrow
y -= (bh + gap)
draw_arrow(ax, cx, y_prev, cx, y + bh)

# 7. Best Model Selection
sel_w = 4.0
draw_box(ax, cx - sel_w/2, y, sel_w, bh, 'Best Model Selection', 'Serialized with joblib', fill='#e8e8e8')
y_positions.append(y)
y_prev = y

# Arrow
y -= (bh + gap)
draw_arrow(ax, cx, y_prev, cx, y + bh)

# 8. FastAPI Web Application
draw_box(ax, cx - bw/2, y, bw, bh, 'FastAPI Web Application', 'User input \u2192 Damage grade prediction', fill='#dcdcdc')
y_positions.append(y)

plt.tight_layout()
plt.savefig(r'd:\Tele-Health\ml_pipeline_diagram.png', dpi=300, bbox_inches='tight', 
            facecolor='white', edgecolor='none', pad_inches=0.3)
plt.close()
print("Done! Saved to d:\\Tele-Health\\ml_pipeline_diagram.png")
