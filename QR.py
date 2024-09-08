import qrcode

# Greet the user
print("🐱‍👤 Hello there, friend! Let's make a super cool QR code together! 🐱‍👤")

# Get text input from the user
text = input("✨ Please enter the magical text you want to turn into a QR code: ")

# Create QR code
qr = qrcode.QRCode(
    version=1,  # Tiny but mighty QR code size (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Keeping it neat and error-free!
    box_size=10,  # Size of each little pixel box (so cute!)
    border=4,  # Just a lil' border for the QR code
)
qr.add_data(text)
qr.make(fit=True)

# Create QR code image with blue QR code and white background
img = qr.make_image(fill_color="RoyalBlue", back_color="white")

# Save image with a fun name
filename = "qrcode.png"
img.save(filename)

# Show off the QR code
img.show()

# Parting message
print(f"🎉 Ta-da! Your QR code has been created, Go scan it and share the magic! ✨")
