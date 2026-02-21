# GitHub'a Push Etme Talimatları

## ⚠️ Ön Koşullar

- Git yüklü olmalı: https://git-scm.com/download/win
- GitHub hesabı: https://github.com
- SSH Key veya Personal Access Token

---

## 📋 Adım 1: Git Bash veya Terminal Açma

### Seçenek A: Git Bash (Önerilen)
```bash
# C:\Users\matra\Documents\GitHub\Semboltibbimalzeme klasöründe sağ tıkla
# "Git Bash Here" seçeneğini seç
```

### Seçenek B: VS Code Terminal
```
Ctrl + ` (Backtick)
```

### Seçenek C: Windows Terminal
```
Windows Terminal açınız ve klasöre gidiniz
```

---

## 🔧 Adım 2: Git Yapılandırması

İlk defa yapıyorsanız, Git kullanıcı bilgilerinizi ayarlayın:

```bash
git config --global user.name "Adınız"
git config --global user.email "email@example.com"
```

Örnek:
```bash
git config --global user.name "Matra"
git config --global user.email "matra@example.com"
```

---

## 📝 Adım 3: Dosyaları Staging'e Ekle

### Tüm dosyaları ekle:
```bash
git add .
```

### Veya belirli dosyaları ekle:
```bash
git add index.html bakimlar.html hakkimizda.html iletisim.html
git add css/ js/ upload/
git add urun/ urun-detay/ kategori/ bakimlar_sayfalari/ urunler/
git add ENTEGRASYON.md README.md sitemap.html
```

---

## 💾 Adım 4: Commit Oluştur

```bash
git commit -m "Semboltibbi website - Full integration and deployment"
```

Veya daha detaylı:
```bash
git commit -m "
- Entegre tüm HTML sayfaları (72+)
- 50+ ürün detay sayfası eklendi
- 11+ bakım rehberi eklendi
- 150+ medya dosyası (resim/logo)
- CSS ve JavaScript dosyaları güncellendi
- Site haritası ve belgelendirme eklendi
- Responsive tasarım ve SEO optimizasyonu
"
```

---

## 🚀 Adım 5: GitHub'a Push Et

### Birinci kez push ederken:
```bash
git branch -M main
git remote add origin https://github.com/matraci/semboltibbimalzeme.git
git push -u origin main
```

### Sonraki push işlemleri:
```bash
git push
```

---

## 🔐 Adım 6: Kimlik Doğrulaması

Git push sırasında şu seçeneklerden birini kullanın:

### Seçenek 1: HTTPS + Personal Access Token (Önerilen)
```bash
# GitHub → Settings → Developer settings → Personal access tokens
# Token oluşturup kopyalayın
# Push sırasında sorulduğunda:
# Username: github_username
# Password: (token'i yapıştırın)
```

### Seçenek 2: SSH Key
```bash
# SSH Key oluşturun:
ssh-keygen -t ed25519 -C "email@example.com"

# Public key'i GitHub'a ekleyin
# GitHub → Settings → SSH and GPG keys → New SSH key
```

### Seçenek 3: GitHub Desktop
1. GitHub Desktop uygulamasını indirin
2. Repo'yu klonlayın
3. Değişiklikleri göreceksiniz
4. Commit ve Push yapın

---

## 📊 Adım 7: Doğrulama

Push tamamlandıktan sonra GitHub'da kontrol edin:

```
https://github.com/matraci/semboltibbimalzeme
```

---

## 🎯 Tam Push Komutu Dizisi

İşleri hızlı yapmak için:

```bash
cd c:\Users\matra\Documents\GitHub\Semboltibbimalzeme

git config --global user.name "Matra"
git config --global user.email "matra@example.com"

git add .

git commit -m "Semboltibbi website - Full integration with 72+ pages and 50+ products"

git push -u origin main
```

---

## ⚠️ Hata Çözümleri

### Hata: "fatal: not a git repository"
```bash
# .git klasörü olmadığı anlamına gelir
# Repository'yi yeniden initialize edin:
git init
git remote add origin https://github.com/matraci/semboltibbimalzeme.git
```

### Hata: "Permission denied (publickey)"
```bash
# SSH key sorunu
# HTTPS kullanın veya SSH key ekleyin
```

### Hata: "everything up-to-date"
```bash
# Değişiklik yok
# Dosya değişikliklerini kontrol edin
git status
```

### Hata: "fatal: The remote origin already exists"
```bash
# Remote zaten tanımlı
git remote -v  # Mevcut remotes'u göster
git remote set-url origin https://github.com/matraci/semboltibbimalzeme.git
```

---

## 📱 VS Code'dan Doğrudan Push

1. VS Code'u açın
2. Sol tarafta **Source Control** seç (Ctrl+Shift+G)
3. **Staged Changes**'te dosyaları göreceksiniz
4. Commit mesajını yazın
5. **✓** simgesine tıklayarak commit yapın
6. **...** menüsünden **Push** seçin

---

## 🔄 Düzenli Push Etme

Değişiklik yaptığında:

```bash
git add .
git commit -m "Açıklaması"
git push
```

---

## 📈 Repository'yi Takip Etme

Diğer insanlar repo'yu klonlamak için:

```bash
git clone https://github.com/matraci/semboltibbimalzeme.git
cd semboltibbimalzeme
python -m http.server 8000
```

---

## ✅ Checklist

- [ ] Git yüklü
- [ ] GitHub hesabı var
- [ ] Personal Access Token veya SSH Key hazır
- [ ] Repository lokal olarak var
- [ ] Git kullanıcı bilgisi ayarlanmış
- [ ] Dosyalar commit edildi
- [ ] Push başarılı

---

**Not**: İlk defa ise talimatları sırasıyla takip edin. Sorularınız varsa GitHub documentation'ı kontrol edin.
