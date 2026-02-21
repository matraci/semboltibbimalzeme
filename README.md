# SembolTibbi - Medikal Malzeme Web Sitesi

25 yılı aşkın süredir sağlık sektöründe uzmanlaşmış SembolTibbi'nin modern, responsive web sitesidir.

## 📁 Proje Yapısı

```
semboltibbimalzeme/
├── index.html                    # Ana sayfa
├── hakkimizda.html              # Hakkımızda sayfası
├── bakimlar.html                # Bakım rehberleri sayfası
├── iletisim.html                # İletişim sayfası
├── css/
│   └── styles.css               # Tüm stil dosyaları
├── js/
│   ├── data.js                  # Dinamik veri tanımları
│   └── main.js                  # Ana JavaScript dosyası
├── urun/
│   ├── index.html               # Ürünler sayfası
│   └── urun-detay/              # Ürün detay sayfaları
└── upload/                      # Resim ve medya dosyaları
```

## ✨ Özellikler

- **Responsive Tasarım**: Tüm cihazlara uyumlu (mobil, tablet, desktop)
- **Modern UI/UX**: Bootstrap 5 ve özel CSS animasyonları
- **Dinamik İçerik**: JavaScript ile dinamik olarak doldurulabilen içerik
- **SEO Optimized**: Meta etiketleri ve semantic HTML
- **Hızlı Yükleme**: CDN kullanılan harici kaynaklar
- **WhatsApp Entegrasyonu**: Hızlı iletişim butonu
- **Smooth Scrolling**: Sayfa içi navigasyon animasyonları

## 🎨 Bileşenler

### Renkler
- **Primary**: #0d6efd (Mavi)
- **Secondary**: #20c997 (Yeşil)
- **Dark**: #1a1a2e (Koyu gri)
- **Light**: #f8f9fa (Açık gri)

### Sayfalar

1. **index.html** - Ana sayfa
   - Hero bölümü
   - Neden SembolTibbi? (3 özellik)
   - Hizmetlerimiz (3 hizmet)
   - İstatistikler
   - Ürün kategorileri
   - Öne çıkan ürünler

2. **hakkimizda.html** - Şirket hakkında
   - Vizyon, Misyon, Değerler
   - Uzman kadro bilgisi

3. **bakimlar.html** - Bakım rehberleri
   - Ostomi, Yara, Kontinans, Sonda bakım rehberleri
   - SSS ve Uzman desteği

4. **iletisim.html** - İletişim sayfası
   - İletişim bilgileri (telefon, email, adres)
   - İletişim formu
   - Neden biz? bölümü

5. **urun/index.html** - Ürünler sayfası
   - Ürün kategorileri

## 🚀 Kullanım

1. Proje dosyalarını bir web sunucusunda yayınlayın
2. `index.html` dosyasını tarayıcıda açın
3. Navigasyon menüsünden diğer sayfalara göz atın

## 📞 İletişim Bilgileri

- **Telefon**: +90 531 772 1888
- **Email**: info@semboltibbi.com
- **WhatsApp**: [İletişim](https://api.whatsapp.com/send?phone=+905317721888)

## 📝 Notlar

- Resim dosyaları `upload/` klasöründe saklanmalıdır
- Tüm harici kaynaklar CDN üzerinden yüklenmiştir
- JavaScript dosyaları asenkron olarak yüklenir
- Loader animasyonu sayfa yüklenirken gösterilir

## 🔧 Özelleştirme

### Renk Şeması Değiştirmek
`css/styles.css` dosyasındaki `:root` CSS değişkenlerini düzenleyin:

```css
:root {
    --primary: #0d6efd;
    --secondary: #20c997;
    /* ... diğer renkler ... */
}
```

### Dinamik İçeriği Güncellemek
`js/data.js` dosyasındaki ilgili veri arraylerini düzenleyin:
- `featuresData` - Özellikler
- `servicesData` - Hizmetler
- `categoriesData` - Kategoriler
- `productsData` - Ürünler

## 📄 Lisans

© 2025 SembolTibbi. Tüm hakları saklıdır.

## 👨‍💼 Geliştirme

Proje, Bootstrap 5, Font Awesome 6.4.0 ve Swiper 11 kullanılarak geliştirilmiştir.

---

**Son Güncelleme**: Şubat 2025
