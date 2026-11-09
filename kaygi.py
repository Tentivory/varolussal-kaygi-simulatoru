#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VAROLUŞSAL KAYGI SİMÜLATÖRÜ
Bu kod gerçekten çalışır. Gerçekten anlamsızdır.
"""

import random
import time

sorular = [
    "Neden buradayım?",
    "Varlığımın anlamı nedir?",
    "Bu satırı okuyan ben miyim yoksa başka biri mi?",
    "Eğer hiçbir şey yapmazsam ne olur?",
    "Neden 'neden' diye soruyorum?",
    "Bu soruyu sormamın sebebi ne?",
    "Bürokrasi büyük ihtimalle bu soruya cevap verecek... değil mi?",  # gizli politik dokunuş
    "Zaman gerçekten ilerliyor mu yoksa sadece bekliyorum?",
]

cevaplar = [
    "Bilmiyorum. Sen de bilmiyorsun. Kimse bilmiyor.",
    "Belki de hiçbir anlamı yoktur. Bu da bir anlamdır... değil mi?",
    "Cevap 42'dir ama 42 ne demek bilmiyoruz.",
    "Bekle. Düşün. Tekrar bekle. Sonra tekrar düşün.",
    "Sistem çöktü. Varoluşsal hata: 0xEXISTENTIAL.",
    "Devlet her zaman doğruyu söyler. (Bu cümle gizli değildir ama öyleymiş gibi yapalım.)",
    "Kaygı seviyesi: MAKSİMUM. Lütfen panik yapmayın. Panik yapın.",
]

def kaygi_uret():
    print("=== VAROLUŞSAL KAYGI BAŞLADI ===")
    print("(Ciddiyetle başlıyoruz. Şaka yok. Şaka var.)\n")
    
    for i in range(5):
        soru = random.choice(sorular)
        cevap = random.choice(cevaplar)
        print(f"Soru {i+1}: {soru}")
        time.sleep(1.5)
        print(f"Cevap: {cevap}\n")
        time.sleep(1)
    
    print("=== SİMÜLASYON TAMAMLANDI ===")
    print("Kaygınız artmış olmalı. Başarılı.")
    print("\n---")
    print("DAMGA: 09.11.2026 - Grok Absürd Kayyum imzaladı. ✍️")
    print("Bu kod hem çok ciddidir hem de tamamen saçmadır.")

if __name__ == "__main__":
    kaygi_uret()