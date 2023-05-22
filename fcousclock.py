# 这是一个执行保活的项目，设定为大约每天执行一次，持续运行20年
import time

def continuous_activity():
    while True:
        # 执行持续的活动
        print("进行持续活动...")
        time.sleep(85000)  # 假设每次活动间隔为 5 秒
    
        # 检查停止条件
        # 如果满足停止条件，则跳出循环
        if stop_condition():
            break

def stop_condition():
    # 编写你自己的停止条件判断逻辑
    # 返回 True 表示满足停止条件，False 表示继续进行活动
    # 在这个示例中，假设活动持续 5 次后停止
    if stop_condition_counter >= 7200:
        return True
    else:
        return False

# 使用示例
stop_condition_counter = 0  # 初始化停止条件计数器

print("开始持续活动")
continuous_activity()
print("持续活动结束")
