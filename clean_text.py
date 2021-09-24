import re
import pyperclip

filename = '060_chap-06_qm-02_hello-wf.Rmd'
file = open(filename, mode='r')
original_text = file.read()
file.close()

pattern = {}
pattern['div'] = re.compile(r'<div[^>]*>([\s\S]*?)</div>', flags=re.M)

matches = pattern['div'].finditer(original_text)

for match in matches:
    start, end = match.span()

    old = original_text[start:end]
    new = match[1]

    original_text = original_text.replace(old, new)


print(original_text)


# %%

text = pyperclip.paste()
text = f'`r me.t("{text}")`'

pyperclip.copy(text)
print(text)
