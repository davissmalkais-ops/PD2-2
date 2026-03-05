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

# 3. uzdevums
for entry in partitions:
  parts = entry.split (";")
  lable = parts[0]
  used = int(parts[3])
  if used >= 90:
    print(f"UZMANĪBU:[Label] disks ir pilns!")

# 4. uzdevums
for entry in partitions:
  parts = entry.split(";")
  lable = parts[0]
  size_gb = int(parts[2]) / 1024
  print(f"[lable]: {size_gb:.2f} GB")

# 5. uzdevums
mount_input = input("Ievadiet montējuma punktu")
found = False
for entry in partitions:
   parts = entry.split(";")
  if parts[1] == mount_input:
    print(parts[0])
    found = True
    break
if not found:
  print("Nav atrasts")

#6. uzdevums
def calculate_used_mb(partitions_list):
  parts = entry.split(";")
  lable = parts[0]
  total_size = int(parts[2])
  used_percent = int (parts[3])
  used-mb - int(total_size * (used_percent / 100))
  result.append({"Label": label, "UsedMB": used_mb})
return result

