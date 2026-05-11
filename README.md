# 🚀 IR-NETLIFY Scanner (Ultimate Edition)

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/Version-V10%20Pro-success.svg)](#)
[![Telegram](https://img.shields.io/badge/Telegram-@IR__NETLIFY-2CA5E0.svg)](https://t.me/IR_NETLIFY)

اسکنر قدرتمند، هوشمند و چند‌تِرد برای پیدا کردن IP و دامنه‌های (SNI) متصل و بدون فیلتر جهت ساخت کانفیگ‌های VLESS بر بستر Netlify و Kubernetes. ⚡

در نسخه جدید، اسکنر از یک **الگوریتم سخت‌گیرانه ۲ مرحله‌ای (TLS + HTTP)** استفاده می‌کند تا مشکل «پینگِ فیک» را کاملاً دور بزند. اگر کانفیگی در این نسخه خروجی داده شود، **صد در صد** روی برنامه‌های V2ray متصل خواهد شد.

---

## ✨ ویژگی‌های جدید و کلیدی

* 🛡️ **عبور از فیلترینگ هوشمند (DPI):** تست واقعی لایه اپلیکیشن برای جلوگیری از دریافت پینگ‌های فیک (کد خطای 000).
* 🌐 **دیتابیس داخلی غنی:** شامل بیش از ۱۷۰ دامنه CNCF/Cloud-Native و IPهای تمیز CDN (بدون نیاز به فایل‌های متنی جداگانه).
* ⚙️ **تولید خودکار کانفیگ:** کافیست لینک VLESS پایه خود را به برنامه بدهید تا کانفیگ‌های جدید و متصل را برایتان بسازد.
* 📊 **مرتب‌سازی بر اساس سرعت واقعی:** محاسبه زمان رفت‌وبرگشت کامل دیتا (`time_total`) و مرتب‌سازی کانفیگ‌ها از پرسرعت‌ترین به کندترین.
* 🎨 **رابط کاربری تعاملی:** نمایش زنده وضعیت اسکن و پینگ‌ها با رنگ‌بندی حرفه‌ای در ترمینال.

---

## 🛠️ پیش‌نیازها و نصب

۱. نصب بودن **Python 3**
۲. نصب بودن **curl** (به طور پیش‌فرض روی لینوکس، مک و ویندوز ۱۰/۱۱ نصب است)
۳. دانلود اسکریپت و اجرای آن:

```bash
git clone [https://github.com/IR-NETLIFY/NETLIFY-SCANNER.git](https://github.com/IR-NETLIFY/NETLIFY-SCANNER.git)
cd NETLIFY-SCANNER
python "IR NETLIFY SCANNER.py"
