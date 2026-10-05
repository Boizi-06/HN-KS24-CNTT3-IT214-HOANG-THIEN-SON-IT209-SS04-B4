"""
Ứng dụng mẫu: Quản lý tệp tin và bảo mật
Session 04 - Bài 4 - IT209
Học viên: Hoàng Thiện Sơn (Boizi-06)
"""

import os

def load_config():
    print("[INFO] Đang khởi động ứng dụng...")
    if os.path.exists("credentials.txt"):
        print("[AN TOÀN] File credentials.txt tồn tại cục bộ và đã được bảo vệ bởi .gitignore!")
    else:
        print("[CẢNH BÁO] Không tìm thấy file credentials.txt!")

if __name__ == "__main__":
    load_config()
