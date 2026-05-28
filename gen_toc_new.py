import win32com.client
import time
import sys
import re
import os

sys.stdout.reconfigure(encoding='utf-8')

filepath = r"D:\Tele-Health\Earthquake_Building_Damage_Prediction_proposal.docx"
output_path = r"D:\Tele-Health\TOC_Output.docx"

os.system("taskkill /f /im WINWORD.EXE 2>nul")
time.sleep(3)

# ========== PHASE 1: READ SOURCE DOCUMENT ==========
word = win32com.client.Dispatch("Word.Application")
word.Visible = False
time.sleep(1)

doc = word.Documents.Open(filepath)
time.sleep(3)

headings = []
figures = []
tables_list = []

chapter_pat = re.compile(r'^CHAPTER\s+\d+$', re.IGNORECASE)
sub_pat = re.compile(r'^(\d+\.\d+)\s+(.+)$')
fig_pat = re.compile(r'^Figure\s+[\d.]+[:\s]', re.IGNORECASE)
tbl_pat = re.compile(r'^Table\s+[\d.]+[:\s]', re.IGNORECASE)

front_matter_exact = {
    "ACKNOWLEDGEMENT", "STUDENT'S DECLARATION", "SUPERVISER'S DECLARATION",
    "SUPERVISOR'S DECLARATION", "LETTER OF APPROVAL", "ABSTRACT",
    "LIST OF FIGURES", "LIST OF TABLES", "ABBREVIATIONS", "BIBLIOGRAPHY", "REFERENCES"
}
main_titles = ["INTRODUCTION", "METHODOLOGY", "REQUIREMENT DOCUMENT",
               "SYSTEM ANALYSIS AND DESIGN", "DEVELOPMENT PLAN",
               "TESTING STRATEGY", "EXPECTED RESULTS",
               "FUTURE ENHANCEMENTS", "CONCLUSION"]

para_count = doc.Paragraphs.Count

for i in range(1, para_count + 1):
    para = doc.Paragraphs(i)
    raw = para.Range.Text
    text = raw.strip().replace('\r', '').replace('\x07', '')
    if not text or len(text) < 3:
        continue
    if '………' in text or '……' in text:
        continue

    page = para.Range.Information(3)
    text_upper = text.upper().strip()

    if fig_pat.match(text):
        figures.append((text[:100], page))
        continue
    if tbl_pat.match(text) and len(text) < 100:
        tables_list.append((text[:100], page))
        continue
    if text_upper in front_matter_exact:
        headings.append((text, page, 0))
        continue
    if chapter_pat.match(text_upper):
        headings.append((text, page, 1))
        continue
    is_main = any(text_upper == mt for mt in main_titles)
    if is_main:
        headings.append((text, page, 1))
        continue
    if sub_pat.match(text) and len(text) < 80 and '\x07' not in raw:
        headings.append((text, page, 2))
        continue
    if text_upper.startswith("ANNEX") and len(text) < 30:
        headings.append((text, page, 1))
        continue

doc.Close(False)
word.Quit()
time.sleep(2)

print(f"Headings: {len(headings)} | Figures: {len(figures)} | Tables: {len(tables_list)}")
for h in headings:
    lvl = ["FRONT","CH/MAIN","SUB"][min(h[2],2)]
    print(f"  [{lvl:>7}] p{h[1]:>2} | {h[0]}")
print()
for f in figures:
    print(f"  [FIG] p{f[1]:>2} | {f[0]}")
print()
for t in tables_list:
    print(f"  [TBL] p{t[1]:>2} | {t[0]}")

# ========== PHASE 2: CREATE OUTPUT DOCUMENT ==========
print("\nCreating output document...")

word2 = win32com.client.Dispatch("Word.Application")
word2.Visible = False
time.sleep(1)

new_doc = word2.Documents.Add()
time.sleep(1)

# Page setup via Sections
new_doc.Sections.Item(1).PageSetup.TopMargin = 72
new_doc.Sections.Item(1).PageSetup.BottomMargin = 72
new_doc.Sections.Item(1).PageSetup.LeftMargin = 72
new_doc.Sections.Item(1).PageSetup.RightMargin = 72

tab_pos = 72 * 6.0

def write_title(title_text):
    rng = new_doc.Content
    rng.Collapse(0)
    rng.InsertAfter(title_text + "\r")
    s = rng.End - len(title_text) - 1
    tr = new_doc.Range(s, rng.End - 1)
    tr.Font.Name = "Times New Roman"
    tr.Font.Size = 14
    tr.Font.Bold = True
    tr.ParagraphFormat.Alignment = 1
    tr.ParagraphFormat.SpaceAfter = 14

def write_entry(text, page, bold=False, indent=0):
    rng = new_doc.Content
    rng.Collapse(0)
    line = text + "\t" + str(page) + "\r"
    rng.InsertAfter(line)
    s = rng.End - len(line)
    lr = new_doc.Range(s, rng.End - 1)
    lr.Font.Name = "Times New Roman"
    lr.Font.Size = 12
    lr.Font.Bold = bold
    lr.ParagraphFormat.Alignment = 0
    lr.ParagraphFormat.SpaceAfter = 2
    lr.ParagraphFormat.SpaceBefore = 1
    lr.ParagraphFormat.LeftIndent = indent
    lr.ParagraphFormat.LineSpacingRule = 0
    lr.ParagraphFormat.TabStops.ClearAll()
    lr.ParagraphFormat.TabStops.Add(Position=tab_pos, Alignment=2, Leader=2)

def page_break():
    rng = new_doc.Content
    rng.Collapse(0)
    rng.InsertBreak(7)

# === TABLE OF CONTENTS ===
write_title("TABLE OF CONTENTS")
for text, page, level in headings:
    if level <= 1:
        write_entry(text, page, bold=True, indent=0)
    else:
        write_entry(text, page, bold=False, indent=28)

# === LIST OF FIGURES ===
page_break()
write_title("LIST OF FIGURES")
for text, page in figures:
    write_entry(text, page, bold=False, indent=0)

# === LIST OF TABLES ===
page_break()
write_title("LIST OF TABLES")
for text, page in tables_list:
    write_entry(text, page, bold=False, indent=0)

new_doc.SaveAs(output_path)
new_doc.Close()
word2.Quit()

print(f"\nDone! Saved to: {output_path}")
