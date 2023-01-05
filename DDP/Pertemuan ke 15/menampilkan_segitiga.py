def segitiga():
  for i in range(1, 7):
    for j in range(1, i +1):
      print("*", end='')
    print('')
  
  tinggi = i
  for k in range(tinggi):
    print("*" * (tinggi-k))
    
print(segitiga())