# Auto Code Review

Aplikasi otomatis untuk melakukan review dan perbandingan kode menggunakan SSIM (Structural Similarity Index) dan AI agent untuk analisis mendalam.

## 🎯 Fitur Utama

- **Perbandingan Kode Otomatis**: Menggunakan algoritma SSIM untuk mengukur similarity antar file kode
- **AI-Powered Review**: Mengintegrasikan AI agent untuk memberikan analisis dan feedback yang mendalam
- **Batch Processing**: Dapat memproses multiple test cases sekaligus
- **Detailed Reporting**: Menghasilkan report lengkap dalam file `results.txt`

## 📁 Struktur Project

```
project-root/
├── main.py                 # Entry point aplikasi
├── compare.py             # Modul untuk perbandingan kode
├── agent.py               # AI agent untuk code review
├── knowledge_base/
│   └── prompt.txt         # Template prompt untuk AI agent
├── test_cases/
│   ├── original.py        # File kode original
│   ├── identical.py       # File identik dengan original
│   ├── whitespace_changed.py    # File dengan perubahan whitespace
│   ├── variable_renamed.py      # File dengan variable yang di-rename
│   └── structure_changed.py     # File dengan perubahan struktur
└── results.txt           # Output file hasil review (auto-generated)
```

## 🚀 Cara Penggunaan

### Prerequisites

Pastikan Anda memiliki:
- Python 3.x
- Semua dependencies yang diperlukan (sesuai dengan modules yang diimport)
- File-file test cases dalam folder `test_cases/`
- File prompt template di `knowledge_base/prompt.txt`

### Menjalankan Aplikasi

```bash
python main.py
```

### Output

Aplikasi akan menghasilkan file `results.txt` yang berisi:
- Score SSIM untuk setiap perbandingan
- Analisis mendalam dari AI agent
- Feedback dan rekomendasi untuk setiap pasangan kode

## ⚙️ Alur Kerja Aplikasi

1. **Inisialisasi**: Membuat file `results.txt` jika belum ada
2. **Load Test Cases**: Memuat daftar pasangan file yang akan dibandingkan
3. **File Validation**: Memverifikasi keberadaan file sebelum processing
4. **Code Comparison**: 
   - Menggunakan fungsi `compare_code_files()` untuk mendapatkan SSIM score
   - Mengekstrak source code dari kedua file
5. **AI Analysis**:
   - Memuat prompt template dari `knowledge_base/prompt.txt`
   - Menggabungkan prompt, source code, dan SSIM score
   - Menjalankan AI agent untuk analisis mendalam
6. **Report Generation**: Menyimpan hasil analisis ke `results.txt`

## 📊 Test Cases

Aplikasi saat ini dikonfigurasi untuk menguji 4 skenario perbandingan:

| Test Case | Deskripsi | Tujuan |
|-----------|-----------|---------|
| `original.py` vs `identical.py` | File yang identik | Baseline untuk score maksimal |
| `original.py` vs `whitespace_changed.py` | Perubahan whitespace/formatting | Uji sensitivitas terhadap formatting |
| `original.py` vs `variable_renamed.py` | Perubahan nama variable | Uji deteksi perubahan semantik minor |
| `original.py` vs `structure_changed.py` | Perubahan struktur kode | Uji deteksi perubahan struktural major |

## 🔧 Kustomisasi

### Menambah Test Cases

Edit list `test_cases` di `main.py`:

```python
test_cases = [
    ("/test_cases/file1.py", "/test_cases/file2.py"),
    # Tambahkan pasangan file baru di sini
]
```

### Mengubah Prompt AI

Edit file `knowledge_base/prompt.txt` untuk menyesuaikan instruksi kepada AI agent.

### Lokasi Output

Hasil review disimpan di `results.txt`. Untuk mengubah lokasi, modifikasi path di bagian file handling.

## 📝 Format Output

```
SSIM Scores:
Comparing code snippets...
------
[AI Agent Analysis untuk perbandingan pertama]
SSIM between /test_cases/original.py and /test_cases/identical.py: 0.95
------
[AI Agent Analysis untuk perbandingan kedua]
SSIM between /test_cases/original.py and /test_cases/whitespace_changed.py: 0.87
...
```

## 🛠️ Troubleshooting

### File Not Found Error
- Pastikan semua file test cases ada di folder `test_cases/`
- Periksa nama file dan path yang benar
- Pastikan working directory sudah benar

### AI Agent Error
- Verifikasi konfigurasi AI agent di `agent.py`
- Pastikan file `knowledge_base/prompt.txt` ada dan readable
- Periksa koneksi internet jika menggunakan API external

### Permission Error
- Pastikan aplikasi memiliki permission untuk write file `results.txt`
- Periksa permission folder dan file yang terlibat

## 🤝 Kontribusi

Untuk berkontribusi pada project ini:
1. Fork repository
2. Buat feature branch
3. Commit perubahan Anda
4. Push ke branch
5. Buat Pull Request

## 📄 Lisensi

[Sesuaikan dengan lisensi yang Anda pilih]

---

**Note**: Pastikan semua dependencies sudah terinstall dan konfigurasi AI agent sudah benar sebelum menjalankan aplikasi.