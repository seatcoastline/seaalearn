// Sederhana: Menampilkan alert saat form dikirim
document.addEventListener('DOMContentLoaded', function() {
    const contactForm = document.getElementById('contactForm');
    
    if(contactForm) {
        contactForm.addEventListener('submit', function(e) {
            const nama = document.getElementById('inputNama').value;
            // Kita beri notifikasi kecil sebelum berpindah halaman
            console.log("Mengirim data untuk: " + nama);
        });
    }
});

// Efek Scroll Halus untuk Navigasi
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
