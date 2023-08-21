#!/usr/local/bin/python
import glob

import re

blocked = "/etc/passwd|flag.txt|proc"
banned = "import|chr|os|sys|system|builtin|exec|eval|subprocess|pty|popen|read|get_data"
search_func = lambda word: re.compile(r"\b({0})\b".format(word), flags=re.IGNORECASE).search
def main():
    print("What would you like to say?")
    for _ in range(2):
        text = input('>>> ').lower()
        block=search_func(blocked)(''.join(text.split("__")))
        check = search_func(banned)(''.join(text.split("__")))

        if check:
            print(f"Nope, we ain't letting you use {check.group(0)}!")
            break
    
        if block:

            print ("you aren't allowed to read that file")
            break
        else:
            try:
                tt = glob.glob(text)[0]
                print(open(tt, "r").read())
            except:
                return "file doesn't exist"
            
         
                
                
if __name__ == "__main__":
    main()
