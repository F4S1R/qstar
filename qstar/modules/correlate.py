# qstar/modules/correlate.py
import difflib

def corriger_par_correlation(input_text, recalibrated_text):
    ratio = difflib.SequenceMatcher(None, input_text, recalibrated_text).ratio()
    if ratio < 0.6:
        return input_text + " → " + recalibrated_text
    return recalibrated_text
