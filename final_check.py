"""
Final comprehensive check of the Earthquake Building Damage Prediction proposal.
"""
import win32com.client
import time
import sys
import os

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

def check_proposal():
    filepath = r"C:\Users\Gaming F16\OneDrive\Documents\Earthquake Building Damage Prediction.docx"
    
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False
    
    try:
        doc = word.Documents.Open(filepath)
        time.sleep(3)
        
        total_pages = doc.ComputeStatistics(2)
        print(f"{'='*70}")
        print(f"TOTAL PAGES: {total_pages}")
        print(f"{'='*70}")
        
        # Extract all headings with page numbers
        print(f"\n{'='*70}")
        print("ALL HEADINGS WITH PAGE NUMBERS")
        print(f"{'='*70}")
        
        headings = []
        for para in doc.Paragraphs:
            style_name = para.Style.NameLocal
            text = para.Range.Text.strip()
            if not text:
                continue
            if "Heading" in style_name:
                page = para.Range.Information(3)
                headings.append((text, style_name, page))
                print(f"  Page {page:>3} | {style_name:<15} | {text[:80]}")
        
        # Full text checks
        print(f"\n{'='*70}")
        print("CONTENT CHECKS")
        print(f"{'='*70}")
        
        issues = []
        full_text = doc.Content.Text
        
        # 1. micro vs macro
        if "micro-averaged" in full_text.lower():
            issues.append("FOUND 'micro-averaged' -- should be 'macro-averaged'")
        else:
            print("  [OK] No 'micro-averaged' found")
        
        count_macro = full_text.lower().count("macro-averaged")
        print(f"  [OK] 'macro-averaged' appears {count_macro} time(s)")
        
        # 2. Onur vs Ulku
        onur_count = full_text.count("Onur,") + full_text.count("Onur ")
        if "Onur et al" in full_text or "Onur, " in full_text:
            issues.append("FOUND 'Onur' as author -- should be 'Ulku'")
        else:
            print("  [OK] No 'Onur' as author (using 'Ulku')")
        
        # 3. comprises of
        if "comprises of" in full_text.lower():
            issues.append("FOUND 'comprises of'")
        else:
            print("  [OK] No 'comprises of'")
        
        # 4. h5-file
        if "h5-file" in full_text.lower() or "h5 file" in full_text.lower():
            issues.append("FOUND 'h5-file' -- should be '.joblib'")
        else:
            print("  [OK] No 'h5-file'")
        
        # 5. XG Boost
        if "XG Boost" in full_text:
            issues.append("FOUND 'XG Boost' -- should be 'XGBoost'")
        else:
            print("  [OK] No 'XG Boost' (using 'XGBoost')")
        
        # 6. this criteria
        if "this criteria" in full_text.lower():
            issues.append("FOUND 'this criteria' -- should be 'this criterion'")
        else:
            print("  [OK] No 'this criteria'")
        
        # 7. taken care mainly
        if "taken care mainly" in full_text.lower():
            issues.append("FOUND 'taken care mainly' -- should be 'taken care of mainly'")
        else:
            print("  [OK] No 'taken care mainly'")
        
        # 8. Enhancments typo
        if "Enhancments" in full_text or "enhancments" in full_text.lower():
            issues.append("FOUND typo 'Enhancments' -- should be 'Enhancements'")
        else:
            print("  [OK] No 'Enhancments' typo")
        
        # 9. GitHub URL
        if "github.com/Code4Sake/earthquake-damage-prediction" in full_text:
            print("  [OK] GitHub URL present")
        elif "To be added" in full_text:
            issues.append("GitHub URL still says 'To be added'")
        else:
            print("  [??] GitHub URL status unclear")
        
        # 10. DrivenData reference
        if "DrivenData. (n.d.)" in full_text:
            print("  [OK] DrivenData reference present")
        else:
            issues.append("MISSING DrivenData reference")
        
        # 11. Double periods
        # Check for '..' but not '...'
        text_no_ellipsis = full_text.replace("...", "")
        if ".." in text_no_ellipsis:
            issues.append("FOUND double period '..' somewhere")
        else:
            print("  [OK] No double periods")
        
        # 12. Colon after headings
        for text, style, page in headings:
            if "Heading 1" in style and text.rstrip().endswith(":"):
                issues.append(f"Heading has trailing colon: '{text[:50]}'")
        
        # Figure captions
        print(f"\n{'='*70}")
        print("FIGURE CAPTIONS")
        print(f"{'='*70}")
        for para in doc.Paragraphs:
            text = para.Range.Text.strip()
            if text.startswith("Figure") and ":" in text[:15]:
                page = para.Range.Information(3)
                print(f"  Page {page:>3} | {text[:80]}")
        
        # Heading case check
        print(f"\n{'='*70}")
        print("HEADING CASE CHECK (Heading 1 only)")
        print(f"{'='*70}")
        for text, style, page in headings:
            if "Heading 1" in style:
                # Remove numbers at start
                clean = text.lstrip("0123456789. ")
                if clean.isupper():
                    print(f"  [CAPS] Page {page:>3} | {text[:60]}")
                else:
                    print(f"  [mixed] Page {page:>3} | {text[:60]}")
                    issues.append(f"Heading NOT all caps: '{text[:50]}'")
        
        # References check
        print(f"\n{'='*70}")
        print("REFERENCES CHECK")
        print(f"{'='*70}")
        ref_authors = ["Adi, S.", "Bhatta, S.", "Ghimire, S.", "Ulku, O.", "Poudyal, B.", "DrivenData"]
        for author in ref_authors:
            if author in full_text:
                print(f"  [OK] Found: {author}")
            else:
                issues.append(f"MISSING reference: {author}")
        
        # Check references for old "Onur" 
        ref_start = full_text.find("References")
        if ref_start > 0:
            ref_text = full_text[ref_start:]
            if "Onur, U." in ref_text:
                issues.append("References still has 'Onur, U.' -- should be 'Ulku, O.'")
        
        # PAGE NUMBER SUMMARY
        print(f"\n{'='*70}")
        print("ACTUAL PAGE NUMBERS FOR TOC VERIFICATION")
        print(f"{'='*70}")
        for text, style, page in headings:
            level = ""
            if "Heading 1" in style:
                level = "H1"
            elif "Heading 2" in style:
                level = "  H2"
            elif "Heading 3" in style:
                level = "    H3"
            print(f"  {level:<6} Page {page:>3} | {text[:65]}")
        
        # FINAL REPORT
        print(f"\n{'='*70}")
        print(f"FINAL REPORT - ISSUES FOUND: {len(issues)}")
        print(f"{'='*70}")
        if issues:
            for i, issue in enumerate(issues, 1):
                print(f"  {i}. [!!] {issue}")
        else:
            print("  [OK] NO ISSUES FOUND -- READY TO SUBMIT!")
        
        print(f"\n{'='*70}")
        print("DONE")
        print(f"{'='*70}")
        
        doc.Close(False)
    except Exception as e:
        print(f"ERROR: {e}")
        import traceback
        traceback.print_exc()
    finally:
        word.Quit()

if __name__ == "__main__":
    check_proposal()
