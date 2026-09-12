"""
    ----------------Python自动化检测LNMP是否正常--------------------
    代码编写完成日期:  2026.9.12  18:09
    代码编写目的：实践subprocess语句，解决日常排查LNMP的繁琐流程
    代码测试的环境：Centos7.9 LNMP+WordPress
    编写作者：Renzo

"""
import subprocess

url = "http://192.168.11.134"   #业务使用的IP地址
log = "/var/log/nginx/error.log"    #nginx错误日志路径
log2 = "/var/log/mariadb/mariadb.log"   #数据库错误日志路径
log3 = "/var/opt/remi/php74/log/php-fpm/error.log"      #php-fpm错误日志路径

# 用 systemctl 检查 nginx 状态
nginx = subprocess.run(
    ["systemctl", "is-active", "nginx"],
    capture_output=True,
    text=True
)

# 判断结果
if nginx.stdout.strip() == "active":
    print("[OK] Nginx 正在运行")
elif nginx.stdout.strip() != "active":
    subprocess.run(
        ["systemctl", "restart", "nginx"],
    )
    print("[OK] Nginx 没在跑！我已经帮你运行起来了！")

# mariadb服务检查
mariadb = subprocess.run(
    ["systemctl", "is-active", "mariadb"],
    capture_output=True,
    text=True
)
# 判断结果
if mariadb.stdout.strip() == "active":
    print("[OK] Mariadb 正常运行")
elif mariadb.stdout.strip() != "active":
    subprocess.run(
        ["systemctl", "restart", "mariadb"],
    )
    print("[OK] Mariadb 处于关闭状态我帮你启动了！")

# php74-php-fpm检查判断
php = subprocess.run(
    ["systemctl", "is-active", "php74-php-fpm"],
    capture_output=True,
    text=True
)
# 判断结果
if php.stdout.strip() == "active":
    print("[OK] PHP 正常运行")
elif php.stdout.strip() != "active":
    subprocess.run(
        ["systemctl", "restart", "php74-php-fpm"],
    )
    print("[OK] PHP 处于停止状态，我已经帮你启动了！")


#lnmp访问检测
lnmp = subprocess.run(
    ["curl", "-i", url],
    capture_output=True,
    text=True
)
# 判断结果
if lnmp.returncode == 0:
    print(f"[OK] LNMP 能正常访问:{lnmp.returncode}")
elif lnmp.returncode != 0:
    log_file = subprocess.run(
        ["tail","-n","3", log,log2,log3],
        capture_output=True,
        text=True
    )
    print(f"[ERROR] LNMP 无法正常访问:{lnmp.returncode}")
    print(f"错误日志为：{log_file.stdout.strip()}")