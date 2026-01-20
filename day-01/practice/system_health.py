import psutil  # import library from PyPI

def check_cpu_threshold():
    # User se CPU threshold lena
    cpu_threshold = int(input("Enter CPU Threshold (%): "))

    # Current CPU usage nikalna
    current_cpu = psutil.cpu_percent(interval=1)
    print(f"Current CPU Usage: {current_cpu}%")

    # Threshold compare karna
    if current_cpu > cpu_threshold:
        print("⚠️ CPU Threshold crossed!")
        print("📧 Alert Email Sent (dummy)")
    else:
        print("✅ CPU is in safe state")


check_cpu_threshold()
