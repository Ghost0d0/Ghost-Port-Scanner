import customtkinter as ctk
from tkinter import messagebox
import threading
import scanner  # Import our scanner functions

# GUI Class
class PortScannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ghost Scanner - Advanced Port Scanner")
        self.geometry("600x450")

        # Hacker theme colors
        self.bg_color = "#2c3e50"  # A more subtle dark blue background
        self.text_color = "#00FF00"  # Green text
        self.highlight_color = "#00BFFF"  # Cyan highlight
        self.button_color = "#2E8B57"  # Sea green button
        self.button_hover_color = "#3CB371"  # Light sea green hover

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.configure(bg=self.bg_color)

        # Title with floating effect
        self.label_title = ctk.CTkLabel(
            self,
            text="👻 GHOST SCANNER",
            font=("Courier", 24, "bold"),
            text_color=self.highlight_color,
            bg_color="transparent", #Force transparency
        )
        self.label_title.pack(pady=(10, 5))

        # IP Entry
        self.label_ip = ctk.CTkLabel(
            self, text="Enter Target IP:", text_color=self.text_color, bg_color="transparent" #Force transparency
        )
        self.label_ip.pack()
        self.entry_ip = ctk.CTkEntry(self, width=250, bg_color=self.bg_color, text_color=self.text_color)
        self.entry_ip.pack(pady=5)

        # Scan Button
        self.button_scan = ctk.CTkButton(
            self,
            text="Start Scan",
            command=self.start_scan,
            fg_color=self.button_color,
            hover_color=self.button_hover_color,
        )
        self.button_scan.pack(pady=10)

        # Progress Bar and Percentage Label
        self.progress = ctk.CTkProgressBar(self, fg_color=self.button_color, progress_color=self.highlight_color)
        self.progress.pack(pady=(5, 0))
        self.progress.set(0)
        self.progress_label = ctk.CTkLabel(self, text="0%", text_color=self.text_color, bg_color="transparent") #Force transparency
        self.progress_label.pack(pady=(0, 10))

        # Results Box with scrollbar
        self.text_results = ctk.CTkTextbox(
            self, width=500, height=180, text_color=self.text_color, bg_color="#282828"
        )
        self.text_results.pack(pady=10)

        self.text_results.configure(state="disabled")

    def start_scan(self):
        target_ip = self.entry_ip.get()
        if not target_ip:
            messagebox.showwarning("Warning", "Please enter a target IP!")
            return
        self.text_results.configure(state="normal")
        self.text_results.delete("1.0", "end")
        self.text_results.insert("end", f"Scanning target: {target_ip}\n")
        self.text_results.configure(state="disabled")
        self.progress.set(0)
        self.progress_label.configure(text="0%")
        threading.Thread(target=self.run_scan, args=(target_ip,)).start()

    def run_scan(self, target_ip):
        ports = [21, 22, 80, 445, 3306]
        open_ports = scanner.stealth_scan(target_ip, ports)

        self.update_progress(30)
        os_detected = scanner.detect_os(target_ip)
        self.update_progress(60)
        vulnerabilities_found = scanner.check_vulnerabilities(open_ports)
        self.update_progress(90)

        results = f"Target: {target_ip}\n"
        results += f"OS Detected: {os_detected}\n"
        results += f"Open Ports: {', '.join(map(str, open_ports))}\n"

        # Modified vulnerability section
        if vulnerabilities_found:
            results += "Vulnerabilities:\n"
            for vuln in vulnerabilities_found:
                results += f"- {vuln}\n"
        else:
            results += "No known vulnerabilities detected.\n"

        self.text_results.configure(state="normal")
        self.text_results.insert("end", results)
        self.text_results.configure(state="disabled")
        self.update_progress(100)
        scanner.save_results(target_ip, open_ports, os_detected, vulnerabilities_found)

    def update_progress(self, value):
        self.progress.set(value / 100)
        self.progress_label.configure(text=f"{value}%")

# 👇 THIS is what main.py will import and call
def launch_gui():
    app = PortScannerApp()
    app.mainloop()