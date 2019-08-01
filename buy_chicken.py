for cocknum in range(102):
    for hennum in range(102 - cocknum):
        for chicknum in range(102 - cocknum - hennum):
            num = cocknum + hennum + chicknum
            sum = cocknum * 5 + hennum * 3 + chicknum * 1 / 3
            if num == 100 and sum == 100:
                print('公鸡数目： %s , 母鸡数目： %s ， 鸡雏数目： %s , 总数目：%s' % (cocknum, hennum, chicknum,num))
