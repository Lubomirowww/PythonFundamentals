def heart_delivery(data):
    current_index_position = 0
    cupids_last_position = 0

    while True:
        command=input().split(' ')
        if command[0] == "Love!":
            break

        index = int(command[1]) + current_index_position
        if index >= len(data):
            index = 0

        if -1 < index < len(data):
            if data[index] > 0:
                data[index] -= 2
                if data[index] == 0:
                    print(f"Place {index} has Valentine' day.")

            else:
                print(f"Place {index} already had Valentine's day.")
        current_index_position = index
        current_index_position = index










nums = list(map(int,input().split('@')))
heart_delivery(nums)