<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CashLens - Kelola Keuangan Digital</title>
    <!-- Menghubungkan ke file CSS eksternal -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap" rel="stylesheet">
</head>
<body>

    <!-- Navigasi -->
    <nav class="navbar">
        <div class="container nav-content">
            <div class="logo">CashLens</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#produk">Produk</a></li>
                <li><a href="#kontak">Kontak</a></li>
            </ul>
        </div>
    </nav>

    <!-- Home Section -->
    <header id="home" class="hero">
        <div class="container">
            <h1>Kelola Uang Jadi <br><span>Lebih Mudah.</span></h1>
            <p>Bantu lacak pengeluaranmu dengan alat finansial digital yang estetik dan otomatis.</p>
            <div class="btn-group">
                <a href="#produk" class="btn btn-primary">Lihat Produk</a>
                <a href="#about" class="btn btn-outline">Tentang Kami</a>
            </div>
        </div>
    </header>

    <!-- About Section -->
    <section id="about" class="container section">
        <div class="badge">Tentang Kami</div>
        <h2>Mengenal CashLens</h2>
        <div class="about-grid">
            <div class="about-text">
                <p><strong>Nama Usaha:</strong> CashLens Digital</p>
                <p><strong>Latar Belakang:</strong> Kami hadir karena banyak orang merasa aplikasi keuangan terlalu rumit. Kami membuat template yang simpel tapi keren.</p>
            </div>
            <div class="mission-cards">
                <div class="card-mini">
                    <h3>Visi</h3>
                    <p>Membantu anak muda lebih bijak dalam mengatur uang.</p>
                </div>
                <div class="card-mini">
                    <h3>Misi</h3>
                    <p>Menghadirkan produk digital yang terjangkau dan fungsional.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Produk Section -->
    <section id="produk" class="section bg-light">
        <div class="container">
            <h2 class="text-center">Katalog Produk</h2>
            <div class="product-grid">
                {% for p in products %}
                <div class="product-card">
                    <div class="icon-box">💰</div>
                    <h3>{{ p.nama }}</h3>
                    <p>{{ p.deskripsi }}</p>
                    <div class="price">{{ p.harga }}</div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <!-- Kontak Section -->
    <section id="kontak" class="container section">
        <div class="form-container">
            <h2 class="text-center">Hubungi Kami</h2>
            <form action="/submit-kontak" method="POST">
                <div class="form-group">
                    <label>Nama Lengkap</label>
                    <input type="text" name="nama" required placeholder="Nama kamu">
                </div>
                <div class="form-group">
                    <label>Email</label>
                    <input type="email" name="email" required placeholder="email@contoh.com">
                </div>
                <div class="form-group">
                    <label>Pesan</label>
                    <textarea name="pesan" rows="4" placeholder="Apa yang ingin kamu tanyakan?"></textarea>
                </div>
                <button type="submit" class="btn btn-primary w-full">Kirim Pesan</button>
            </form>
        </div>
    </section>

    <footer>
        <p>© 2024 CashLens Digital. Dibuat dengan semangat.</p>
    </footer>

</body>
</html>
