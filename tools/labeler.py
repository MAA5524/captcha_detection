import os
import csv
import shutil
from tkinter import StringVar, messagebox
from PIL import Image, ImageTk
import customtkinter as ctk

# ======================
# Configuration
# ======================
IMAGE_DIR = "../data/images"
PROCESSED_DIR = "../data/processed"
CSV_FILE = "../data/labeling_state.csv"

os.makedirs(PROCESSED_DIR, exist_ok=True)

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "label"])

# Set modern theme
ctk.set_appearance_mode("System")  # "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

class CaptchaLabeler:
    def __init__(self):
        self.images = sorted([f for f in os.listdir(IMAGE_DIR) if f.lower().endswith('.png')])
        self.current_index = 0

        self.root = ctk.CTk()
        self.root.title("Captcha Labeler — Modern UI")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        # Header
        header = ctk.CTkLabel(self.root, text="📝 Captcha Labeler", font=("Segoe UI", 20, "bold"))
        header.pack(pady=(15, 5))

        # Image frame
        self.img_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.img_frame.pack(pady=10)

        self.img_label = ctk.CTkLabel(
            self.img_frame,
            text="",
            width=300,
            height=50
        )
        self.img_label.pack()

        # Filename label
        self.filename_label = ctk.CTkLabel(self.root, text="", font=("Segoe UI", 12))
        self.filename_label.pack(pady=(5, 5))

        # Input frame
        input_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        input_frame.pack(pady=10)

        ctk.CTkLabel(input_frame, text="Enter CAPTCHA text:", font=("Segoe UI", 14)).pack()
        self.label_var = StringVar()
        self.label_entry = ctk.CTkEntry(
            input_frame,
            textvariable=self.label_var,
            width=300,
            font=("Segoe UI", 18),
            placeholder_text="e.g., PMXDN",
            corner_radius=10,
            height=40
        )
        self.label_entry.pack(pady=5)
        self.label_entry.bind("<Return>", self.submit)

        # Button frame
        button_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        button_frame.pack(pady=15)

        self.submit_btn = ctk.CTkButton(
            button_frame,
            text="✅ Save & Next",
            command=self.submit,
            width=150,
            height=40,
            font=("Segoe UI", 14, "bold"),
            corner_radius=10,
            fg_color="#1f6aa5",
            hover_color="#144b7a"
        )
        self.submit_btn.pack()

        # Status label
        self.status_label = ctk.CTkLabel(self.root, text="Ready to label...", text_color="gray", font=("Segoe UI", 12))
        self.status_label.pack(pady=10)

        self.show_current()

    def append_to_csv(self, filename, label):
        with open(CSV_FILE, "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([filename, label])

    def show_current(self):
        if self.current_index >= len(self.images):
            messagebox.showinfo("🎉 Done!", "All images have been labeled!")
            self.root.quit()
            return

        img_name = self.images[self.current_index]
        img_path = os.path.join(IMAGE_DIR, img_name)

        try:
            img = Image.open(img_path)
            img.thumbnail((700, 500), Image.Resampling.LANCZOS)
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(300, 50))
            self.img_label.configure(image=ctk_img, text="")
            self.img_label.image = ctk_img
        except Exception as e:
            self.img_label.configure(image=None, text="⚠️ Image load error", font=("Segoe UI", 14))
            self.img_label.image = None

        self.filename_label.configure(text=f"📁 {img_name}")
        self.label_var.set("")
        self.status_label.configure(text="Enter label → Press Enter")

        self.label_entry.focus()

    def submit(self, event=None):
        label = self.label_var.get().strip()
        img_name = self.images[self.current_index]

        if not label:
            self.status_label.configure(text="❌ Label cannot be empty!", text_color="red")
            return

        src_path = os.path.join(IMAGE_DIR, img_name)
        dst_path = os.path.join(PROCESSED_DIR, img_name)

        try:
            shutil.move(src_path, dst_path)
            self.append_to_csv(img_name, label)

            self.current_index += 1
            self.show_current()
            self.status_label.configure(text="✅ Saved! Next image...", text_color="green")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process:\n{str(e)}")
            self.status_label.configure(text="❌ Error occurred", text_color="red")

if __name__ == "__main__":
    app = CaptchaLabeler()
    app.root.mainloop()