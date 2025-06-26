# 导入numpy验证docker是否根据requirements文件安装好了依赖
import os
from pathlib import Path
import time
import numpy as np

if __name__ == '__main__':
    # 在logs目录下创建个名为docker.log的空文件，验证容器和宿主机是否能进行数据同步
    log_file = Path(os.path.abspath('..') + "/logs/docker.log")
    try:
        if log_file.exists():
            log_file.unlink()  # 删除旧日志
            print(f"[{time.ctime()}] 已删除旧日志文件")
        log_file.touch()  # 创建新日志文件
        print(f"[{time.ctime()}] 已创建新日志文件")
    except PermissionError:
        print(f"[{time.ctime()}] 日志文件操作权限不足")

    print("hello docker")