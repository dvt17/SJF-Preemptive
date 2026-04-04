import tkinter as tk
from tkinter import ttk, messagebox
from models import * 
class Display:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU scheduling using SJF Preemptive")
        self.root.geometry("820x600")
        self.processes = []
        
        self.setupUI()
    
    def setupUI(self):
        inputFrame = tk.LabelFrame(self.root, text="Process input",font=("Arial",10,"bold"), padx=10, pady=10)
        inputFrame.pack(fill='x', padx=10, pady=5)

        tk.Label(inputFrame, text="Process id (Pid):").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(inputFrame, text="Arrival Time (AT):").grid(row=0, column=2, padx=5, pady=5)
        tk.Label(inputFrame, text="Burst Time (BT):").grid(row=0, column=4, padx=5, pady=5)

        self.pidEntry = tk.Entry(inputFrame, width=10)
        self.atEntry = tk.Entry(inputFrame, width=10)
        self.btEntry = tk.Entry(inputFrame, width=10)

        self.pidEntry.grid(row=0, column=1, padx=5, pady=5)
        self.atEntry.grid(row=0, column=3, padx=5, pady=5)
        self.btEntry.grid(row=0, column=5, padx=5, pady=5)

        addData = tk.Button(inputFrame, text="Add", command=self.addProcess, bg="#4CAF50", fg= "White")
        clearData = tk.Button(inputFrame, text ="Clear", command=self.clearProcess,bg="#C7A934", fg= "White")
        calculatorData = tk.Button(inputFrame, text="Calculator",command=self.caculatorProcess,bg="#4579E1", fg= "White")
        quitProgram = tk.Button(inputFrame, text="Exit",command=root.quit,bg="#f44336", fg= "White")

        addData.grid(row=0, column=6, padx=8, pady=8)
        clearData.grid(row=0, column=7, padx=8, pady=8)
        calculatorData.grid(row=0, column=8, padx=8, pady =8)
        quitProgram.grid(row=0, column=9, padx=8, pady=8)
        tableFrame = tk.Frame(self.root)
        tableFrame.pack(fil="both", expand=True, padx=10, pady=10)

        columns = ("PID", "AT", "BT", "CT", "TAT", "WT", "RT")
        self.tree = ttk.Treeview(tableFrame, columns=columns, show="headings", height=8 )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100)

        self.tree.pack(fill="both", expand=True)

        avgFrame = tk.Frame(self.root)
        avgFrame.pack(fill="x", padx=10, pady=5)
        self.avgTATLabel = tk.Label(avgFrame, text="Average TAT: 0.0 ms", font=("Arial", 10, "bold"))
        self.avgTATLabel.pack(side="left", padx=20)
        self.avgWTLabel = tk.Label(avgFrame, text="Average WT: 0.0 ms", font=("Arial", 10, "bold"))
        self.avgWTLabel.pack(side="left", padx=20)
        self.avgRTLabel = tk.Label(avgFrame, text="Average RT: 0.0 ms", font=("Arial", 10, "bold"))
        self.avgRTLabel.pack(side="left", padx=20)

        ganttFrame = tk.LabelFrame(self.root, text="Gantt Chart (SFRT)",font=("Arial", 10, "bold"), padx=10, pady=10)
        ganttFrame.pack(fill="x", padx=10, pady=5)

        self.canvas = tk.Canvas(ganttFrame, height=100, bg="white")
        self.canvas.pack(fill="x")

        self.adverLabel = tk.Label(root, text="Awaiting data...", font=("Arial", 10, "bold"))
        self.adverLabel.pack(pady=5)

    def addProcess(self):
        try:
            pid = self.pidEntry.get()
            at = int(self.atEntry.get())
            bt = int(self.btEntry.get())
            
            if not pid: raise ValueError
            if at < 0 or bt <= 0:
                messagebox.showerror("ERROR", "AT must >= 0 and BT must > 0")
                return
            
            self.processes.append(Process(pid, at, bt))
            self.tree.insert("", "end", values=(pid, at, bt, "-", "-", "-"))
            
            self.pidEntry.delete(0, tk.END)
            self.atEntry.delete(0, tk.END)
            self.btEntry.delete(0, tk.END)
            self.pidEntry.focus()
            self.adverLabel.config(text="Data added successfully")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data!")
        
    def clearProcess(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.canvas.delete("all")
        self.avgTATLabel.config(text="Average TAT: 0.0 ms")
        self.avgWTLabel.config(text="Average WT: 0.0 ms")
        self.avgRTLabel.config(text="Average RT: 0.0 ms")
        self.adverLabel.config(text="Data cleared")

    def caculatorProcess(self):
        if not self.processes:
            messagebox.showwarning("Warming", "There is no process for calculation yet!")
            return
        try:
            # Lưu ý: Hàm trả về 5 giá trị
            procs, gantt, avgWT, avgTAT, avgRT = SJFPreemptive(self.processes)

            self.updateTable(procs)
            self.drawGantt(gantt)

            self.avgTATLabel.config(text=f"Average TAT: {avgTAT:.2f} ms")
            self.avgWTLabel.config(text=f"Average WT: {avgWT:.2f} ms")
            self.avgRTLabel.config(text=f"Average RT: {avgRT:.2f} ms")
            self.adverLabel.config(text="Successful calculation")
        except Exception as e:
            messagebox.showerror("Algorithm Error", str(e))
    def updateTable(self,procs):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for p in procs:
            self.tree.insert("", "end", values=(
                p.pid, p.arrivalTime, p.burstTime, 
                p.completionTime, p.turnAroundTime, p.waitingTime, p.responseTime
            ))

    def drawGantt(self, gantt):
        self.canvas.delete("all")

        scale = 40
        x = 20
        y1 = 30
        y2 = 80

        colors = [
            "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4",
            "#FFD93D", "#A29BFE", "#FD79A8", "#00B894"
        ]

        colorMap = {}

        def getColor(pid):
            if pid == "IDLE":
                return "#B2BEC3"
            if pid not in colorMap:
                colorMap[pid] = colors[len(colorMap) % len(colors)]
            return colorMap[pid]

        
        for pid, start, end in gantt:
            width = (end - start) * scale
            color = getColor(pid)

            self.canvas.create_rectangle(
                x, y1, x + width, y2,
                fill=color,
                outline="black",
                width=2
            )

            self.canvas.create_text(
                x + width / 2,
                (y1 + y2) / 2,
                text=str(pid),
                font=("Arial", 10, "bold")
            )

            self.canvas.create_text(
                x,
                y2 + 15,
                text=str(start),
                font=("Arial", 9)
            )

            x += width

        self.canvas.create_text(
            x,
            y2 + 15,
            text=str(gantt[-1][2]),
            font=("Arial", 9)
        )        

       
if __name__ == "__main__":
    root = tk.Tk()
    app = Display(root)
    root.mainloop()