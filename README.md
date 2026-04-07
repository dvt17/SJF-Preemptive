# SJF-Preemptive

```bash
BTL/
├── models.py 
├── display.py
├── connectdb.py
└── main.py
```

## Display

### Hàm setupUI(self)

```py
inputFrame = tk.LabelFrame(self.root, text="Process input", font=("Arial", 10, "bold"), padx=10, pady=10)
inputFrame.pack(fill='x', padx=10, pady=5)
```

- **LabelFrame()**: khởi tạo 1 khung viền:
  - self.root: cửa sổ cha chứa khung viền này và là cửa sổ chính của chương trình.
  - text: tên hoặc của khung viền.
  - font: điều chỉnh font chữ của text.
  - padx: điều chỉnh khoảng trống bên trong theo trục x.
  - pady: điều chỉnh khoảng trống bên trong theo trục y.
- **pack()**: hiển thị khung viền:
  - fill='x': Tự động kéo dài theo trục x để lấp đầy chiều rộng của cửa sổ.
  - padx: điều chỉnh khoảng trống bên ngoài theo trục x.
  - pady: điều chỉnh khoảng trống bên ngoài theo trục y.

```py
tk.Label(inputFrame, text="Process id (Pid):").grid(row=0, column=0, padx=5, pady=5)
self.pidEntry = tk.Entry(inputFrame, width=10)
self.pidEntry.grid(row=0, column=1, padx=5, pady=5)
```

- **Label()**: tạo ra các nhãn dán hoặc chữ trong khung viền mới khởi tạo ở trên:
  - text: tên hoặc chú thích của nhãn dán.
- **grid()**: căn chỉnh vị trí theo hàng, cột chính xác hơn: 
  - row: hàng.
  - column: cột.
- **Entry()**: tạo ra 1 ô trống cho người dùng nhập thông tin vào:
  - width: độ rộng của ô trống.

```PY
addData = tk.Button(inputFrame, text="Add", command=self.addProcess, bg="#54F25A", fg="White")
addData.grid(row=0, column=6, padx=8, pady=8)
```

- **Button**: tạo ra 1 nút bấm cho người dùng thao tác với chức năng của nó.
  - text: tên của nút bấm.
  - command: là chức năng của nút bấm khi liên kết nút bấm với một hàm (phương thức) là addProcess . Khi người dùng click vào nút này, chương trình sẽ tự động gọi hàm self.addProcess để thực thi lệnh.
  - bg: màu nền của nút bấm(background).
  - fg: màu chữ của text.

```py
tableFrame = tk.Frame(self.root)
tableFrame.pack(fill="both", expand=True, padx=10, pady=10)
columns = ("PID", "AT", "BT", "CT", "TAT", "WT", "RT")
self.tree = ttk.Treeview(tableFrame, columns=columns, show="headings", height=8)
for col in columns:
    self.tree.heading(col, text=col)
    self.tree.column(col, anchor="center", width=100)
self.tree.pack(fill="both", expand=True)
```

- **Frame**: tạo ra 1 khung để tạo bảng hiển thị dữ liệu.
- **pack()**: hiển thị khung.
  - fill: khung giãn ra lấp đầy khung theo chiều (both: là cả 2 chiều).
  - expand: cho phép giãn theo khung chương trình.
- **Treeview**: tạ ra widget dạng bảng:
  - columns: tạo ra danh sách các cột.
  - show: giúp ẩn các cột hay khoảng trống bên trái của Treeview.
  - height: độ cao của bảng
- **heading**: gán tên lên mỗi cột  tiêu đề.
- **column**: căn chỉnh cột.
  - anchor: căn lề chữ (center: căn giữa).
  - width: độ rộng của cột.

```py
self.avgTATLabel = tk.Label(avgFrame, text="Average TAT: 0.0 ms", font=("Arial", 10, "bold"))
self.avgTATLabel.pack(side="left", padx=20)
```

- font: xét phông chữ, cỡ chữ và định dạng của chữ.
- side: đẩy khung nhãn về bên phía tận cùng trái(hoặc phải) của khung.

```py
self.canvas = tk.Canvas(ganttFrame, height=100, bg="white")
self.canvas.pack(fill="x")
```

- **Canvas**: tạo ra 1 widget cho phép vẽ các hình học(hình chữ nhật, đường thẳng,..).

### Hàm saveProcessToDB(self, process)
