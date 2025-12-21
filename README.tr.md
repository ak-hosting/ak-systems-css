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
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v1.0.0/dist/ak-design-system.min.css"
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
