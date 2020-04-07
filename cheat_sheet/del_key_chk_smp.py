import re

# DELキー文字(0x7F)が入ってるかどうか判別する

p = re.compile(r'[\u007F]+')

moji = 'あいう' + '\u007F' + 'dd'
print(moji)
moji2 = 'bb上お'

if p.findall(moji):
  print('見つかった')

if p.findall(moji2):
  print('見つかった')
else:
  print('見つからず')

# 単純な正規表現よりこっちが早い
if '\u007F' in moji:
  print('inでも見つかる!!') 