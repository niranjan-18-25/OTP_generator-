🔐 OTP Verification Program (Python)
📌 Overview

This is a simple Python-based One-Time Password (OTP) verification system.
The program generates a random 6-digit OTP and allows the user up to 3 attempts to enter the correct OTP.

If the correct OTP is entered within the allowed attempts, access is granted. Otherwise, the OTP expires.

⚙️ How It Works

The program generates a random 6-digit OTP using Python’s built-in random module.

The OTP is displayed on the screen (for testing purposes).

The user is prompted to enter the OTP.

The user gets 3 total attempts:

✅ Correct OTP → Access Granted 🎉

❌ Wrong OTP (3 times) → OTP Expired 😒

🧠 Code Logic Breakdown

random.randint(100000, 999999) generates a 6-digit OTP.

A while(True) loop keeps asking for input until:

The correct OTP is entered, or

The attempt limit is reached.

A counter variable count tracks the number of failed attempts.

▶️ How to Run
1️⃣ Requirements

Python 3.x installed

2️⃣ Run the Program
python filename.py


(Replace filename.py with your actual file name.)

📄 Example Output
Generated OTP: 483921
Enter the OTP : 123456
Your entered wrong OTP
Enter the OTP : 483921
Access Granted 🎉

🚀 Future Improvements (Optional Ideas)

Hide the OTP (simulate sending via SMS/Email)

Add time-based expiration (e.g., 60 seconds)

Store attempts securely

Use string OTP to preserve leading zeros

Add GUI interface

📚 Concepts Used

Random number generation

Loops (while)

Conditional statements (if-else)

User input handling

Basic authentication logic

👨‍💻 Author

Created as a beginner-friendly Python project to understand loops and conditional logic.
