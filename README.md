# 🦠 VirusTotal Dosya İndirici | VirusTotal File Downloader

<div align="center">

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![VirusTotal API](https://img.shields.io/badge/VirusTotal-API-red.svg)](https://developers.virustotal.com/)

</div>

Modern bir Python uygulaması ile VirusTotal'dan dosya indirin.
Download files from VirusTotal with a modern Python application.

## 🚀 Özellikler | Features

- 🎯 Kolay kullanım | Easy to use
- 💻 Modern komut satırı arayüzü | Modern CLI interface
- 🔄 İlerleme göstergesi | Progress indicator
- 🎨 Renkli çıktılar | Colored output
- 🛡️ Hata yönetimi | Error handling

## 📋 Gereksinimler | Requirements

- Python 3.7+
- VirusTotal Premium API Key

## ⚙️ Kurulum | Installation

```bash
# Depoyu klonlayın | Clone the repository
git clone https://github.com/yourusername/virustotal-downloader.git
cd virustotal-downloader

# Gerekli paketleri yükleyin | Install required packages
pip install -r requirements.txt

# API anahtarınızı ayarlayın | Set your API key
# vt_downloader.py dosyasında API_KEY değişkenini güncelleyin
# Update API_KEY variable in vt_downloader.py
```

## 🎮 Kullanım | Usage

### Temel Kullanım | Basic Usage
```bash
python vt_downloader.py HASH_DEGERI
```

### Örnek | Example
```bash
python vt_downloader.py 44d88612fea8a8f36de82e1278abb02f
```

### Özel Dizine İndirme | Custom Output Directory
```bash
python vt_downloader.py HASH_DEGERI --output-dir başka_dizin
```

## 📝 Parametreler | Parameters

- `HASH_DEGERI`: İndirilecek dosyanın hash değeri (zorunlu) | File hash to download (required)
- `--output-dir`, `-o`: Dosyanın indirileceği dizin (varsayılan: "downloads") | Output directory (default: "downloads")

## ⚠️ Önemli Not | Important Note

Bu uygulama VirusTotal Premium API gerektirmektedir. Ücretsiz API anahtarları ile dosya indirme işlemi yapılamaz.

This application requires a VirusTotal Premium API. File downloading is not available with free API keys.

## 📜 Lisans | License

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Katkıda Bulunma | Contributing

1. Fork edin | Fork it
2. Yeni bir branch oluşturun | Create your feature branch
3. Değişikliklerinizi commit edin | Commit your changes
4. Branch'inizi push edin | Push to the branch
5. Bir Pull Request oluşturun | Create a new Pull Request 