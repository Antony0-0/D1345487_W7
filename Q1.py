#不用input數值，直接輸入範例就好
x = 121
reverse_number = x >= 0
x_str = str(x)
left, right = 0, len(x_str) - 1
while left < right and reverse_number:
    if x_str[left] != x_str[right]:
        reverse_number = False
    left += 1
    right -= 1
print(reverse_number)