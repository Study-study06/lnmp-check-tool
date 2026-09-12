# LNMP 巡检工具

一个用 Python 写的 LNMP 服务状态巡检脚本，支持自动检测和恢复。

## 功能
- 检查 Nginx、MariaDB、PHP-FPM 是否在运行
- 服务挂掉时自动重启
- 检测 LNMP 站点是否能正常访问
- 访问异常时自动抓取错误日志

## 用法
```bash
python3 check_lnmp.py
#我的第一个自动化巡检脚本
#This is my first automation script
