import tkinter as tk
from tkinter import messagebox
import threading
import serial
import time

# Global variables for tracking attempts and lockout status
attempt_count = 0
lockout_time = None
lockout_period = 30 * 60  # 30 minutes in seconds

# Assuming the serial port setup as per Serial.py
port = serial.Serial("COM7", 9600)

class PinInputUI:
    def __init__(self, master):
        self.master = master
        self.pin = "1234"  # Assuming this is the correct PIN
        master.protocol("WM_DELETE_WINDOW", self.on_close)  # Handle window close event

    def check_pin(self, entered_pin):
        global attempt_count, lockout_time

        # Check if we are currently in a lockout period
        if lockout_time is not None:
            remaining_lockout = lockout_period - (time.time() - lockout_time)
            if remaining_lockout > 0:
                messagebox.showerror("Access Denied", f"Too many incorrect attempts. Please try again in {int(remaining_lockout // 60)} minutes.")
                return

        # Reset lockout time if the PIN is checked outside the lockout period
        lockout_time = None

        # PIN verification
        if entered_pin == self.pin:
            messagebox.showinfo("Access Granted", "Correct PIN. Door unlocked.")
            port.write(b'1')  # Signal to unlock the door through the serial port
            self.reset_attempts()  # Reset attempt counter
            self.master.destroy()  # Close the PIN input window
        else:
            attempt_count += 1
            if attempt_count >= 5:
                messagebox.showerror("Access Denied", "Too many incorrect attempts. Try again in 30 minutes.")
                attempt_count = 0  # Reset attempt counter
                lockout_time = time.time()  # Start lockout period
            else:
                messagebox.showerror("Access Denied", "Incorrect PIN.")

    def reset_attempts(self):
        global attempt_count, lockout_time
        attempt_count = 0
        lockout_time = None

    def on_close(self):
        self.reset_attempts()
        self.master.destroy()

def run_pin_ui():
    root = tk.Tk()
    ui = PinInputUI(root)
    tk.Label(root, text="Enter PIN:").pack()
    pin_entry = tk.Entry(root, show="*")
    pin_entry.pack()
    pin_entry.bind("<Return>", lambda event: ui.check_pin(pin_entry.get()))
    root.mainloop()

# If running directly for testing
if __name__ == "__main__":
    run_pin_ui()
