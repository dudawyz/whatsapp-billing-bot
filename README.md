# 📲 WhatsApp Billing Bot

A Python automation bot that reads client data from a spreadsheet and automatically sends billing reminder messages via WhatsApp Web.

---

## 💡 About the Project

This was my first personal project — built to solve a real problem: sending payment reminder messages to multiple clients without doing it manually one by one.

The bot reads a list of clients (name, phone number, and due date) from an Excel file and sends a personalized WhatsApp message to each one using WhatsApp Web.

---

## ⚙️ How It Works

1. Opens WhatsApp Web in the browser
2. Reads the client list from `clientes chat bot.xlsx`
3. For each client, builds a personalized message with their name and due date
4. Opens the WhatsApp Web send link for that phone number
5. Automatically presses Enter to send the message
6. Closes the tab and moves to the next client

---

## 🛠️ Technologies Used

- Python 3
- [openpyxl](https://openpyxl.readthedocs.io/) — reading the Excel spreadsheet
- [pyautogui](https://pyautogui.readthedocs.io/) — simulating keyboard input
- [webbrowser](https://docs.python.org/3/library/webbrowser.html) — opening WhatsApp Web links
- [urllib.parse](https://docs.python.org/3/library/urllib.parse.html) — encoding the message text in the URL

---

## 📁 Spreadsheet Format

The file `clientes chat bot.xlsx` should follow this structure:

| Name       | Phone Number  | Due Date   |
|------------|---------------|------------|
| João Silva | 5511999999999 | 2026-04-30 |
| Maria Lima | 5521988888888 | 2026-05-05 |

> ⚠️ The phone number must include the country code (e.g. `55` for Brazil) with no spaces or special characters.

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/whatsapp-billing-bot.git
   cd whatsapp-billing-bot
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your client data to the spreadsheet following the format above.

4. Run the script:
   ```bash
   python app.py
   ```

5. When the browser opens WhatsApp Web, scan the QR code and wait for it to load before the bot starts.

---

## ⚠️ Known Limitations

- The bot uses fixed `sleep()` delays to wait for WhatsApp Web to load. If your internet is slow, you may need to increase these values in the code.
- WhatsApp Web must be kept open and in focus during execution.
- This project uses browser automation and is intended for personal use only.

---

## 📌 Status

✅ Functional — built as a personal automation project and portfolio piece.

---

## 👤 Author

Made by [duda](https://https://github.com/dudawyz)
