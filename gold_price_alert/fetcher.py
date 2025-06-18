### fetcher.py
import requests
from log import log

def get_gold_info():
    log("正在获取黄金价格数据...", "DEBUG")
    try:
        url = "https://api.tanshuapi.com/api/gold/v1/shgold2?key=e2e5b70a2592b2314655e09f3530bf09"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        data = resp.json()
        if data and data.get("code") == 1 and isinstance(data.get("data", {}).get("list", {}), dict):
            gold_info = data["data"]["list"].get("Au9999")
            if gold_info and "price" in gold_info:
                gold_info["price"] = float(gold_info["price"])
                return gold_info
            else:
                log("没有找到 Au9999 的价格数据", "WARNING")
                return None
        else:
            log(f"API 返回异常: {data}", "ERROR")
            return None
    except Exception as e:
        log(f"金价获取失败：{e}", "ERROR")
        return None
