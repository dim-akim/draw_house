print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x == (w or y)) or ((w <= z) and (y <= w))) is False:
                    print(x, y, z, w)
