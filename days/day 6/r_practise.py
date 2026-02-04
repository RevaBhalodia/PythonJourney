# sum of n natural no.sum
def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) + n

sum = cal_sum(10)
print(sum)




# print all emenets in list

def print_list(list , idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

chocolates = ["5star","galaxy","lottychcocpie","coco","lollypop"]

print_list(chocolates)

