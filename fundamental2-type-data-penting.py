print('type data skalar/ type data sederhana')
anak1 = 'eko'
anak2 = 'dwi'
anak3 = 'tri'
anak4 = 'catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntype data list/ daftar/ array')
anak = []
anak.append('eko')
anak.append('dwi')
anak.append('tri')
anak.append('catur')
print(anak)

print('\natau...')
anakku = ['eko', 'dwi', 'tri', 'catur']
print(anakku)
anakku.append ('limo')
print(anakku)

print('\nmenyapa anak tertentu')
print(f'halo {anakku[0]}')
print(f'halo {anakku[1]}')
print(f'halo {anakku[2]}')
print(f'halo {anakku[3]}')
print(f'halo {anakku[4]}')

print('\nmenyapa semua anak')
my_son = ['eko', 'dwi', 'tri', 'catur']
my_son.append ('limo')
for m in my_son:
    print(f'haloooo {m}')

print('\nsapa semua anak cara ribet')
for m in range (0, len (my_son)):
    print(f'{m+1}. haloooo {my_son[m]}')

