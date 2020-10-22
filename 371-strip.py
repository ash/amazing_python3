# Removing whitespace

text = '   Hello   '

s = text.strip()
print(f'strip: [{s}]')

s1 = text.rstrip()
print(f'rstrip: [{s1}]')

s2 = text.lstrip()
print(f'lstrip: [{s2}]')
