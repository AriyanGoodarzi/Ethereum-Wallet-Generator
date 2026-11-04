from mnemonic import Mnemonic
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from eth_account import Account
import qrcode
from PIL import Image, ImageTk
import secrets

# ---------------------------
# Main Application Window
# ---------------------------
app = ttk.Window(
    title="Ethereum Wallet Generator",
    themename="cyborg",
    size=(950, 800),
    resizable=(True, True)
)

# ---------------------------
# Canvas + Scrollable Frame
# ---------------------------
canvas = Canvas(app)
scrollbar = ttk.Scrollbar(app, orient=VERTICAL, command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

# ---------------------------
# Generate wallet
# ---------------------------
def generate_wallet():
    private_key = "0x" + secrets.token_hex(32)
    acct = Account.from_key(private_key)
    public_key = acct._key_obj.public_key
    address = acct.address

    priv_text.delete(1.0, END)
    pub_text.delete(1.0, END)
    addr_text.delete(1.0, END)

    priv_text.insert(END, private_key)
    pub_text.insert(END, str(public_key))
    addr_text.insert(END, address)

    eth_link = f"ethereum:{address}"
    generate_qr(eth_link)

    status_label.config(text="Wallet generated successfully!", foreground="green")

# ---------------------------
# Generate 12-word BIP39 mnemonic
# ---------------------------
def generate_bip39():
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=128)
    bip39_text.delete(1.0, END)
    bip39_text.insert(END, words)
    status_label.config(text="12-word Seed generated successfully!", foreground="green")

# ---------------------------
# Copy text to clipboard
# ---------------------------
def copy_text(text_widget, message):
    app.clipboard_clear()
    app.clipboard_append(text_widget.get(1.0, END).strip())
    status_label.config(text=message, foreground="blue")

# ---------------------------
# Save QR code as image
# ---------------------------
def save_qr():
    qr_label.image._PhotoImage__photo.write("Ethereum_Address_QR.png", format="png")
    status_label.config(text="QR Code saved successfully!", foreground="purple")

# ---------------------------
# Generate QR code image
# ---------------------------
def generate_qr(address):
    qr = qrcode.make(address)
    qr.save("address_qr.png")

    img = Image.open("address_qr.png")
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)

    qr_label.config(image=img)
    qr_label.image = img

# ---------------------------
# Title
# ---------------------------
title = ttk.Label(scrollable_frame, text="Ethereum Wallet Generator", font=("Arial", 26, "bold"))
title.pack(pady=15)

# ---------------------------
# Frame for keys and address
# ---------------------------
frame = ttk.Frame(scrollable_frame)
frame.pack(pady=10)

# Private Key
priv_label = ttk.Label(frame, text="Private Key:", font=("Arial", 16, "bold"))
priv_label.grid(row=0, column=0, sticky=W, pady=5)
priv_text = Text(frame, width=85, height=2, font=("Consolas", 12))
priv_text.grid(row=1, column=0, pady=5)

# Public Key
pub_label = ttk.Label(frame, text="Public Key:", font=("Arial", 16, "bold"))
pub_label.grid(row=2, column=0, sticky=W, pady=5)
pub_text = Text(frame, width=85, height=3, font=("Consolas", 12))
pub_text.grid(row=3, column=0, pady=5)

# Ethereum Address
addr_label = ttk.Label(frame, text="Ethereum Address:", font=("Arial", 16, "bold"))
addr_label.grid(row=4, column=0, sticky=W, pady=5)
addr_text = Text(frame, width=85, height=2, font=("Consolas", 12))
addr_text.grid(row=5, column=0, pady=5)

# ---------------------------
# BIP39 12-word Seed Phrase
# ---------------------------
bip39_label = ttk.Label(scrollable_frame, text="BIP39 12-word Seed Phrase:", font=("Arial", 16, "bold"))
bip39_label.pack(pady=5)
bip39_text = Text(scrollable_frame, width=85, height=3, font=("Consolas", 12))
bip39_text.pack(pady=5)

bip39_button = ttk.Button(scrollable_frame, text="Generate 12-word Seed", bootstyle="info", command=generate_bip39)
bip39_button.pack(pady=5)

# ---------------------------
# QR Code
# ---------------------------
qr_label = ttk.Label(scrollable_frame)
qr_label.pack(pady=15)

# ---------------------------
# Buttons: Generate + Copy + Save QR
# ---------------------------
generate_btn = ttk.Button(scrollable_frame, text="Generate Wallet", bootstyle="success", command=generate_wallet)
generate_btn.pack(pady=10)

copy_priv_btn = ttk.Button(scrollable_frame, text="Copy Private Key", bootstyle="info",
                           command=lambda: copy_text(priv_text, "Private Key copied!"))
copy_priv_btn.pack(pady=5)

copy_pub_btn = ttk.Button(scrollable_frame, text="Copy Public Key", bootstyle="info",
                          command=lambda: copy_text(pub_text, "Public Key copied!"))
copy_pub_btn.pack(pady=5)

copy_addr_btn = ttk.Button(scrollable_frame, text="Copy Address", bootstyle="info",
                           command=lambda: copy_text(addr_text, "Address copied!"))
copy_addr_btn.pack(pady=5)

save_qr_btn = ttk.Button(scrollable_frame, text="Save QR Code", bootstyle="warning", command=save_qr)
save_qr_btn.pack(pady=10)

# ---------------------------
# Status Label
# ---------------------------
status_label = ttk.Label(scrollable_frame, text="", font=("Arial", 14, "italic"))
status_label.pack(pady=5)

# ---------------------------
# Run application
# ---------------------------
app.mainloop()


