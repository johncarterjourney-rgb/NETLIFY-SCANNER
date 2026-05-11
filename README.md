# 🚀 NETLIFY VLESS Scanner (V1 Pro Ultimate)

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/Version-V1%20Pro-success.svg)](#)
[![Channel](https://img.shields.io/badge/Telegram-@ArchiveTell-2CA5E0.svg)](https://t.me/archivetell)
[![Developer](https://img.shields.io/badge/Developer-Bachelor⚡️-orange.svg)](#)

اسکنر قدرتمند، هوشمند و چند‌تِرد **NETLIFY** برای پیدا کردن IP و دامنه‌های (SNI) متصل و بدون فیلتر جهت ساخت کانفیگ‌های VLESS قطعی. ⚡

در نسخه V10 Pro، این اسکنر از یک **الگوریتم سخت‌گیرانه ۲ مرحله‌ای (TLS + HTTP)** استفاده می‌کند تا مشکل اعصاب‌خردکن «پینگِ فیک» را کاملاً دور بزند. اگر کانفیگی در این اسکنر تایید شود، **صد در صد** روی برنامه‌های V2ray متصل خواهد شد.

---

## ✨ ویژگی‌های کلیدی (V1 Pro)

* 🛡️ **عبور از فیلترینگ هوشمند (DPI):** تست واقعی لایه اپلیکیشن (HTTP Status) برای جلوگیری از دریافت پینگ‌های فیک و دراپ شدن پکت‌ها.
* 🌐 **دیتابیس داخلی غنی:** شامل بیش از ۷۰ دامنه CNCF/Cloud-Native و بیش از ۱۰۰ آی‌پی‌ تمیز CDN (بدون نیاز به فایل‌های متنی جداگانه).
* ⚙️ **تولید خودکار کانفیگ:** کافیست لینک VLESS پایه خود را به برنامه بدهید تا کانفیگ‌های جدید و متصل را با اسم اختصاصی برایتان بسازد.
* 📊 **مرتب‌سازی بر اساس سرعت واقعی:** محاسبه زمان رفت‌وبرگشت کامل دیتا (`time_total`) و مرتب‌سازی کانفیگ‌ها از پرسرعت‌ترین به کندترین.
* 🎨 **رابط کاربری تعاملی:** نمایش زنده وضعیت اسکن و پینگ‌ها با رنگ‌بندی حرفه‌ای در ترمینال سیستم شما.

---

## 🛠️ پیش‌نیازها و نصب

۱. نصب بودن **Python 3**
۲. نصب بودن ابزار **curl** (به طور پیش‌فرض روی لینوکس، مک و ویندوز ۱۰/۱۱ نصب است)
۳. دانلود اسکریپت و اجرای آن:

```bash
git clone [https://github.com/johncarterjourney-rgb/NETLIFY-SCANNER.git](https://github.com/johncarterjourney-rgb/NETLIFY-SCANNER.git)
cd NETLIFY-SCANNER
python index.py
