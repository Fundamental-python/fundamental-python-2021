"""
type data dyctionary sekedar menghubungkan antara key dan value
KVP = key value pair
dictionary = kamus
"""
kamus_ind_eng = {}
kamus_ind_eng ['anak'] = 'son'
kamus_ind_eng ['istri'] = 'wife'
kamus_ind_eng ['ayah'] = 'father'
kamus_ind_eng ['ibu'] = 'mother'
print (kamus_ind_eng)
print(kamus_ind_eng['anak'])
print(kamus_ind_eng['istri'])
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\natau cara rekomentasi pep 8')
kamus_ind_eng = {'anak': 'son', 'istri' : 'wife', 'ayah': 'father', 'ibu': 'mother'}
print(kamus_ind_eng)
print(kamus_ind_eng['anak'])
print(kamus_ind_eng['istri'])
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('\ncontoh lain:')
print('data ini dikirimkan oleh server gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal' : '2021-01-19',
    'driver_list' : ['eko', 'dwi', 'tri', 'catur']
}
print(data_dari_server_gojek)
print(f"driver di sekitar sini adalah {data_dari_server_gojek['driver_list']}")
print(f"driver #1 adalah {data_dari_server_gojek['driver_list'][0]}")
print(f"driver #4 adalah {data_dari_server_gojek['driver_list'][3]}")

print('\ncontoh lain lagi:')
print('data ini dikirimkan oleh server gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_from_server_gojek = {
    'tanggal' : '2021-01-19',
    'driver_list' : [{'nama': 'eko', 'jarak' : 10},
                     {'nama': 'dwi', 'jarak' : 30},
                     {'nama': 'tri', 'jarak' : 100},
                     {'nama':'catur', 'jarak': 1000}]
}
print(data_from_server_gojek)
print(f"driver di sekitar sini adalah {data_from_server_gojek['driver_list']}")
print(f"driver #1 adalah {data_from_server_gojek['driver_list'][0]}")
print(f"driver #4 adalah {data_from_server_gojek['driver_list'][3]}")
print(f"driver terdekat berjarak {data_from_server_gojek['driver_list'][0]['jarak']} meter")
print(f"driver terjauh berjarak {data_from_server_gojek['driver_list'][3]['jarak']} meter")
print(f"driver terdekat adalah {data_from_server_gojek['driver_list'][0]['nama']}")
print(f"driver terjauh adalah {data_from_server_gojek['driver_list'][3]['nama']}")




