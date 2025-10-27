# Simple Form Data API

<details>
<summary>Task Description</summary>

Bangun sebuah server sederhana menggunakan Node.js atau framework Express.
Buatlah endpoint API yang dapat menerima data formulir dari frontend pada hari
pertama dan menyimpannya ke dalam sebuah penyimpanan data sederhana, misalnya
dalam bentuk array di dalam server. Pastikan bahwa server dapat mengembalikan data
yang telah disimpan ketika diminta oleh frontend.


Kriteria Penilaian:
- Penggunaan Node.js atau Express untuk mengembangkan server.
- Desain endpoint API yang baik.
- Kemampuan server untuk menerima, menyimpan, dan mengembalikan data.
</details>


## Overview

This submodule implements a simple **Node.js / Express server** to accept, store, and return form data from the frontend.  

---

## Prerequisites
- Docker >= 24.0 (optional, for containerized deployment)  
- Internet connection to download image from Docker registry

---

## Installation & Setup

```bash
git clone https://github.com/username/huawei-technical-test-I.git
cd huawei-technical-test-I/pengembangan-backend
chmod +x run.sh && ./run.sh (or you can execute 'docker-compose up --build' directly)
open http://localhost:5556/api-docs/ and test APIs on swagger
```