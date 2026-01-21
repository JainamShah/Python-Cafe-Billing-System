import qrcode
from urllib.parse import quote
from datetime import datetime
import random

menu = {
    "Pizza": 600,
    "Burger": 40,
    "Pasta": 350,
    "Salad": 100,
    "Soda": 150,
    "Milkshake": 250,
    "Coffee": 150,
    "Momos": 350,
    "Sandwich": 150,
    "Noodles": 40,
    "Mocktail": 300
}

# Greeting
print("Welcome to our Python Restaurant!")
print("Here is our Menu:\n")

for item, price in menu.items():
    print(f"{item}: {price} INR")

# Taking Order with Quantity
order = {}

while True:
    item = input("\nEnter the item you want to order (or type 'done' to finish): ").title()

    if item.lower() == "done":
        break

    if item in menu:
        qty = int(input(f"Enter quantity for {item}: "))
        order[item] = order.get(item, 0) + qty
        print(f"✅ {item} x{qty} added to your order.")
    else:
        print("❌ Sorry, we don't have that item on the menu.")

# Generate Bill
if not order:
    print("\n⚠ No order placed. Thank you!")
    exit()

total_bill = 0
bill_lines = []
order_id = random.randint(1000, 9999)
time_now = datetime.now().strftime("%d-%m-%Y %I:%M %p")


print("\n==================== BILL ====================")
print("Python Restaurant")
print(f"Order ID: {order_id}, Date/Time: {time_now}")

print("------------------------------------------------")

for item, qty in order.items():
    price = menu[item]
    item_total = price * qty
    total_bill += item_total
    print(f"{item:10} x{qty:<2} = {item_total} INR")
    bill_lines.append(f"{item} x{qty} = {item_total} INR")

print("------------------------------------------------")
print(f"TOTAL BILL: {total_bill} INR")
print("================================================")

# Extra Details
#order_id = random.randint(1000, 9999)
#time_now = datetime.now().strftime("%d-%m-%Y %I:%M %p")

# ✅ QR Code Data (Detailed)
qr_data = f"""
PYTHON RESTAURANT
Order ID: {order_id}
Date/Time: {time_now}

Items:
""" + "\n".join(bill_lines) + f"""

-------------------------
TOTAL: {total_bill} INR
Thank you! Visit Again 😊
"""

#UPI Payment Link (Optional)
upi_id = "jeny.cool51-1@okhdfcbank"
payee_name = "Python Restaurant"

# Create UPI link
note = f"Order Payment - {order_id}"
upi_link = f"upi://pay?pa={upi_id}&pn={quote(payee_name)}&am={total_bill}&cu=INR&tn={quote(note)}"
# Generate QR for UPI link
upi_qr = qrcode.make(upi_link)
upi_qr_file = f"upi_payment_qr_{order_id}.png"
upi_qr.save(upi_qr_file)


# Generate QR
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(qr_data)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white")

file_name = f"bill_qr_{order_id}.png"
qr_img.save(file_name)

print(f"\n✅ Detailed QR Code Generated Successfully!")
print(f"📌 Saved as: {file_name}")
