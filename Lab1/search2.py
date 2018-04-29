nums = [3, 4, 6, 4, 34, -23, 98]
x = int(input("Enter a number: "))

#must not use count() or in or index()

#linear search
# found = False
#
# for num in nums:
#     if num == x:
#         found = True
#         break
# if found:
#     print("Found")
# else:
    # print("Not found")

for num in nums:
    if num ==x:
        print("Found")
        break
else:
    #neu vong for khong gap break thi chay vao vong else
    print("Not found")
