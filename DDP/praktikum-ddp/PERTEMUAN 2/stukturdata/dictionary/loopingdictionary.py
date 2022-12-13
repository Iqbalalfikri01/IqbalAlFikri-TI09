mahasiswa = {
    "nama": "Muhammad Fadhillah Iqbal Al Fikri",
    "matkkul": "Dasar Dasar Pemrograman",
    "nilai": 90
}

#looping nilai (values)
for i in mahasiswa.values():
    print(i)

#looping nilai (keys)
for j in mahasiswa.keys():
    print(j)

#looping nilai menggunakan for, key, values
for key, values in mahasiswa.items():
    print(key, ":", values)