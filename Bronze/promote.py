with open('promote.in') as fin:
    b_cnt, s_cnt, g_cnt, p_cnt = [list(map(int, item.strip().split(' '))) for item in fin.readlines()]
    
plat = p_cnt[1] - p_cnt[0]
gold = g_cnt[1] - (g_cnt[0] - plat)
silver = s_cnt[1] - (s_cnt[0] - gold)

with open('promote.out', 'w') as fout:
    fout.write(f'{silver}\n{gold}\n{plat}\n')
