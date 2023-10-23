WATER_MELON_WEIGHT = input()
if int(WATER_MELON_WEIGHT) >= 1 and int(WATER_MELON_WEIGHT) <= 100:
    if int(WATER_MELON_WEIGHT) % 2 == 0 and int(WATER_MELON_WEIGHT)!=2 :
        print('YES')
    else:
        print('NO')
else:
    print('wrong')