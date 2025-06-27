# 导入numpy验证docker是否根据requirements文件安装好了依赖
# import numpy as np
import os
if __name__ == '__main__':
    # 在logs目录下创建个名为docker.log的空文件，验证容器和宿主机是否能进行数据同步
    log_file = os.path.abspath('..') + '/logs/docker.log'
    log_entry = "hello docker"
    with open(log_file,"a", encoding="utf-8") as log_f:
        log_f.write(log_entry)
    print(log_entry)