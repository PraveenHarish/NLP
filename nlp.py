import re
def detect_word_pattern(pat,txt):
    result=re.findall(pat,txt)
    if result:
        print("Pattern Detected")
        for i in result:
            print(i)
    else :
        print("No Pattern Detected")
sample_inputs=[
    (r"\bP\w+","Python is programming language"),
    (r"\b\d{4}\b","He was born in the year of 2006"),
    (r"\bing\b","Playing cricket is good")
]
for pat,txt in sample_inputs:
    print("Pattern :",pat)
    print("Text :",txt)
    detect_word_pattern(pat,txt)
    print("*"*50)