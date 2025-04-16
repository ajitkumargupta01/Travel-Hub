****🚄 Travel Hub – Indian Rail Management System (RMS)****

Travel Hub is a multi-service, full-stack travel management platform built using Streamlit and MySQL. It enables users to book tickets for trains, metros, flights, and cabs, order meals during train travel, manage profiles, and much more — all through an intuitive and responsive interface.

Designed for Indian travelers, this project is ideal for personal use, hackathons, student projects, or as a foundation for larger transport systems.

🌟 Features
🔐 Authentication
User sign-up and login

Data is stored securely in MySQL

**🚆 Train Ticket Booking**

Search trains by source and destination

View timings, duration, and class options

Book for multiple passengers

Generate PNR & seat numbers

**🚇 Metro Ticket Booking**

Browse available routes & schedules

QR code generation for boarding

View & cancel metro tickets

**✈️ Flight Booking**

Browse and book domestic flights

View booked flight tickets

Cancel tickets if needed

**🚕 Cab Booking**

Select pickup and destination

Real-time fare estimate based on distance

Choose vehicle type: Bike, Auto, Mini Cab, Sedan

**🍽️ Train Restaurant Ordering**

Browse menus from local restaurants

Choose city & hotel

Add food items to the cart and place orders

Choose dine-in, takeaway, or seat delivery

**👤 User Profile**

View personal details

Edit & update your info

Logout securely

**📋 Ticket Management**

View all train/flight/metro ticket bookings

Cancel train tickets with one click

**🧑‍💻 About the Developers**

Highlights the contributions of all 4 developers

LinkedIn profiles for professional reference

**🆘 Help & Support**

Built-in bug reporting

Categorized issues per module (Train, Cab, etc.)

🖥️ Tech Stack

Layer	Technology
Frontend	Streamlit (Python UI)
Backend	Python
Database	MySQL
Libraries	streamlit, pandas, mysql-connector-python, qrcode, datetime, io
📦 Folder Structure
bash
Copy
Edit
📁 travel-hub/
├── rms.py             # Main Streamlit application
├── authunicate.py     # Login/signup logic and database queries
├── dbconnect.py       # MySQL connection configuration
└── README.md          # Documentation
🔧 Setup Instructions

**1. 🐍 Create Virtual Environment**

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
**2. 📦 Install Required Dependencies**

pip install streamlit pandas mysql-connector-python qrcode

**3. 🛢️ Setup MySQL**

Open MySQL client or phpMyAdmin
Run this command:
CREATE DATABASE irctc;
Update your dbconnect.py with your MySQL credentials:
# dbconnect.py
return mysql.connector.connect(
    host="localhost",
    user="your_username",       # <- Your MySQL username
    password="your_password",   # <- Your MySQL password
    database="irctc"
)
✅ Tables like users, trains, and passengers will be auto-created by the app when required.

▶️ Run the Application
streamlit run rms.py
You’ll be redirected to your browser automatically. If not, visit: http://localhost:8501

🧪 Sample Test Workflow
Sign up with your email and details

Log-in and access the homepage

Search Trains or Book Metro/Flight/Cab

Order Food during your journey

View/Cancel tickets anytime

Edit your profile and manage bookings

**💡 Future Enhancements** (Optional Ideas)

🔄 Integration with Google Maps API for live cab tracking

💳 Payment gateway integration (Razorpay/UPI)

🧠 ML-based train delay predictions

📱 Convert to PWA (Progressive Web App)

**👨‍💻 Contributors**

Ajit Kumar Gupta | https://www.linkedin.com/in/ajit-kumar-gupta-89405b297

📬 Contact
📧 ajeetkumargupta907@gmail.com 




***before running the project, do the **
**## 💾Database Setup**
Open MySQL Command Line Client:
  CREATE DATABASE irctc;

Before searching for trains, run the following command in the MySQL command line to add dummy train data

  INSERT INTO trains VALUES
('Rajdhani Express', '12301', 'Delhi', 'Patna', '17:15', '08:45', '15h 30m', '2025-04-20', '1A, 2A, 3A', 'SL', 'GN', 'CC'),
('Shatabdi Express', '12023', 'Patna', 'Howrah', '05:30', '13:30', '8h 00m', '2025-04-21', 'CC', 'EC', '', ''),
('Vikramshila Express', '12367', 'Bhagalpur', 'Anand Vihar', '11:00', '06:10', '19h 10m', '2025-04-22', '1A, 2A, 3A', 'SL', 'GN', ''),
('Magadh Express', '20801', 'Islampur', 'New Delhi', '15:30', '10:50', '19h 20m', '2025-04-23', '1A, 2A', '3A', 'SL', 'GN'),
('Maurya Express', '15027', 'Hatia', 'Gorakhpur', '19:10', '13:30', '18h 20m', '2025-04-24', '2A', '3A', 'SL', 'GN'),
('Patna Jan Shatabdi', '15125', 'Patna', 'Banaras', '05:30', '10:30', '5h 00m', '2025-04-25', 'CC', '2S', '', ''),
('Tejas Rajdhani', '12309', 'Rajendra Nagar', 'New Delhi', '19:10', '07:40', '12h 30m', '2025-04-26', '1A, 2A, 3A', '', '', ''),
('Patliputra Express', '18622', 'Patna', 'Howrah', '15:20', '06:10', '14h 50m', '2025-04-27', '2A', '3A', 'SL', ''),
('Humsafar Express', '22354', 'Patna', 'Bangalore', '20:00', '10:30', '38h 30m', '2025-04-28', '3A', 'SL', '', ''),
('Gaya Express', '12397', 'Gaya', 'New Delhi', '14:30', '07:45', '17h 15m', '2025-04-29', '1A, 2A', '3A', 'SL', 'GN'),
('Vande Bharat', '22436', 'Varanasi', 'Patna', '06:00', '10:00', '4h 00m', '2025-04-30', 'EC', 'CC', '', ''),
('Intercity Express', '13247', 'Rajgir', 'Howrah', '06:00', '16:45', '10h 45m', '2025-05-01', '2A', '3A', 'SL', ''),
('Pataliputra Exp', '12141', 'Mumbai', 'Patna', '23:30', '07:00', '31h 30m', '2025-05-02', '2A', '3A', 'SL', 'GN');
