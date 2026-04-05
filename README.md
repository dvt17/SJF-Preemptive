# SJF-Preemptive

```bash
BTL/
├── models.py 
├── display.py
├── connectdb.py
└── main.py
```

## Display

### Hàm setupUI()

```py
inputFrame = tk.LabelFrame(self.root, text="Process input", font=("Arial", 10, "bold"), padx=10, pady=10)
inputFrame.pack(fill='x', padx=10, pady=5)
```

- **LabelFrame()**: khởi tạo 1 khung viền:
  - self.root: cửa sổ cha chứa khung viền này và là cửa sổ chính của chương trình
  - text: tên hoặc của khung viền
  - font: điều chỉnh font chữ của text
  - padx: điều chỉnh khoảng trống bên trong theo trục x
  - pady: điều chỉnh khoảng trống bên trong theo trục y
- **pack()**: hiển thị khung viền:
  - fill='x': Tự động kéo dài theo trục x để lấp đầy chiều rộng của cửa sổ
  - padx: điều chỉnh khoảng trống bên ngoài theo trục x
  - pady: điều chỉnh khoảng trống bên ngoài theo trục y

```py
tk.Label(inputFrame, text="Process id (Pid):").grid(row=0, column=0, padx=5, pady=5)
self.pidEntry = tk.Entry(inputFrame, width=10)
self.pidEntry.grid(row=0, column=1, padx=5, pady=5)
```

- **Label()**: tạo ra các nhãn dán hoặc chữ trong khung viền mới khởi tạo ở trên:
  - text: tên hoặc chú thích của nhãn dán
- **grid()**: căn chỉnh theo hàng, cột chính xác hơn: 
  - row: hàng
  - column: cột
- **Entry()**: tạo ra 1 ô trống cho người dùng nhập thông tin vào:
  - width: độ rộng của ô trống
