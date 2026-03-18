suspicious_files =[
    "rk.sys",
    "rootkit.exe",
    "hidden_driver",
    "malware.sys"
]

def scan_file(filename):
    
    if filename in suspicious_files:
        return "Possible Rootkit Detected"
    else:
        return "File is safe" 