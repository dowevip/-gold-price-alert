# log.py
from datetime import datetime
import os

# 日志文件路径（确保与 run.sh 中 LOG 路径一致）
LOG_PATH = "/volume1/homes/dowe/projects/gold_price_alert/log.txt"


def log(msg, level="INFO"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level_icon = {
        "INFO": "ℹ️",
        "SUCCESS": "✅",
        "WARNING": "⚠️",
        "ERROR": "❌",
        "DEBUG": "🐞"
    }.get(level.upper(), "ℹ️")

    formatted = f"[{level_icon} {level}] {now} - {msg}"

    # 输出到控制台
    print(formatted)

    # 追加写入到日志文件
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
    except Exception as e:
        print(f"[❌ ERROR] 无法写入日志文件：{e}")