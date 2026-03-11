# ak-systems CSS Framework

ak-systems tarafından hızlı prototipler için geliştirilmiş hafif bir CSS framework'ü.

*Bu belgeyi [English](README.md) | [Deutsch](README.de.md) dillerinde okuyun*

## Kurulum

### Üretim (CDN) - Önerilen

Framework'ü kullanmanın en güvenilir yolu olan jsDelivr CDN'ini kullanın.

```html
<!-- Belirli bir sürümü kullanın (üretim için önerilen) -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@v2.0.2/dist/ak-design-system.min.css"
/>
```

### Geliştirme (Yerel)

Sadece framework'ün kendisine katkıda bulunuyorsanız kullanın.

```html
<link rel="stylesheet" href="dist/ak-design-system.css">
```

### Bleeding Edge (Kararsız)

`main` dalındaki en son değişikliklere ihtiyacınız varsa (üretim için önerilmez):

```html
<!-- Uyarı: Haber verilmeksizin kırılmalara neden olabilir -->
<link
  rel="stylesheet"
  href="https://cdn.jsdelivr.net/gh/ak-hosting/ak-systems-css@main/dist/ak-design-system.min.css"
/>
```

## Sürümleme ve CDN Kullanımı

- **Önerilen:** İstenmeyen güncellemeleri önlemek için sürüm etiketlerine sabitleyin (örn. `.../ak-systems-css@v1.3.2/...`). Bu, biz değişiklik yapsak bile sitenizin tam olarak aynı görünmesini sağlar.
- **Geliştirme:** En son değişiklikleri her zaman almak için `.../ak-systems-css@main/...` kullanın. Sınıf adlarını değiştirirsek bunun düzeninizi bozabileceğini unutmayın.
- Detaylı sürüm geçmişi için [CHANGELOG.md](CHANGELOG.md) dosyasına bakın.
- Yalnızca desteklenen girişler: Geliştirme için `dist/ak-design-system.css` ve üretim/CDN için `dist/ak-design-system.min.css`.

## Derleme (Build) Süreci

`dist/` klasöründeki dosyaları oluşturmak için:

```bash
./build-css.sh
```

`css/ak-design-system/` içindeki CSS dosyaları güncelse ve sadece bundle + minify yapmak istiyorsanız:

```bash
./build.sh
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
<div class="ak-grid ak-grid-3 ak-gap-4">
  <div>Sütun 1</div>
  <div>Sütun 2</div>
  <div>Sütun 3</div>
</div>
```

### Butonlar

```html
<button class="ak-btn">Standart Buton</button>
<button class="ak-btn ak-btn-primary">Birincil Buton</button>
<button class="ak-btn ak-btn-destructive">Yıkıcı Buton</button>

<!-- Modern Varyantlar (Soft, Glass, Gradient, Şekiller) - tam liste için AGENT_CONTEXT.md dosyasına bakın -->
<button class="ak-btn ak-btn-soft-primary ak-btn-rounded">Modern Yuvarlak</button>
```

### Yükleyiciler / Animasyonlar

```html
<!-- Temel Spinner -->
<div class="ak-loader-spinner ak-loader-primary ak-loader-md"></div>

<!-- Nokta Yükleyici -->
<div class="ak-loader-dots ak-loader-primary ak-loader-md">
  <span></span><span></span><span></span>
</div>
```

### Header & Footer Varyantları

```html
<!-- Ortalanmış Header -->
<header class="ak-header ak-header-centered">
  <div class="ak-header-content">
    <nav class="ak-header-nav">...</nav>
    <div class="ak-header-brand">Logo</div>
    <div class="ak-header-actions">...</div>
  </div>
</header>

<!-- Çok Sütunlu Footer -->
<footer class="ak-footer ak-footer-multi-column">
  <div class="ak-footer-content">
    <div class="ak-footer-column">
      <h5 class="ak-footer-column-title">Şirket</h5>
      <a href="#">Hakkımızda</a>
      <a href="#">İletişim</a>
    </div>
  </div>
</footer>
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

## AI / MCP Rehberi

Bu proje, AI ajanları (Codex, Cursor, Claude ve diğer LLM'ler) için bir **Model Context Protocol (MCP)** içerir. MCP, AI ajanlarının tüm kodu analiz etmeden AK Design System ile doğru çalışması için kurallar, zihinsel modeller ve karar mantığı sağlar.

**Dokümantasyon hiyerarşisi:**
- **MCP** ([`docs/ak-design-system.mcp.md`](docs/ak-design-system.mcp.md)): Kurallar, zihinsel model ve karar çerçevesi
- **AGENT_CONTEXT.md** ([`docs/AGENT_CONTEXT.md`](docs/AGENT_CONTEXT.md)): Sınıf listeleri ve kod örnekleri ile teknik referans
- **demo/index.html**: HTML kalıpları için kaynak gerçeği

MCP, AI ajanları tarafından harici kullanım için tasarlanmıştır ve ilkelere ve yapıya odaklanır, AGENT_CONTEXT.md ise spesifik sınıf adları ve uygulama detaylarını içerir.

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
