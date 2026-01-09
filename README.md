# 🧠 Penyelesaian Masalah 0/1 Knapsack
## Menggunakan Algoritma Backtracking dan Dynamic Programming

**Nessa Denanta Sari (105841110923)**  
**Ilma Aqsari (105841108023)**  
**5C**  

---

## 📌 Deskripsi Proyek
Proyek ini membahas penyelesaian **0/1 Knapsack Problem** pada konteks pemilihan **peralatan medis** dengan kapasitas angkut terbatas. Tujuan utama adalah memaksimalkan nilai manfaat peralatan tanpa melampaui batas kapasitas menggunakan algoritma yang efisien.

Metode yang digunakan:
- Brute Force  
- Backtracking dengan Pruning  
- Dynamic Programming  

Implementasi dilakukan menggunakan **Python**, dilengkapi analisis performa dan visualisasi **State Space Tree**.

---

## 🏥 Deskripsi Proyek
Proyek ini membahas penyelesaian 0/1 Knapsack Problem pada konteks pemilihan peralatan medis dengan kapasitas angkut terbatas. Tujuan utama adalah memaksimalkan nilai manfaat dari peralatan yang dibawa tanpa melebihi batas kapasitas, menggunakan pendekatan algoritmik yang efisien.

Tiga metode digunakan dan dibandingkan:
- Brute Force  
- Backtracking dengan Pruning 
-  Dynamic Programming

Implementasi dilakukan menggunakan Python, dilengkapi dengan analisis performa dan visualisasi State Space Tree.

## 🎯 Identifikasi Masalah
Masalah diklasifikasikan sebagai **0/1 Knapsack Problem** dengan model matematis:

Maksimalkan:
Σ vᵢ xᵢ  

Dengan batasan:
Σ wᵢ xᵢ ≤ W,  
xᵢ ∈ {0,1}

Masalah ini termasuk **NP-Complete**, sehingga pendekatan Brute Force menjadi tidak efisien untuk jumlah item besar.

---

## ⚙️ Alasan Penggunaan Algoritma

### Dynamic Programming
- Menjamin solusi optimal global  
- Menghindari perhitungan ulang  
- Kompleksitas waktu O(n × W)  

### Backtracking dengan Pruning
- Memangkas cabang tidak valid  
- Mengurangi ruang pencarian  
- Lebih efisien dibanding Brute Force  

---

## 🌳 State Space Tree
State Space Tree merepresentasikan seluruh kemungkinan keputusan pemilihan item.

- Node menyimpan total berat dan nilai
- Level merepresentasikan keputusan tiap item
- Node merah menunjukkan pruning
- Node hijau menunjukkan solusi valid

---

## 📊 Data
Data terdiri dari 18 peralatan medis dengan atribut berat dan nilai manfaat. Kapasitas maksimum knapsack adalah **55 kg**.
| No  | Nama Peralatan          | Berat (kg) | Nilai |
| --- | ----------------------- | ---------- | ----- |
| 1   | Alat Tes Darah Portable | 8          | 25    |
| 2   | Mikroskop Digital Mini  | 12         | 40    |
| 3   | Cool Box Vaksin         | 15         | 45    |
| ... | ...                     | ...        | ...   |
| 18  | Meja Medis Lipat        | 20         | 40    |


## 📈 Output Program
Hasil program menampilkan:
- Daftar peralatan medis terpilih
- Total berat dan nilai manfaat maksimum
- Persentase efisiensi pruning

Contoh hasil:
- Total Berat: 54 kg / 55 kg  
- Total Nilai: 285  
- Efisiensi Pruning: ±46,58%  

---

## 🔍 Analisis

### Mengapa Kombinasi Optimal?
Kombinasi terpilih memaksimalkan nilai manfaat tanpa melampaui kapasitas knapsack dan memanfaatkan kapasitas secara efisien.

### Perbandingan Brute Force vs Backtracking
Backtracking mengevaluasi jauh lebih sedikit simpul dibanding Brute Force karena adanya pruning, sehingga lebih efisien secara komputasi.

---

## ✅ Kesimpulan
Algoritma **Backtracking dengan pruning** efektif dan efisien untuk menyelesaikan 0/1 Knapsack. **Dynamic Programming** digunakan sebagai validasi solusi optimal.

Pendekatan ini sangat cocok diterapkan pada permasalahan logistik medis dengan kapasitas terbatas.
