str1 = 'いろはにほへとちりぬるを'
str2 = 'いろ,はにほ,へ,と,ちりぬる,を'

print('split前 : ', str2)
str2_lst = str2.split(',')
# ['いろ', 'はにほ', 'へ', 'と', 'ちりぬる', 'を']
print('split後 : ', str2_lst)
str2_lst_join = '|'.join(str2_lst)
print('join後 : ', str2_lst_join)
print('')
print('検索対象 : ', str1)

# 前方一致
print('「いろは」と前方一致 : ', str1.startswith('いろは')) # True
print('「あいう」と前方一致 : ', str1.startswith('あいう')) # False
print('「ぬるを」と後方一致 : ', str1.endswith('ぬるを')) # True