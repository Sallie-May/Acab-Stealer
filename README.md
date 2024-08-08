# Acab Stealer 
This repository exposes and analyzes a stealer malware that has been hidden in various GitHub projects, often disguised as dualhook in tools, other stealers, and software. The goal is to reveal how this malicious code spreads and to help others identify and avoid it.

Contents:

##  Malware Code Leak: The source code of the stealer.
Files from first payload to the final one:
- `firstpayload.py`
- `dropper.py`
 `gruppe.py`

## Analysis: How it works and how it was hidden.

He's way to hide it is pretty simple. It use `;` to hide inside of python program

- Example :
- `import os                                                                                      :exec("payload")`

# Detection Tips: Ways to spot similar threats in other projects.
- `Always look for any exec/eval call inside of any python file`

Disclaimer:
This project is for educational purposes only. Misuse of this information is prohibited.

RUN IT IN A VM IM NOT RESPONSIBLE FOR YOUR ACTIONS
