# ak-systems CSS Framework

ak-systems tarafından hızlı prototipler için geliştirilmiş hafif bir CSS framework'ü.

*Bu belgeyi [English](README.md) | [Deutsch](README.de.md) dillerinde okuyun*

## Kurulum

Tek desteklenen giriş (geliştirme):

```html
<link rel="stylesheet" href="css/ak-design-system/index.css">
```

Üretim/CDN girişi:

```html
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v1.0.1/dist/ak-design-system.min.css"
/>
```

## Kullanım

### Container

```html
<div class="ak-container">
  <!-- İçerik buraya -->
</div>
```

### Grid Sistemi

```html
<div class="ak-row">
  <div class="ak-col">Sütun 1</div>
  <div class="ak-col">Sütun 2</div>
  <div class="ak-col">Sütun 3</div>
</div>
```

### Butonlar

```html
<button class="ak-btn">Standart Buton</button>
<button class="ak-btn ak-btn-primary">Birincil Buton</button>
<button class="ak-btn ak-btn-danger">Tehlike Butonu</button>
```

## Mobil ve Dokunmatik En İyi Uygulamalar

- Önerilen viewport meta etiketi:
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  ```
  Duyarlı breakpoints ve mobile-first davranışı sağlar.
- Mobil için optimize edilmiş bileşenler:
  - Dokunmatik için boyutlandırılmış butonlar ve ikon butonlar
  - Duyarlı grid ve layout davranışı
  - Mobilde sidebar ve footer navigasyon davranışı
- Erişilebilirlik ve hareket:
  - `prefers-reduced-motion` desteği
  - Klavye ve focus-visible desteği

**Öneri:** Özel bileşenler (örn. checkbox, radio, link) için en az 24×24px dokunma hedefleri kullanın. Bu, erişilebilirlik en iyi uygulamalarıyla uyumludur ve framework tarafından zorlanmayan bir kullanım önerisidir.

## Demo

Tüm bileşenleri içeren bir demo sayfasını burada bulabilirsiniz: [ak-systems CSS Demo](https://ak-hosting.github.io/ak-systems-css/demo/)

Not: Demo sayfası, GitHub Pages etkinleştirildiğinde kullanılabilir. O zamana kadar yerel sunucu ile `demo/index.html` dosyasını açabilirsiniz.

## Önemli Notlar

- ak-systems tarafından geliştirilmiştir (Web sitesi: [ak-pro.com](https://ak-pro.com))
- Bu framework değiştirilemez
- Değişiklikler için alt lisanslama izni yoktur
- Hatalar veya zararlar için sorumluluk kabul edilmez

## Lisans

Bu proje [ak-systems CSS Framework License](LICENSE) altında lisanslanmıştır.
- Bu, framework'ü değiştirmek için bir lisans değildir
- Başka bir CSS kullanabilirsiniz, ancak bu framework değiştirilemez
- Herhangi bir hata veya değişiklikten sorumlu değiliz
