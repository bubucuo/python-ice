str='0123456789'
# index是索引，从0开始，-1表示最后一个字符, [是包含，)是不包含, n是字符串长度
print(str[0:-1])           
print(str[0])            
print(str[2:5:2])            # [2,5)
print(str[2:])             # [2, n)


print(len(str))