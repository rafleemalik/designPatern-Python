# 🚀 Laporan Design Pattern
## 📝 Raflee Caesar Dano Malik

---

# 🔌 Adapter & Strategy Design Pattern

## 🔷 Adapter Design Pattern

### 📌 Konsep Adapter Design Pattern
**Adapter Pattern** bekerja seperti penerjemah yang membantu dua pihak yang berbeda agar bisa berkomunikasi. 

- **Target** → Antarmuka standar yang diharapkan klien untuk berinteraksi.
- **Adaptee** → Kelas dengan fungsi yang diinginkan, tetapi menggunakan cara berbeda.
- **Adapter** → Jembatan antara Target dan Adaptee sehingga bisa bekerja bersama tanpa perlu mengubah kode asli.

> **Intinya:** Pola ini memungkinkan penggunaan kembali kode tanpa perlu mengubahnya!

![Adapter Design Pattern](https://github.com/user-attachments/assets/3798f760-2359-44bb-b3b2-2f9e97aa44b1)

---

### 📌 Class Diagram

Dalam sistem manajemen karyawan:
- **Employee** adalah kelas utama.
- **Manager, Intern, Engineer** merupakan subclass yang memiliki atribut spesifik.
- **EmployeeAdapter** berperan sebagai perantara antara **Employee** dan antarmuka **IEmployee**.

<img width="883" alt="Class Diagram - Adapter Pattern" src="https://github.com/user-attachments/assets/de2ea333-a0d1-463a-8450-052fe9faf0aa" />

---

### 📌 Use Case Diagram

<img width="519" alt="Use Case Diagram" src="https://github.com/user-attachments/assets/56d850f4-8cd8-4795-9e71-d3f6da226786" />

---

### 📌 Sequence Diagram
Bagaimana sistem menangani input pengguna:
1. Pengguna memasukkan data karyawan ke **Main Program**.
2. **Main Program** memanggil **EmployeeAdapter** untuk membuat objek karyawan.
3. **EmployeeAdapter** menginisialisasi objek **Employee**.
4. Saat informasi karyawan diperlukan, `get_info()` dipanggil pada **EmployeeAdapter**.
5. Data dikembalikan dan ditampilkan ke pengguna.

<img width="951" alt="Sequence Diagram - Adapter Pattern" src="https://github.com/user-attachments/assets/a5600da3-24ad-4814-810e-c746e1290d69" />

---

## 🎯 Strategy Design Pattern

### 📌 Konsep Strategy Design Pattern
Pola ini memungkinkan pemilihan algoritma atau strategi secara **dinamis** tanpa mengubah kode inti.

- **Client** memilih strategi melalui **Context**.
- **Strategy** adalah antarmuka yang menentukan metode strategi.
- **ConcreteStrategy A dan B** adalah implementasi spesifik dari strategi tersebut.

> **Intinya:** Mengubah strategi bisa dilakukan dengan mudah tanpa merombak kode utama!

![Konsep Strategy Design Pattern](https://github.com/user-attachments/assets/f37057c5-0dad-48a0-a99e-ab30be1644a9)

---

### 📌 Class Diagram

- **EmployeeContext** bertindak sebagai perantara.
- **EmployeeStrategy** adalah antarmuka strategi.
- **ManagerStrategy, EngineerStrategy, InternStrategy** adalah implementasi dari strategi.
- **Employee** dan subclassnya memiliki atribut spesifik.

<img width="1038" alt="Class Diagram - Strategy Pattern" src="https://github.com/user-attachments/assets/e967a281-4f17-4f0e-a4c1-a695c6d81fd6" />

---

### 📌 Use Case Diagram

<img width="519" alt="Use Case Diagram" src="https://github.com/user-attachments/assets/140990d1-64d8-4d7d-88f5-80da7e7f1b11" />

---

### 📌 Sequence Diagram
Bagaimana sistem bekerja:
1. **Client** memilih strategi (`set_strategy(ManagerStrategy)`).
2. **EmployeeContext** meneruskan ke strategi yang dipilih.
3. **Strategy** mengambil informasi karyawan.
4. Data dikembalikan dan ditampilkan ke **Client**.

<img width="951" alt="Sequence Diagram - Strategy Pattern" src="https://github.com/user-attachments/assets/d0211a54-3ab2-4438-9ec9-036737070955" />

---

## 🖥️ CLI Apps
### 📌 Tampilan Aplikasi Command Line

**Halaman utama aplikasi:**
<img width="192" alt="Screen Shot 2025-02-11 at 13 52 07" src="https://github.com/user-attachments/assets/5e61e7ca-92b6-4c3d-bbe9-ce8e27d5a3f1" />

**Menambahkan karyawan baru:**
<img width="519" alt="CLI Add Employee" src="https://github.com/user-attachments/assets/d5139071-7fc7-42db-b46d-bd3c51bea370" />

**Melihat data karyawan:**
<img width="519" alt="CLI View Employee" src="https://github.com/user-attachments/assets/a1d129ff-2d4d-4ba4-a272-7e3f81f9069c" />

---

## 📌 Kesimpulan
✅ **Adapter Pattern** → Menghubungkan kelas dengan antarmuka yang tidak kompatibel tanpa mengubah kode asli.
✅ **Strategy Pattern** → Memungkinkan perubahan strategi secara fleksibel tanpa mengubah struktur kode utama.
✅ **Keuntungan:** Meningkatkan modularitas, fleksibilitas, dan keterbacaan kode dalam sistem berbasis **OOP**.

> 💡 Dengan memahami dan mengimplementasikan Design Patterns ini, kita dapat membangun aplikasi yang lebih **scalable** dan **maintainable**!

🚀 **Siap untuk membuat kode yang lebih rapi dan efisien? Let's code smart!**

