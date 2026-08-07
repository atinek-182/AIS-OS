import sys
import re

INVALID_JS_FUNCTIONS = [
    "encodeURIComponent",
    "decodeURIComponent",
    "window",
    "fetch",
    "document",
    "console.log"
]

def validate_notion_formula(formula_str):
    print("========================================================")
    print("ZORIXEL AIOS: Notion Formula 2.0 Local Syntax Validator")
    print("========================================================\n")
    
    # 1. Check parens balance
    open_p = formula_str.count("(")
    close_p = formula_str.count(")")
    if open_p != close_p:
        print(f"[ERROR] Parentheses Mismatch! Open '(': {open_p}, Close ')': {close_p}")
        sys.exit(1)
    print(f"[OK] Parentheses balanced ({open_p} pairs).")
    
    # 2. Check for prohibited JS browser functions
    for fn in INVALID_JS_FUNCTIONS:
        if fn in formula_str:
            print(f"[ERROR] Invalid function '{fn}' detected! Notion Formula 2.0 does not support browser JS functions.")
            print("-> Replace with pre-encoded '%20' (space) or '%0A' (newline) and replaceAll(prop(...), ' ', '%20').")
            sys.exit(1)
    print("[OK] Zero invalid browser JS functions detected.")
    
    # 3. Check for defensive null guards
    if "prop(" in formula_str and "empty(" not in formula_str:
        print("[WARNING] Formula references prop() but contains zero empty() null guards.")
        print("-> Ensure empty database rows do not crash the formula.")
    else:
        print("[OK] Defensive empty() null guards detected.")
        
    print("\n========================================================")
    print("NOTION FORMULA VALIDATION PASSED SUCCESSFULLY!")
    print("========================================================\n")

if __name__ == "__main__":
    test_formula = """if(empty(prop("Phone")), "", if(empty(replaceAll(prop("Phone"), "[^0-9]", "")), "", "https://wa.me/91" + replaceAll(prop("Phone"), "[^0-9]", "") + "?text=Namaste%20" + replaceAll(if(empty(prop("Name")), "Scholar", prop("Name")), " ", "%20") + "%20Ji%2C%0A%0AYour%20order%20status%20is%3A%20" + replaceAll(if(empty(prop("Status")), "New", prop("Status")), " ", "%20") + "%20(Balance%20Due%3A%20INR%20" + if(empty(prop("Balance Due")), "0", format(prop("Balance Due"))) + ")"))"""
    validate_notion_formula(test_formula)
