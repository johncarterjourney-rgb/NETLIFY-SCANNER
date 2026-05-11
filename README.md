# 🚀 NETLIFY VLESS Scanner (V2.0.0 Ultimate)

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/Version-V2.0.0-success.svg)](#)
[![Channel](https://img.shields.io/badge/Telegram-@ArchiveTell-2CA5E0.svg)](https://t.me/archivetell)
[![Developer](https://img.shields.io/badge/Developer-Bachelor⚡️-orange.svg)](#)

اسکنر قدرتمند، هوشمند و چند‌تِرد **NETLIFY** برای پیدا کردن IP و دامنه‌های (SNI) متصل و بدون فیلتر جهت ساخت کانفیگ‌های VLESS قطعی. ⚡

در نسخه جدید، این اسکنر از یک **الگوریتم سخت‌گیرانه ۲ مرحله‌ای (TLS + HTTP)** استفاده می‌کند تا مشکل اعصاب‌خردکن «پینگِ فیک» را کاملاً دور بزند. اگر کانفیگی در این اسکنر تایید شود، **صد در صد** روی برنامه‌های V2ray متصل خواهد شد.

---

## ✨ ویژگی‌های کلیدی در آپدیت جدید

* 🛰️ **دور زدن DNS (Shecan Bypass):** امکان انتخاب حالت شکن برای دور زدن مسمومیت DNS قبل از شروع اسکن.
* ⚙️ **کنترل دستی پردازش‌ها (Thread Control):** قابلیت تنظیم تعداد تردها توسط کاربر برای جلوگیری از کرش کردن (خطای Signal 9) در ترموکس اندروید.
* 💻 **نمایش زنده در ترمینال:** نمایش آنی کانفیگ‌های متصل در صفحه ترمینال، علاوه بر ذخیره در فایل.
* 🛡️ **عبور از فیلترینگ هوشمند (DPI):** تست واقعی لایه اپلیکیشن (HTTP Status) برای جلوگیری از دریافت پینگ‌های فیک و دراپ شدن پکت‌ها.
* 🌐 **دیتابیس داخلی غنی:** شامل بیش از ۷۰ دامنه CNCF/Cloud-Native و بیش از ۱۰۰ آی‌پی‌ تمیز CDN (بدون نیاز به فایل‌های متنی جداگانه).
* 🌍 **رابط کاربری تمام انگلیسی:** برای خوانایی بهتر در انواع ترمینال‌ها و سیستم‌عامل‌ها.

---

## 🛠️ پیش‌نیازها و نصب

۱. نصب بودن **Python 3**
۲. نصب بودن ابزار **curl** (به طور پیش‌فرض روی لینوکس، مک و ویندوز ۱۰/۱۱ نصب است)
۳. دانلود اسکریپت و اجرای آن:

```bash
git clone [https://github.com/johncarterjourney-rgb/NETLIFY-SCANNER.git](https://github.com/johncarterjourney-rgb/NETLIFY-SCANNER.git)
cd NETLIFY-SCANNER
python index.py
