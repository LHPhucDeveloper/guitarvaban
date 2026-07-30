# Kỷ Yếu Điện Tử - "CHÚNG TA CỦA NHỮNG NĂM ẤY"
### Kỷ niệm 05 năm thành lập CLB Guitar và Bạn (01/08/2021 – 01/08/2026)

---

## 🌟 Cải Tiến Mới Nhất

1. **Phông Chữ Tiếng Việt Cao Cấp**:
   - Sử dụng `Be Vietnam Pro` cho phần thân văn bản (cực kỳ rõ nét, chuẩn tiếng Việt).
   - Sử dụng `Cormorant Garamond` & `Lora` cho tiêu đề và tạp chí nghệ thuật.
   - Thêm font chữ ký `Caveat` cho phần chữ ký của Founder.

2. **Căn Đều Văn Bản (Text Justification)**:
   - Tất cả các đoạn văn thư ngỏ, hồi ký, câu chuyện đều được căn đều 2 bên (`text-align: justify; text-justify: inter-word;`) mang lại trải nghiệm đọc tạp chí in ấn cao cấp.

3. **Hiệu Ứng Cuộn Trang Apple Smooth Reveal**:
   - Các phần tử mượt mà trượt nhẹ từ dưới lên và mờ dần (Fade-in & Scale) khi cuộn trang, sử dụng đường cong gia tốc chuẩn Apple `cubic-bezier(0.16, 1, 0.3, 1)`.

4. **Thanh Tiến Trình Cuộn Apple Progress Header**:
   - Rút gọn menu điều hướng cũ thành thanh tiến trình cuộn đọc tinh tế ở mép trên cùng.
   - Hiển thị phần đang đọc trực tiếp (ví dụ: `Đang xem: Phần III: Những Người Giữ Lửa`).

---

## 📁 Cấu Trúc Thư Mục Project

```
/
├── index.html              # Trang chủ chứa toàn bộ 8 Phần Kỷ yếu
├── styles.css              # Hệ thống CSS Design System & Style cho A4 PDF Print
├── script.js               # Đổi giao diện, Tìm kiếm thành viên, Lightbox modal
├── assets/
│   ├── images/
│   │   ├── logo.png        # Logo chính thức của CLB
│   │   ├── members/        # Ảnh 40 thành viên (1.jpeg .. 40.jpeg)
│   │   └── gallery/        # Ảnh hoạt động, offline & giao lưu
└── README.md               # Hướng dẫn sử dụng & xuất PDF A4
```

---

## 🖨️ Hướng Dẫn Xuất File PDF A4 Để In Ấn

1. Mở file `index.html` bằng trình duyệt **Google Chrome** hoặc **Safari**.
2. Nhấn nút **"🖨️ Xuất PDF A4"** ở góc phải thanh menu navigation (hoặc nhấn phím tắt `Cmd + P` trên Mac / `Ctrl + P` trên Windows).
3. Trong cửa sổ xem trước in:
   - **Máy in (Destination)**: Chọn *Save as PDF* (Lưu dưới dạng PDF).
   - **Khổ giấy (Paper size)**: Chọn *A4*.
   - **Tỷ lệ (Scale)**: Chọn *Default* hoặc *100%*.
   - **Đồ họa nền (Background graphics)**: Tích chọn ✅ (Bắt buộc để hiển thị khung nền và màu sắc chuẩn).
4. Nhấn **Save** để tải file PDF kỷ yếu đẹp mắt hoàn chỉnh!
