# PD2-2
Dāvis Smalkais, DT1-1


# Label; MountPoint; TotalSize (MB); Used (%)
partitions = [
"System;/;50000;85",
"Data;/home;150000;40",
"Cache;/tmp;5000;10",
"Backup;/mnt/backup;500000;92",
"USB-Drive;/media/usb;16000;0",
"Logs;/var/log;10000;95",
"Database;/var/lib/mysql;80000;70",
"Shared;/mnt/shared;200000;15",
"Win-System;/mnt/win;100000;90",
"Recovery;/recovery;2000;98"
]

from tkinter import *

# Create the main window
ws = Tk()
ws.geometry("300x400")

# Add labels 
Label(ws, text="System", borderwidth=3, padx=5, pady=10).pack(padx=5, pady=10)
Label(ws, text="Data", borderwidth=3,  padx=5, pady=10).pack(padx=5, pady=10)
Label(ws, text="Cache", borderwidth=3, padx=5, pady=10).pack(padx=5, pady=10)
Label(ws, text="Backup", borderwidth=3, padx=5, pady=10).pack(padx=5, pady=10)
Label(ws, text="USB-Drive", borderwidth=3, padx=5, pady=10).pack(padx=5, pady=10)
Label(ws, text="Logs", borderwidth=3, padx=5, pady=10).pack(padx=5, pady=10)
Label(ws, text="Database", borderwidth=3, padx=5, pady=10).pack(padx=5, pady=10)
Label(ws, text="Shared", borderwidth=3, padx=5, pady=10).pack(padx=5, pady=10)
Label(ws, text="Win", borderwidth=3, padx=5, pady=10).pack(padx=5, pady=10)
Label(ws, text="Recovery", borderwidth=3, padx=5, pady=10).pack(padx=5, pady=10)
# Run the main event loop
ws.mainloop()

TotalSize = [50000, 150000, 5000, 500000, 16000, 10000, 80000, 200000, 100000, 2000]
print(sum(TotalSize),"MB")

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(f"Used%: {total}%")
