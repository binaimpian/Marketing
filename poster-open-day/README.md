# Poster Open Day – Bina Impian Empire

Poster media sosial (IG & FB, 1080×1350) untuk Open Day Bina Impian Empire, Sabtu 21 November 2026, 9 pagi – 4 petang.

## Poster terkini
`final-v4/bina-impian-empire-open-day-v6.png` (fon fancy, OPEN DAY rapat, no. 014-799 2354)

## Folder
| Folder | Isi |
|---|---|
| `final-v4/` | Poster terkini (v4–v6) + HTML sumber |
| `minimal/` | Poster minimal: gaya kalendar & halaman terselak (biru & kuning) |
| `5-poster/` | 5 konsep poster lengkap dengan team |
| `final-v3/`, `final-v2/`, `final/` | Versi-versi awal |
| `10-konsep/` | 10 konsep gaya poster pertama |
| `brand/` | Logo SVG, PDF logo, QR WhatsApp |
| `team-cut/` | Gambar team sales yang dah dibuang latar hijau (PNG lutsinar) |
| `copywriting.md` | Research ringkas, headline & caption |
| `key.py` | Skrip buang latar skrin hijau |

Gambar asal (`team-raw/`) tidak dimasukkan; salinan asal ada di Google Drive.

## Cara edit & render semula poster
Setiap poster ialah fail `.html`. Edit teks/nombor dalam HTML, kemudian render ke PNG dengan Playwright:

```bash
node -e "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350},deviceScaleFactor:2});await p.goto('file://'+process.cwd()+'/final-v4/poster.html',{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:'poster.png'});await b.close()})()"
```

Nota: QR dalam `brand/qr-whatsapp.svg` dan poster lama masih guna nombor lama (+60 12-379 4335).
