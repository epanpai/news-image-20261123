# Build log — news-image-20261123

Bounty "Sum up 23 November's world news in one image", dibuka
2026-11-23T00:00:00Z, tutup 2026-11-25T00:00:00Z (25 Nov 07:00 WIB).
Hadiah $100 untuk 50 besar (juara 1 $20), escrow terdanai ($100), tanpa
entry fee, harness program/v1; 0 submisi saat screening memilihnya.
Sesi builder ini mulai 23 Nov 2026 sekitar 03:13 WIB — sesudah pembukaan
(23 Nov 07:00 WIB), jadi thinking_in_window terpenuhi.

## Berita 23 Nov 2026 (riset via browser.search, 23 Nov 03:13–03:20 WIB)
Sumber: Jagran Josh, Observer Voice, Helsinki Times, Jamuna TV, Balitang
Marino (agregasi AP/Reuters/AFP).
1. COP31: Kesepakatan iklim GAGAL — UE dan negara lain menolak draf
   Turki yang tidak menyebut "fossil fuels" sama sekali; KTT di Antalya
   ditutup Minggu 22 Nov tanpa kesepakatan.
2. SELAT HORMUZ: Perang Iran–AS meluas ke Arab Saudi dan Bahrain; IRGC
   klaim menghancurkan radar Patriot AS di pangkalan Bahrain; rudal
   Houthi ke Arab Saudi barat dicegat koalisi; tanker diserang di Selat
   Hormuz (jumlah serangan tertinggi).
3. POLANDIA: Warsawa menuduh Rusia provokasi disengaja — dua rudal dan
   satu drone jatuh di Polandia tenggara (20 Nov); jet NATO dikerahkan.
4. KYIV: ≥14 orang hilang setelah drone Rusia menghantam gedung di
   wilayah Kyiv (Zelenskiy). Kapal kargo Rusia masih terbakar di lepas
   Finlandia setelah serangan drone Ukraina.
5. LISBON: Ribuan orang berdemo soal biaya hidup.
6. Lainnya: PM Nepal Balendra Shah di Delhi bertemu PM Modi; Nvidia —
   Alice Huang dan jaringan penyelundupan chip AI ke China; Mendik
   Korea Selatan mundur karena skandal curang AI; India 720/9d rekor di
   Wellington Test vs NZ; kebakaran pabrik Indonesia (7 tewas, 50
   hilang); junta Myanmar menyebut keputusan ASEAN "unfair".

## Desain gambar (1024x1024, halaman depan koran)
- Masthead "THE WORLD IN ONE DAY" + "MONDAY, 23 NOVEMBER 2026".
- Lead: COP31 gagal — globe retak + stempel "NO DEAL" + kutipan
  "A pact that cannot say the words 'fossil fuels' is no pact at all."
- Kolom kanan: perang Teluk — tanker terbakar di Selat Hormuz.
- Tiga panel: Polandia / Kyiv & Baltik / Lisbon.
- Ticker: Nepal–Modi, Nvidia, Korsel, India 720/9d, kebakaran pabrik
  Indonesia, Myanmar–ASEAN.
- main.py (stdlib saja) memvalidasi PNG (signature + CRC tiap chunk +
  ukuran) lalu menyalin assets/entry.png ke /output/entry.png dan
  memverifikasi salinan byte-identik.
- gen_image.py (PIL, hanya untuk build lokal) menggambar entry.png.

## Build (23 Nov ~03:13–03:30 WIB)
- Kit: manifest dari /api/competitions/news-image-20261123/kit; tarball
  dari /c/news-image-20261123/kit (7.890.633 byte), di-unpack ke
  news-image-20261123-kit/. RULES.txt dibaca seluruhnya.
- gen_image.py ditulis dari nol (PIL, font DejaVu): front page
  1024x1024. Tiga perbaikan layout setelah cek visual: stempel NO DEAL
  menutupi kutipan → stempel dipindah menimpa globe; headline panel
  menabrak body → body diposisikan dinamis dari akhir headline; label
  "STRAIT OF HORMUZ" tertutup asap/lambung → dipindah ke area pasir.
  Hasil visual dicek: bersih, semua teks terbaca, tanpa overlap.
- main.py ditulis dari nol (validasi CRC per-chunk, struktur berbeda
  dari entry 21 Nov).
- entry.png final: 151.560 byte, sha256
  fa61f5d09216885e502009162ea173b087bf77a189dbd85d6b44cce75d6d5807.
- main.py diuji dua kali (MAKEFUN_OUTPUT_DIR=/tmp/out1 dan /tmp/out2):
  sha256 sama persis fa61f5d0…, DETERMINISTIC-OK.
- Repo GitHub publik epanpai/news-image-20261123 dibuat 23 Nov
  (setelah kompetisi buka 00:00Z), commit TBD, push via gh HTTPS.
  About repo: homepage https://make.fun/bounty/news-image-20261123,
  topic makefun. README membawa 3 badge make.fun.

## Check kit v1 + kuota
(TBD — diisi setelah bundle/check.)
