# main.py
from scheduler import check
import schedule
import time
from log import log

log("✅ main.py 成功开始执行", "SUCCESS")
log("⏳ 启动监测，每小时30分检测一次...", "INFO")

# 启动后立即执行一次
check()

# 每小时 30 分执行一次
schedule.every().hour.at(":30").do(check)

# 调度循环
while True:
    schedule.run_pending()
    time.sleep(1)