<h1 align="center">E-commerce Data ETL Project</h1>

<p align="center">
  Mini project untuk data engineering yang mengimplementasikan proses ETL (Extract, Transform, Load) pada dataset e-commerce. 
  <br>
  Proyek ini mengolah data transaksi e-commerce dan menyediakan analisis dasar untuk insight bisnis.
</p>

<h2>📁 Struktur Proyek</h2>

<pre>
mini-project-1/
│
├── etl/                    # Modul ETL
│   ├── __init__.py
│   ├── extract.py         # Proses ekstraksi data
│   ├── transform.py       # Proses transformasi dan cleaning data
│   ├── load.py           # Proses loading data ke CSV/MySQL
│   └── schema.py         # Schema database
│
├── analysis/              # Modul analisis
│   └── queries.py        # Query-query untuk analisis data
│
├── config.py             # Konfigurasi proyek
├── main.py              # Entry point utama
└── run_analysis.py      # Script untuk menjalankan analisis
</pre>

<h2>✨ Fitur</h2>

<ul>
  <li>Ekstraksi data dari file CSV</li>
  <li>Transformasi data:
    <ul>
      <li>Penghapusan duplikasi</li>
      <li>Penanganan missing values</li>
      <li>Konversi format tanggal</li>
      <li>Penambahan kolom kalkulasi</li>
      <li>Filter transaksi valid</li>
    </ul>
  </li>
  <li>Loading data ke:
    <ul>
      <li>File CSV</li>
      <li>Database MySQL</li>
    </ul>
  </li>
  <li>Analisis data dasar:
    <ul>
      <li>Total penjualan per customer</li>
      <li>Produk terlaris</li>
      <li>Penjualan per negara</li>
      <li>Tren penjualan bulanan</li>
    </ul>
  </li>
</ul>

<h2>🔧 Prasyarat</h2>

<ul>
  <li>Python 3.x</li>
  <li>pandas</li>
  <li>sqlalchemy</li>
  <li>mysql-connector-python</li>
</ul>

<h2>⚡ Instalasi</h2>

<ol>
  <li>Clone repository ini:
    <pre><code>git clone [URL_REPOSITORY]
cd mini-project-1</code></pre>
  </li>
  <li>Install dependencies:
    <pre><code>pip install pandas sqlalchemy mysql-connector-python</code></pre>
  </li>
  <li>Sesuaikan konfigurasi database di <code>config.py</code></li>
</ol>

<h2>🚀 Penggunaan</h2>

<ol>
  <li>Menjalankan proses ETL:
    <pre><code>python main.py</code></pre>
  </li>
  <li>Menjalankan analisis:
    <pre><code>python run_analysis.py</code></pre>
  </li>
</ol>

<h2>💾 Struktur Database</h2>

<p>Tabel <code>transactions</code>:</p>
<ul>
  <li>id (Primary Key)</li>
  <li>InvoiceNo</li>
  <li>StockCode</li>
  <li>Description</li>
  <li>Quantity</li>
  <li>InvoiceDate</li>
  <li>UnitPrice</li>
  <li>CustomerID</li>
  <li>Country</li>
  <li>TotalAmount</li>
  <li>Year</li>
  <li>Month</li>
  <li>DayOfWeek</li>
</ul>

<p>Index yang digunakan:</p>
<ul>
  <li>idx_customer (CustomerID)</li>
  <li>idx_invoice (InvoiceNo)</li>
  <li>idx_date (InvoiceDate)</li>
  <li>idx_country (Country)</li>
</ul>

<h2>🤝 Kontribusi</h2>

<p>Silakan berkontribusi dengan membuat pull request. Untuk perubahan besar, harap buka issue terlebih dahulu untuk mendiskusikan perubahan yang diinginkan.</p>

<h2>📝 License</h2>

<p><a href="https://choosealicense.com/licenses/mit/">MIT License</a></p>
