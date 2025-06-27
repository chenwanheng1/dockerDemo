import time
from pathlib import Path


if __name__ == '__main__':
    # 在logs目录下创建个名为docker.log的空文件，验证容器和宿主机是否能进行数据同步
    # 获取当前脚本的路径对象
    # log_file = Path("vol2/1000/home/script/logs/test.log")
    log_file = Path(__file__).resolve().parent.parent / 'logs/dockerTest.log'
    try:
        while True:
            log_entry = f"[{time.ctime()}] hello"
            with open(log_file,"a", encoding="utf-8") as log_f:
                log_f.write(log_entry)
                log_f.close()
            time.sleep(10)
    except PermissionError:
        print(f"[{time.ctime()}] 日志文件操作权限不足")