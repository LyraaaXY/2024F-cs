# 每个月的天数，第一维表示平年，第二维表示闰年
day_of_month = [
    [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
]

# 判断是否是闰年
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# 给当前日期加1天
def add_one_day(year, month, day):
    day += 1  # 让day加1
    if day > day_of_month[is_leap_year(year)][month]:  # 如果超过当前月的天数
        month += 1  # 让month加1
        day = 1  # 重置day为1号
    if month > 12:  # 如果月份大于12
        year += 1  # 让year加1
        month = 1  # 重置month为1月
    return year, month, day

# 主函数
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 解析输入的日期和天数
    date = data[0].split('-')
    year, month, day = int(date[0]), int(date[1]), int(date[2])
    n = int(data[1])
    
    # 逐天增加日期
    for _ in range(n):
        year, month, day = add_one_day(year, month, day)
    
    # 输出结果
    print(f"{year:04d}-{month:02d}-{day:02d}")

if __name__ == "__main__":
    main()