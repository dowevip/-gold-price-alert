# scheduler.py
from datetime import datetime
from config_local import TARGET
from fetcher import get_gold_info
from notifier import send_email
from log import log

query_log = []
has_sent_open_mail = False
has_sent_close_mail = False

def check():
    global has_sent_open_mail, has_sent_close_mail

    now = datetime.now()
    #now = datetime.strptime("2025-06-17 15:30", "%Y-%m-%d %H:%M")

    # 如果是周末，跳过
    if now.weekday() >= 5:
        log(f"⏸ 周末 {now.strftime('%A %H:%M')}，跳过监测", "INFO")
        return

    # 每天早上清除标记（新的一天重新开始）
    if now.hour == 0 and now.minute == 0:
        has_sent_open_mail = False
        has_sent_close_mail = False
        query_log.clear()
        log("🕛 新的一天，重置开盘/收盘提醒标记", "INFO")

    # 如果不在 9:30–15:30 工作时间段
    if now.hour < 9 or (now.hour == 9 and now.minute < 30) or now.hour > 15:
        log(f"⏸ 当前时间 {now.strftime('%H:%M')} 不在监测时段，跳过", "INFO")
        return

    gold_info = get_gold_info()
    if gold_info:
        price = gold_info["price"]
        log(f"当前金价：{price} 元/克", "INFO")
        query_log.append(f"{now.strftime('%H:%M')}：{price} 元/克")
        change_percent = float(gold_info.get("changepercent", "0").replace("%", "").replace("+", "").strip() or 0)

        # 开盘邮件逻辑（只发一次）
        if not has_sent_open_mail and now.hour >= 9 and now.minute >= 30:
            body = (
                f"【开盘提醒】\n"
                f"昨日收盘价：{gold_info.get('lastclosingprice', '未知')} 元/克\n"
                f"今日开盘价：{gold_info.get('openingprice', '未知')} 元/克\n"
                f"当前金价：{price} 元/克"
            )
            send_email("开盘提醒", body)
            has_sent_open_mail = True
            log("✅ 已发送开盘提醒邮件", "SUCCESS")

        # 收盘邮件逻辑（只发一次）
        if not has_sent_close_mail and now.hour == 15 and now.minute >= 30:
            body = (
                    f"【收盘前提醒】\n"
                    f"今日查询记录（共 {len(query_log)} 次）：\n" + "\n".join(query_log)
            )
            send_email("收盘提醒", body)
            has_sent_close_mail = True
            log("✅ 已发送收盘提醒邮件", "SUCCESS")

        # 实时监测价格阈值
        if price < TARGET or abs(change_percent) > 20:
            send_email(f"金价提醒：{price} 元/克", f"当前金价为 {price} 元/克，触发提醒条件")
            log("📬 实时提醒邮件已发送", "SUCCESS")
    else:
        log("❌ 获取金价失败", "ERROR")