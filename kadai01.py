own = list(map(int, input().split()))
n = int(input())
enemy = [list(map(int, input().split())) for i in range(n)]
# [[左上座標], [右上座標], [左下座標], [右下座標]]
own_area = [[own[0], own[1]], [own[0]+own[2], own[1]], [own[0], own[1]+own[3]], [own[0]+own[2], own[1]+own[3]]]
c = 1
for en in enemy:
    enemy_area = [[en[0], en[1]], [en[0]+en[2], en[1]], [en[0], en[1]+en[3]], [en[0]+en[2], en[1]+en[3]]]
    # 自機左 ～ 自機右の領域に敵があれば判定
    if (own_area[0][0] < enemy_area[0][0] and own_area[1][0] > enemy_area[0][0] and own_area[0][1] < enemy_area[0][1] and own_area[2][1]>enemy_area[0][1]):
        print("敵機" + str(c) + "が自機の右側に判定あり")
    # 自機左 ～ 自機右の領域に敵があれば判定
    if (own_area[0][0] < enemy_area[1][0] and own_area[1][0] > enemy_area[1][0] and own_area[0][1] < enemy_area[3][1] and own_area[2][1] > enemy_area[3][1]):
        print("敵機" + str(c) + "が自機の左側に判定あり")
    c+=1
