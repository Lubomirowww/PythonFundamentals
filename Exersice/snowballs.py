n=int(input())

data_quality=0
data=""

for _ in range(n):

    snowball_weight=int(input())
    snowball_time=int(input())
    snowball_quality=int(input())

    best_ball=(snowball_weight / snowball_time) ** snowball_quality

    if best_ball > data_quality:
        data_quality = best_ball
        data = f"{snowball_weight} : {snowball_time} =  {int(best_ball)} ({snowball_quality})"
        # с горният ред пазим стойноста и можем да я променяме динамично

print(data)




#2
# 10
# 2
# 3
# 5
# 5
# 5