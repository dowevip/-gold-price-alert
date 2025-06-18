金价提醒系统（Gold Price Alert System）
========================================

简介（Introduction）
--------------------
本项目是一个自动化的金价监测与邮件提醒系统，支持工作日内定时获取上海黄金交易所Au99.99金价，并在满足条件时发送邮件提醒，包括：
- 每日开盘提醒（09:30 后）
- 实时价格低于预设阈值提醒
- 每日收盘前汇总提醒（15:30 后）

This project is an automated gold price monitoring and email alert system. It fetches Au99.99 prices from the Shanghai Gold Exchange on weekdays and sends alerts based on defined conditions:
- Daily market opening alert (after 09:30)
- Real-time alert if price drops below a set threshold
- Daily pre-close summary (after 15:30)

功能（Features）
--------------------
- ⏰ 定时运行：每小时整点+30分自动监测
- 📩 邮件通知：通过 Gmail 发送多收件人提醒邮件
- 📊 支持开盘价、实时价、涨跌幅等数据展示
- ✅ 本地运行，结构清晰、便于部署和维护

- ⏰ Scheduled checks: runs every hour at :30
- 📩 Email notifications: sent via Gmail to multiple recipients
- 📊 Shows opening price, current price, price change percentage
- ✅ Runs locally, clean modular structure, easy to deploy and maintain

使用说明（Usage）
--------------------
1. 克隆项目：
   git clone https://github.com/你的用户名/gold-price-alert.git

2. 进入项目目录，创建虚拟环境并安装依赖：
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

3. 配置邮箱和阈值（修改 `config.py`）：
   - 收件邮箱列表
   - 发件邮箱 SMTP、授权码
   - 价格提醒阈值 TARGET

4. 启动程序（运行一次立即执行一次检测，并进入定时监测循环）：
   python gold_price_alert/main.py

说明：如需后台运行建议使用 `screen` 或 `nohup` 等工具。

To run:
1. Clone this repo and enter the project folder
2. Create venv, install requirements
3. Modify `config.py` with your email + price threshold
4. Run `python gold_price_alert/main.py`

其他（Others）
--------------------
- 所有日志保存在 log.txt（如目录存在）
- 当前仅支持上海黄金交易所 Au99.99 数据源
- 如需部署在 NAS，请调整路径与定时策略

LICENSE
--------------------
MIT License

作者（Author）：@dowevip
