Nama: Raisa Diandra Survijanto
NPM: 2206814545
Kelas: PBP E



JAWABAN TUGAS 2

Link adaptable: https://instrumentscatalogue.adaptable.app/main/



1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

    Berikut adalah cara saya mengimplementasikan tiap langkah dari checklist yang disediakan:

    - Membuat sebuah proyek Django baru.
        Pertama-tama harus membuat direktori lokal dan repositori di GitHub. Setelah membuat keduanya, harus melakukan konfigurasi terhadap direktori agar bisa dihubungkan dengan repositori. Kemudian dihubungkan dengan cara membuat branch dan dihubungkan.
        Kemudian, saya membuat direktori instruments_catalogue sebagai direktori utama tempat saya bekerja dan mengaktivasi virtual environment. Saya membuat file requirements.txt untuk diisi dependencies (komponen agar suatu perangkat lunak dapat berfungsi) dan dipasang. Kemudian saya membuat direktori proyek bernama instrument_catalogue.
        Setelah itu saya mengganti allowed hosts agar aplikasi dapat diakses oleh semua dan menjalankan server. Lalu saya menambahkan file .gitignore agar berkas dalam .gitignore tidak masuk ke versi kontrol Git. Terakhir saya melakukan add, commit, dan push agar progress tersimpan dalam Git.

    - Membuat aplikasi dengan nama main pada proyek tersebut.
        Saya membuat aplikasi baru dengan nama main. Setelah menerapkan perintah "python manage.py startapp main" di commands prompt, muncul suatu direktori baru yang disebut direktori aplikasi dengan nama main.

    - Melakukan routing pada proyek agar dapat menjalankan aplikasi main.
        Saya harus mendaftarkan aplikasi main ke dalam proyek agar terhubung dengan proyek. Aplikasi main ditambahkan kepada INSTALLED_APPS di settings.py pertanda dia sudah didaftarkan.
        Setelah itu, saya harus membuat tempat aplikasi akan berjalan. Saya membuat direktori baru dalam direktori aplikasi main, yang bernama templates. Di sana, saya membuat file html baru bernama main.html. Seluruh isi models saya akan ditampilkan di sana.

    - Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib.
        Saya masuk ke models.py dan membuat suatu class baru bernama Item. Kemudian saya menambahkan seluruh atribut wajib pada class tersebut, yaitu name (dengan tipe data character sehingga menggunakan CharField dan maksimal 255 karakter), amount (dengan tipe data integer sehingga menggunakan IntegerField), dan description (dengan TextField). Selain tiga itu, saya menambahkan satu atribut lagi yaitu price (dengan IntegerField). Setelah melakukan hal tersebut, saya melakukan migrasi untuk models agar tersimpan.

    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML.
        Dalam views.py, saya memasukkan data yang ingin saya masukkan. Pertama harus import render dari django.shortcuts. Saya juga import Item dari models.py agar dapat membuat item baru di file ini. Kemudian saya menambahkan fungsi show_main. Saya menambahkan data seperti nama aplikasi, nama saya, kelas saya, dan juga satu contoh data yang akan saya masukkan sesuai atribut di models.py.
        Kemudian, data yang sudah saya buat tentang itemnya saya save dan masukkan ke dalam context. Context berisi tiga variabel yaitu name, class, dan item. Ketiga nama variabel itu akan digunakan dalam main.html agar mempermudah. Terakhir, saya merender context dengan URL tujuan main.html agar data bisa digunakan di main.html.
        Dalam main.html, saya mengatur bagaimana saya menginginkan bentuk tampilan website. Saya ingin membuat tabel untuk menampilkan data dari models.py, jadi saya mengatur style tabel. Judul, nama, dan kelas langsung saya tulis (ukuran judul lebih besar), tetapi data saya masukkan di tabel sehingga saya menggunakan <table>.

    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
        Pertama harus dilakukan import path dari django.urls (untuk pola URL) dan import show_main dari views.py agar bisa dipakai di file ini. Kemudian saya melakukan konfigurasi routing URL aplikasi main dengan cara membuat variabel urlpatterns dan memasukkan fungsi show_main ke dalam menggunakan path.
        Berkas urls.py pada direktori aplikasi main khusus mengatur aplikasi tersebut. Suatu proyek bisa memiliki lebih dari satu aplikasi sehingga harus dihubungkan juga dengan urls.py di direktori proyek. Ini dapat dilakukan dengan menambahkan include pada import karena include digunakan untuk mengimpor URL aplikasi ke proyek.
        Setelah selesai seluruh langkah

    - Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat.
        Deployment di Adaptable dilakukan dengan cara membuka Adaptable, membuat app baru, memilih menggunakan repositori yang sudah ada, memilih Python sebagai template deployment, PostgreSQL sebagai basis data yang akan digunakan, menyesuaikan versi Python, menambahkan Start Command sesuai nama direktori utama, membuat nama untuk aplikasi, mencentang bagian HTTP Listener on Port, dan terakhir melakukan deploy. Deployment akan berjalan memakan beberapa menit, kemudian setelah selesai, website dapat diakses.
        Apabila saya melakukan perubahan pada directory, saya cukup melakukan add, commit, dan push. Jika sudah tersimpan di repositori GitHub, website di Adaptable akan melakukan deploy ulang secara otomatis, dan hasil yang baru akan terlihat di link yang sama apabila deployment sudah selesai.

    - Membuat sebuah README.md.
        Ini adalah file README.md yang saya buat dan berisi jawaban terhadap seluruh pertanyaan serta tautan Adaptable saya.



2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    Berikut adalah bagan yang saya buat:
    ![bagan](bagan.png)



3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

    Virtual environment digunakan agar dependencies yang sudah diatur untuk satu direktori utama ini tidak bertabrakan dengan direktori lainnya. Dengan virtual environment, kita bisa mengatur agar setiap direktori utama dapat memiliki dependencies atau menggunakan packages yang berbeda. Ini berguna apabila kita membuat dua proyek atau lebih yang menggunakan packages yang berbeda.
    Berdasarkan penjelasan di atas, sebenarnya kita bisa membuat aplikasi web berbasis Django tanpa virtual environment, tapi memiliki kelemahan. Kelemahan yang dapat terasa adalah seluruh direktori utama yang kita buat harus menggunakan dependencies dan packages yang sama. Ini akan menyulitkan apabila kita harus membuat dua proyek berbeda yang membutuhkan packages yang berbeda.



4. Jelaskan apakah itu MVC, MVP, MVVM dan perbedaan dari ketiganya.

    MTV adalah Model Template View. Model adalah komponen yang berkaitan dengan data. Template adalah tempat tampilan diatur dan dihubungkan dengan view. View adalah komponen yang mengatur bagaimana data ditampilkan dan interaksi dengan pengguna, menghubungkan antara model dan template.

    Berikut adalah pengertian serta perbedaan antara MVC, MVP, dan MVVM:

    - MVC adalah Model View Controller. Controller adalah komponen yang mengintegrasi model dan view. Seluruh data diambil dari model.

    - MVP adalah Model View Presenter. Presenter adalah komponen yang menerima input pada view, mengirim ke model, dan mengembalikan ke view. Data yang digunakan diminta terlebih dahulu melalui view.

    - MVVM adalah Model View View-Model. View model adalah komponen yang menjadi abstraksi dari view sekaligus menjadi wrapper untuk model agar bisa terhubung, view model bekerja secara dua arah. MVVM mirip dengan MVP, tetapi view model akan memanipulasi data terlebih dahulu baru dikirim kembali ke view.



Referensi:
Lalani, S. (2022, May 9). MVC vs MVP vs MVVM - Top 10 Differences You Should Know. Xperti. https://xperti.io/blogs/mvc-vs-mvp-vs-mvvm/
tereško. (2012, August 9). What are the differences between MVC, MVP and MVVM? Stack Overflow. https://stackoverflow.com/questions/11877575/what-are-the-differences-between-mvc-mvp-and-mvvm 
