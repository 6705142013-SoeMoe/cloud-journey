import shutil

def check_disk(path, warn_percent):
    total, used, free = shutil.disk_usage(path)
    percent_used = used / total * 100
    print(f"Path: {path}")
    print(f"Used: {percent_used:.1f}%")
    if percent_used > warn_percent:
        print("WARNING: disk is getting full!")
    else:
        print("OK: plenty of space.")

check_disk("/", 0)
