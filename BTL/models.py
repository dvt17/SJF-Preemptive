from display import *
class Process:
    def __init__(self, pid,arrivalTime, burstTime):
        self.pid = pid                          # Process ID
        self.arrivalTime = arrivalTime          # Arrival Time (Thời gian đến)
        self.burstTime = burstTime              # Burst Time (Thời gian chạy)
        
        self.remainingTime = burstTime          # Remaining Time (Thời gian còn lại)
        self.completionTime = 0                 # Completion Time (Thời gian hoàn thành)
        self.turnAroundTime = 0                 # Turn Around Time (Thời gian lưu lại)
        self.waitingTime = 0                    # Waiting Time (Thời gian chờ)
        self.firstResponseTime = -1             # Timestamp when CPU is first allocated (-1 means not allocated yet)
        self.responseTime = 0                   # Response Time = firstResponseTime - arrivalTime


def  SJFPreemptive(processes):
 
    # Input validation
    for p in processes:
        if p.burstTime <= 0 or p.arrivalTime < 0:
            raise ValueError(f"Invalid input for Process {p.pid}: Burst time must be > 0 and Arrival time must be >= 0.")
        # Restore the remaining time (rt) to the initial burst time (bt)
        p.remainingTime = p.burstTime
        p.firstResponseTime = -1
        p.responseTime = 0
        p.completionTime = 0
        p.turnAroundTime = 0
        p.waitingTime = 0

    n = len(processes)
    currentTime = 0
    completed = 0
    gantt = [] 
    lastPid = None
    startTime = 0

    # Loop until all processes are completed
    while completed != n:
        idx = -1
        minRemainingTime = float('inf')
        
        # Find the arrived process with the shortest remaining time
        for i in range(n):
            if processes[i].arrivalTime <= currentTime and processes[i].remainingTime > 0:
                if processes[i].remainingTime < minRemainingTime:
                    minRemainingTime = processes[i].remainingTime
                    idx = i
                # Tie-breaker Level 1: Prioritize FCFS (earliest arrival)
                elif processes[i].remainingTime == minRemainingTime and idx != -1:
                    if processes[i].arrivalTime < processes[idx].arrivalTime:
                        idx = i
                    # Tie-breaker Level 2: If arrival times are also equal, sort by PID
                    elif idx != -1 and processes[i].arrivalTime == processes[idx].arrivalTime:
                        if processes[i].pid < processes[idx].pid:
                            idx = i

        if idx != -1: 
            pid = processes[idx].pid
            
            # Record first response time for the process
            if processes[idx].firstResponseTime == -1:
                processes[idx].firstResponseTime = currentTime
                processes[idx].responseTime = processes[idx].firstResponseTime - processes[idx].arrivalTime

            # Record context switch (Preemption)
            if lastPid != pid:
                if lastPid is not None:
                    gantt.append((lastPid, startTime, currentTime))
                startTime = currentTime
                lastPid = pid
            
            # Execute for 1 unit of time
            processes[idx].remainingTime -= 1
            currentTime += 1
            
            # Process is completed
            if processes[idx].remainingTime == 0:
                completed += 1
                processes[idx].completionTime = currentTime
                processes[idx].turnAroundTime = processes[idx].completionTime - processes[idx].arrivalTime
                processes[idx].waitingTime = processes[idx].turnAroundTime - processes[idx].burstTime
                
        else:
            # If no process is in the Ready Queue -> CPU is IDLE
            if lastPid != "IDLE":
                if lastPid is not None:
                    gantt.append((lastPid, startTime, currentTime))
                startTime = currentTime
                lastPid = "IDLE"
            currentTime += 1
            
    # Append the final execution block to the Gantt chart
    if lastPid is not None:
        gantt.append((lastPid, startTime, currentTime))

    # Calculate average metrics for reporting
    avgWaitingTime = sum(p.waitingTime for p in processes) / n if n > 0 else 0
    avgTurnAroundTime = sum(p.turnAroundTime for p in processes) / n if n > 0 else 0
    avgResponseTime = sum(p.responseTime for p in processes) / n if n > 0 else 0

    return processes, gantt, avgWaitingTime, avgTurnAroundTime, avgResponseTime



