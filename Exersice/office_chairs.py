def office_management(number_of_rooms):
     left_chairs = 0
     condition = True

     for room_number in range (1, number_of_rooms +1):
          data = input().split(" ")
          available_chairs = data[0]
          visitors=int(data[1])
          diff = abs(len(available_chairs)-  visitors)

          if len(available_chairs) < visitors:
              condition = False
              print(f'{diff}more chairs needed in roms{room_number}')
          elif len(available_chairs) > visitors:
              left_chairs += diff

     if condition:
         print (f"Game on, {left_chairs} free chairs left")


info=int(input())
print(office_management(info))



data=int(input())
office_management(data)
