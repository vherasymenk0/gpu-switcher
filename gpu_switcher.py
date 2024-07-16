import subprocess
import tkinter as tk
from tkinter import messagebox

def switch_gpu(gpu_type):
    try:
        if gpu_type == "nvidia":
            mode = "on-demand"
        else:
            mode = gpu_type
        
        subprocess.run(["sudo", "prime-select", mode], check=True)
        subprocess.run(["sudo", "systemctl", "restart", "gdm3"], check=True)  # Замените "gdm3" на "lightdm" или другой дисплейный менеджер, если используете другой.
        messagebox.showinfo("Success", f"Switched to {gpu_type} GPU ({mode} mode). X-server restarted.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to switch to {gpu_type} GPU ({mode} mode).\n{e}")

def create_ui():
    window = tk.Tk()
    window.title("GPU Switcher")

    label = tk.Label(window, text="Select GPU:")
    label.pack(pady=10)

    intel_button = tk.Button(window, text="Integrated (Intel)", command=lambda: switch_gpu("intel"))
    intel_button.pack(pady=5)

    nvidia_button = tk.Button(window, text="Discrete (NVIDIA On-Demand)", command=lambda: switch_gpu("nvidia"))
    nvidia_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_ui()
