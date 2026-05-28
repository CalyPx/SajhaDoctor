import win32com.client
import os, time

word = win32com.client.Dispatch('Word.Application')
word.Visible = False

filepath = r'C:\Users\Gaming F16\OneDrive\Documents\Earthquake Building Damage Prediction.docx'
doc = word.Documents.Open(filepath)
time.sleep(2)

total = doc.ComputeStatistics(2)
print(f'Total pages: {total}')
print()

# Collect ALL paragraphs with page numbers
results = []
for p in doc.Paragraphs:
    text = p.Range.Text.strip()
    if not text:
        continue
    try:
        is_bold = p.Range.Font.Bold
        page = p.Range.Information(3)
        if is_bold and len(text) < 100:
            results.append((page, text, is_bold))
    except:
        pass

# Filter to actual headings only
skip_patterns = [
    'FR-0', 'NFR-0', 'Step ', 'Decision Tree Classifier',
    'K-Nearest Neighbor (KNN) :', 'Random Forest Classifier',
    'XGBoost Classifier', 'Model Testing:', 'Functional Testing:',
    'Integration Testing:', 'Submitted', 'Code for Change',
    'Artificial Intelligence', 'A Project', 'Using Machine',
    'Earthquake Building', 'Supervised', 'GitHub URL',
    'Enrollment', 'Submission Date'
]

for page, text, bold in results:
    if any(s in text for s in skip_patterns):
        continue
    if bold:
        print(f'Page {page:3d} | {text[:75]}')

doc.Close(False)
word.Quit()
