import streamlit as st
import pandas as pd
from dbconnect import get_connection
import authunicate as auth
from datetime import datetime, time, date
import datetime
import random
import qrcode
import io

if "page" not in st.session_state:
    st.session_state.page="login"

st.set_page_config(
    page_title="🚀 Team 4A | Travel Hub",
    page_icon="🧭",
    layout="centered"
)

def login():
    st.title("Login")
    auth.create_Table()
    with st.form("login_form"):
        email=st.text_input("Email", placeholder="Enter your email")
        email=email.strip()

        password=st.text_input("Password", type="password", placeholder="Enter your password")
        password=password.strip()
        remember=st.checkbox("Remember me")
        col1,col2,col3,col4,col5,col6=st.columns(6)
        with col1:
            login_button=st.form_submit_button("Log In")
        with col6:
            signup_button=st.form_submit_button("sign up")
        if login_button:
            user =auth.check_user(email,password)
            if user:
                st.session_state.email=email
                st.session_state.user=user[0]
                st.success("✅ Successfully login")
                st.session_state.page="Home"
                st.rerun()
            else:
                st.warning("User not found. Please sign up.")   
        elif signup_button:
            st.session_state.page="signup"


def sign_up():
    st.title("Sign-Up")
    with st.form("signup_form"):
        col6, col7=st.columns(2)
        with col6:
            first_name=st.text_input("First name", placeholder="Enter your first name")
            first_name=first_name.strip()
        with col7:
            last_name=st.text_input("Last name", placeholder="Enter your last name")    
            last_name=last_name.strip() 
        
        col1,col2=st.columns(2)
        with col1:
            email=st.text_input("Email", placeholder="Enter your email")
            email=email.strip()
        with col2:
            password=st.text_input("Password", type="password", placeholder="Enter your password")
            password=password.strip()
    
        col8,col9=st.columns(2)
        with col8:
            mob_num=st.text_input("Mobile number",placeholder="Enter your mobile number")
            mob_num=mob_num.strip()
        with col9:
            gender=st.selectbox("Gender",("Select","Male","Female","Other"))
            
        address=st.text_input("Address", placeholder="Enter your full address")

        col3,col4,col5=st.columns([2, 1.5, 1])
        with col3:
            city=st.text_input("City")
        with col4:
            state=st.selectbox("State",[
                "Select",
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        "Bihar",
        "Chhattisgarh",
        "Goa",
        "Gujarat",
        "Haryana",
        "Himachal Pradesh",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Madhya Pradesh",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Punjab",
        "Rajasthan",
        "Sikkim",
        "Tamil Nadu",
        "Telangana",
        "Tripura",
        "Uttar Pradesh",
        "Uttarakhand",
        "West Bengal"
    ]
    )
        with col5:
            pin_code=st.text_input("Pin-code")

        col10,a,b,c,d,col11=st.columns(6)
        with col10:
            submitted=st.form_submit_button("Sign Up")
        with col11:
            logn=st.form_submit_button("Log in")

        if submitted:
            if first_name and last_name and email and password and mob_num and gender and address and city and state and pin_code:
                data=(first_name,last_name,email,password,mob_num,gender,address,city,state,pin_code)
                auth.create_Table()
                auth.register_user(data)
                st.success("✅ Sign-up successful!")
                st.session_state.page="login"
                st.rerun()
            else:
                st.warning("Plz Enter all field.")
        elif logn:
            st .session_state.page="login"
        

if st.session_state.page not in ["login", "signup"]:
    st.sidebar.markdown("<h1 style='text-align: center; font-size:2rem; font-weight:bolder; color: black;'>🌍 Travel Hub</h1>", unsafe_allow_html=True)

    st.sidebar.markdown("""
        <style>
        .nav-button {
            background-color: #0d6efd;
            color: white;
            font-weight: 600;
            padding: 0.5rem 1.2rem;
            margin: 0.3rem 0;
            border: none;
            border-radius: 0.5rem;
            cursor: pointer;
            width: 100%;
            transition: all 0.3s ease;
            text-align: center;
            display: block;
        }
        .nav-button:hover {
            background-color: #20c997;
            color: black;
        }
        .nav-form {
            display: flex;
            flex-direction: column;
            align-items: stretch;
        }
        </style>
    """,unsafe_allow_html=True)

    with st.sidebar.form("nav_form",clear_on_submit=False):
        st.markdown('<div class="nav-form">',unsafe_allow_html=True)
        home_btn = st.form_submit_button("🏠 Home",use_container_width=True)
        restaurant_btn = st.form_submit_button("🍽 Restaurant",use_container_width=True)
        ticket_btn = st.form_submit_button("🎫 Show-Ticket",use_container_width=True)
        flight_btn = st.form_submit_button("✈ Book-Flight Ticket",use_container_width=True)
        metro_btn = st.form_submit_button("🚇 Book-Metro Ticket",use_container_width=True)
        cab_btn= st.form_submit_button("🚕 Book-Cab",use_container_width=True)
        user_btn = st.form_submit_button("👤 View-Profile",use_container_width=True)
        about_btn = st.form_submit_button("👥 Meet Our Developers",use_container_width=True)
        help_btn = st.form_submit_button("🤝 Contact & Support",use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)


        if home_btn:
            st.session_state.page = "Home"
            st.session_state.homepage='search'
        if restaurant_btn:
            st.session_state.page = "Restaurant"
        elif ticket_btn:
            st.session_state.page = "Ticket"
        elif user_btn:
            st.session_state.page = "User"
        elif about_btn:
            st.session_state.page = "About"
        elif metro_btn:
            st.session_state.page = "Metro"
        elif cab_btn:
            st.session_state.page = "Cab"
        elif help_btn:
            st.session_state.page = "Help"  
        elif flight_btn:
            st.session_state.page = "Flight" 

def home():
    username=st.session_state.get('email')

    if "homepage" not in st.session_state:
        st.session_state.homepage="search"
    def showSearchForm():
        st.markdown("<h1 style='text-align: center; color: #000000;'>🚆 Train Ticket Booking</h1>", unsafe_allow_html=True)
        st.markdown("### Search for Trains")
        col1,col2,col3=st.columns(3)
        with col1:
            source=st.text_input("From", key="source", placeholder="Enter Source Station")
            source=source.capitalize()
            source=source.strip()
        with col2:
            destination=st.text_input("To", key="destination", placeholder="Enter Destination")
            destination=destination.capitalize()
            destination=destination.strip()
        with col3:
            travel_date=st.date_input("Date of Travel", key="date")

        if st.button("🔍 Search Trains"):
            auth.create_train_Table()
            auth.create_Passenser_Table()
            if source and destination:
                st.session_state.search_results=auth.search_train(source,destination)
                if st.session_state.search_results:
                    st.session_state.showt=auth.search_train(source,destination)
                    st.session_state.homepage="results"
                    st.rerun()
                else:
                    st.warning("No train found for this route")
            else:
                st.warning("Please fill all the fields to search trains.")

    def showResults():
        st.title("📋 Available Trains")
        search_results = st.session_state.get("search_results")
        with st.container():
            st.subheader(f"{search_results[0]} ({search_results[1]}) — {search_results[7]}")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown(f"🕔 *{search_results[4]} | {search_results[2].upper()}*")
            with col2:
                st.markdown(f"⏱ *{search_results[6]}*")
            with col3:
                st.markdown(f"🌙 *{search_results[5]} | {search_results[3].upper()}*")
            if st.button("Book"):
                st.session_state.homepage ="book"
                # showClass()
                st.rerun() 


    
    def showClass():
        import random 
        st.title("🎟 Book Ticket")
        search_results = st.session_state.get("showt")
        st.header(f"{search_results[0]} {search_results[1]} — {search_results[7]}")
        col1, col2, col3=st.columns(3)
        with col1:
            st.markdown(f"🕔 *{search_results[4]} | {search_results[2]}*")
        with col2:
            st.markdown(f"⏱ *{search_results[6]}*")
        with col3:
            st.markdown(f"🌙 *{search_results[5]} | {search_results[3]}*")

        st.markdown("---")

        col4,col5,col6=st.columns([1, 2, 1])
        with col5:
            st.markdown("### Select Class & Passengers")
            booking_class=st.selectbox(
            "🛏 Booking Class",
            options=[
                search_results[8], 
                search_results[9], 
                search_results[10], 
                search_results[11]
            ])
            passengernum=st.number_input("👥 Number of Passengers", min_value=1, max_value=5, step=1)

        st.markdown("---")
    
        pnr="Pnr"+str(random.randint(10000,99999))
        seat=random.randint(100,999)
    
        for i in range(passengernum):
            st.subheader(f"Passenger {i + 1}")
            col_name,col_age,col_gender=st.columns(3)

            with col_name:
                name=st.text_input(f"Name {i+1}", placeholder="Enter your name")
            with col_age:
                age=st.text_input(f"Age {i+1}", placeholder="Enter your age")
              
            with col_gender:
                gender=st.selectbox(
                    f"Gender {i+1}",
                    options=[None, "Male", "Female", "Other"],
                )
            if name and age and gender:
                if st.button(f"✅ Book Ticket {i+1}"):
                    data=[username,pnr,name,search_results[2],search_results[3],booking_class,seat]
                    auth.register_passengers(data)
                    if i==passengernum-1:
                        st.success("🎉 Ticket Booked!")
                        st.session_state.homepage="search"
            else:
                st.error("⚠ Please fill all fields properly before booking.")
        

    if st.session_state.homepage == "search":
        showSearchForm()
    if st.session_state.homepage == "results":
        showResults()
    elif st.session_state.homepage == "book":
        showClass()


def restro():
    return {
        "Delhi": {
            "Chandni Chowk Diner": {
                "Chole Bhature": 80, "Rajma Chawal": 90, "Aloo Tikki": 50, "Paneer Tikka": 120,
                "Butter Chicken": 180, "Kebabs": 150, "Paratha": 40, "Kathi Roll": 60, "Jalebi": 30, "Lassi": 50
            },
            "Rajdhani Rasoi": {
                "Dal Makhani": 100, "Shahi Paneer": 140, "Naan": 25, "Bhindi Masala": 90,
                "Samosa": 20, "Kheer": 50, "Tandoori Roti": 20, "Pakora": 40, "Gulab Jamun": 40, "Dahi Bhalla": 35
            }
        },
        "Mumbai": {
            "Marine Drive Bites": {
                "Vada Pav": 25, "Pav Bhaji": 80, "Misal Pav": 60, "Bombay Sandwich": 50, "Bhel Puri": 40,
                "Sev Puri": 35, "Ragda Pattice": 45, "Pani Puri": 30, "Falooda": 70, "Kulfi": 60
            },
            "Bollywood Treats": {
                "Tandoori Chicken": 180, "Veg Kolhapuri": 120, "Fish Thali": 200, "Chicken Frankie": 90,
                "Batata Vada": 20, "Mango Lassi": 50, "Kombdi Vade": 160, "Upma": 40, "Idli": 30, "Sheera": 35
            }
        },
        "Bengaluru": {
            "Silicon Spice": {
                "Masala Dosa": 60, "Set Dosa": 55, "Bisibele Bath": 70, "Rava Idli": 40, "Vangi Bath": 65,
                "Filter Coffee": 25, "Mysore Pak": 30, "Bonda": 20, "Kesari Bath": 35, "Akki Roti": 50
            },
            "Garden City Grill": {
                "Chicken Ghee Roast": 170, "Mangalorean Fish Curry": 180, "Paneer Ghee Roast": 150,
                "Neer Dosa": 40, "Kori Roti": 60, "Veg Pulao": 70, "Rasam": 25, "Appam": 35,
                "Pineapple Sheera": 30, "Idli-Vada Combo": 40
            }
        },
        "Kolkata": {
            "Bengali Bhoj": {
                "Shorshe Ilish": 220, "Chingri Malai Curry": 200, "Beguni": 30, "Luchi": 25, "Aloo Posto": 70,
                "Kosha Mangsho": 190, "Macher Jhol": 160, "Sandesh": 40, "Mishti Doi": 35, "Pulao": 80
            },
            "Howrah Bites": {
                "Mughlai Paratha": 60, "Ghugni": 50, "Kolkata Rolls": 70, "Telebhaja": 30, "Fish Fry": 100,
                "Chowmein": 90, "Chhanar Dalna": 85, "Rosogolla": 20, "Paturi": 110, "Labra": 60
            }
        },
        "Chennai": {
            "Marina Meals": {
                "Idli": 20, "Dosa": 40, "Vada": 20, "Sambar": 25, "Rasam": 25,
                "Pongal": 35, "Kootu": 45, "Poriyal": 40, "Thayir Sadam": 30, "Payasam": 40
            },
            "South Spice": {
                "Chettinad Chicken": 160, "Parotta": 25, "Kothu Parotta": 60, "Fish Fry": 100,
                "Kuzhambu": 70, "Lemon Rice": 40, "Tamarind Rice": 45, "Filter Coffee": 25,
                "Murukku": 15, "Adai": 35
            }
        },
        "Hyderabad": {
            "Biryani House": {
                "Hyderabadi Biryani": 150, "Mirchi Ka Salan": 50, "Double Ka Meetha": 40, "Pathar Ka Gosht": 180,
                "Chicken 65": 100, "Haleem": 120, "Khubani Ka Meetha": 50, "Bagara Baingan": 70,
                "Sheermal": 30, "Kheema": 130
            },
            "Charminar Treats": {
                "Lukhmi": 40, "Nihari": 170, "Mutton Curry": 180, "Paya Soup": 90, "Osmania Biscuit": 10,
                "Irani Chai": 15, "Dum Ka Murgh": 150, "Malai Korma": 140, "Falooda": 60, "Paneer Biryani": 130
            }
        },
        "Ahmedabad": {
            "Gujju Rasoi": {
                "Dhokla": 30, "Khandvi": 35, "Undhiyu": 80, "Fafda": 20, "Jalebi": 30,
                "Thepla": 25, "Handvo": 40, "Sev Tameta": 45, "Dal Dhokli": 55, "Shrikhand": 50
            },
            "Sabarmati Snacks": {
                "Khakra": 20, "Bhakhri": 25, "Patra": 30, "Muthiya": 35, "Lilva Kachori": 40,
                "Chorafali": 30, "Mag Ni Dal": 45, "Gathiya": 25, "Churma Ladoo": 30, "Chaas": 15
            }
        },
        "Jaipur": {
            "Pink City Thali": {
                "Dal Baati Churma": 120, "Gatte ki Sabzi": 80, "Ker Sangri": 75, "Laal Maas": 200,
                "Mawa Kachori": 40, "Mirchi Vada": 25, "Onion Kachori": 30, "Rabri": 45,
                "Panchmel Dal": 60, "Bajra Roti": 20
            },
            "Rajputana Flavors": {
                "Besan Gatta": 70, "Methi Bajra Puri": 25, "Papad Mangodi": 50, "Boondi Raita": 30,
                "Kalmi Vada": 45, "Aloo Pyaz Sabzi": 55, "Ghevar": 60, "Malpua": 50,
                "Churma": 40, "Masala Chach": 15
            }
        },
        "Lucknow": {
            "Awadhi Aroma": {
                "Galouti Kebab": 180, "Kakori Kebab": 190, "Lucknawi Biryani": 160, "Sheermal": 30,
                "Rogan Josh": 200, "Roomali Roti": 20, "Shahi Tukda": 50, "Nihari": 180,
                "Korma": 160, "Kulcha": 25
            },
            "Tehzeeb Tandoor": {
                "Tunday Kebab": 160, "Mutton Biryani": 170, "Chicken Rezala": 150, "Keema": 140,
                "Zafrani Pulao": 120, "Paya": 100, "Seekh Kebab": 150, "Paneer Masala": 130,
                "Firni": 50, "Halwa": 40
            }
        },
        "Amritsar": {
            "Golden Dhaba": {
                "Amritsari Kulcha": 60, "Chole": 50, "Paneer Bhurji": 90, "Rajma": 70,
                "Sarson da Saag": 80, "Makki di Roti": 30, "Lassi": 40, "Tandoori Roti": 20,
                "Aloo Gobhi": 60, "Kheer": 35
            },
            "Punjabi Zaika": {
                "Butter Chicken": 190, "Paneer Tikka": 130, "Murg Makhani": 180, "Bhuna Gosht": 170,
                "Paratha": 25, "Pakora": 30, "Chana Masala": 60, "Dahi Bhalla": 40, "Barfi": 30, "Jalebi": 25
            }
        }
    }


def Resturant():
    st.markdown("<h1 style='text-align: center; color: #BF9264;'>🥣 Train Restaurant Ordering System 🍽</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: gray;'>Part of the Indian Rail Management System (RMS)</h4>", unsafe_allow_html=True)
    st.markdown("---")
    data = restro()
    with st.container():
        col1,col2=st.columns(2)
        with col1:
            city=st.selectbox("📍 Select a City", list(data.keys()))
        with col2:
            hotel=st.selectbox("🏨 Select a Hotel", list(data[city].keys()))


    service=st.selectbox("🛎 Choose Service Type", ["Dine-In", "Takeaway", "Seat Service"])
    menu=data[city][hotel]
    st.markdown(f"<h3 style='color:#FF0B55;'>🍛 Menu for <i>{hotel}</i>, {city}</h3>", unsafe_allow_html=True)

    st.markdown("---")
    selected_items={}
    with st.container():
        for dish, price in menu.items():
            qty=st.number_input(f"{dish}** — ₹{price}", min_value=0, max_value=10, step=1, key=dish)
            if qty > 0:
                selected_items[dish]=(qty, price)

    st.markdown("---")

    if selected_items:
        st.markdown("<h3 style='color: #00C851;'>🧾 Order Summary</h3>", unsafe_allow_html=True)
        total = 0
        for item, (qty, price) in selected_items.items():
            item_total=qty * price
            total += item_total
            st.write(f"✅ {item} x {qty} = ₹{item_total}")

        st.markdown(f"<h4 style='color: #ff9800;'>💰 Total: ₹{total}</h4>", unsafe_allow_html=True)
        st.markdown(f"🛎 Service Type Chosen: {service}")

        if st.button("✅ Place Order"):
            st.success(f"🎉 Order placed successfully for {service}! Enjoy your meal! 😋")
    else:
        st.info("🍽 Please select at least one item to place an order.")




def view_tickets():
    st.title("🎟 View Booked Tickets")
    st.session_state.tickets=auth.get_passengers(st.session_state.email)

    if not st.session_state.tickets:
        st.info("No tickets booked.")
        return

    for i in range(len(st.session_state.tickets)):
        ticket=st.session_state.tickets
        with st.expander(f"🎫 Ticket {i + 1} — PNR: {ticket[i][1]}"):
            col1,col2,col3,col4,col5,col6=st.columns(6)
            with col1:
                st.markdown(f"*Passenger Name:* {ticket[i][2]}")
            with col2:
                st.markdown(f"*PNR Number:* {ticket[i][1]}")
            with col3:
                st.markdown(f"*Source:*<br>{ticket[i][3]}", unsafe_allow_html=True)
            with col4:
                st.markdown(f"*Destination:* {ticket[i][4]}")
            with col5:
                st.markdown(f"*Class:* {ticket[i][5]}")
            with col6:
                st.markdown(f"*Seat Number:* {ticket[i][6]}")

            if st.button(f"❌ Cancel Ticket {ticket[i][1]}"):
                st.success(f"Ticket with PNR {ticket[i][1]} canceled.")
                auth.cancel_ticket(ticket[i][1])
        


def profile():
    st.title("👤 User Profile")
    if "email" in st.session_state:
        username=st.session_state.email
    else:
        st.warning("⚠ No user is currently logged in.")
        return

    data = auth.get_user(username) 
    if data is None:
        st.error("❌ User not found.")
        return
    
    user = {
        "First Name": data[0],
        "Last Name": data[1],
        "Email": data[2],
        "Mobile": data[4],
        "Gender": data[5],
        "Address": data[6],
        "City": data[7],
        "State": data[8],
        "Pin Code": data[9]
    }

    st.session_state.user_profile = user

    col1,col2=st.columns(2)

    with col1:
        st.subheader("🧾 Basic Information")
        st.write(f"First Name: {user['First Name']}")
        st.write(f"Last Name: {user['Last Name']}")
        st.write(f"Gender: {user['Gender']}")
        st.write(f"Mobile: {user['Mobile']}")

    with col2:
        st.subheader("📬 Contact Information")
        st.write(f"Email: {user['Email']}")
        st.write(f"Address: {user['Address']}")
        st.write(f"City: {user['City']}")
        st.write(f"State: {user['State']}")
        st.write(f"Pin Code: {user['Pin Code']}")

    st.markdown("---")
    col1,col2=st.columns(2)
    with col1:
        if st.button("🚪 Log Out"):
            st.session_state.user_profile=None
            st.session_state.email=None
            st.success("You have been logged out.")
            st.session_state.page='login'
    with col2:
        # st.session_state.edit_mode = False
        if st.button('✏ Edit'):
            st.session_state.edit_mode = True

    if st.session_state.get("edit_mode", False):
        with st.form("edit_form"):
            st.subheader("✏ Edit Profile")
            first_name=st.text_input('First Name', placeholder='Enter new first name')
            last_name=st.text_input('Last Name',  placeholder='Enter new last name')
            password=st.text_input('Password', type="password", placeholder='Enter new password')

            submitted=st.form_submit_button("Update")
            if first_name and last_name and password:
                if submitted:
                    if auth.update_details(first_name,last_name,password,username):
                        st.success("Details updated sucessfully!")
                        st.session_state.edit_mode = False
                        st.session_state.page='User'
                        st.rerun()
            else:
                st .warning("please fill all fields")

def profile():
    st.title("👤 User Profile")
    if "email" in st.session_state:
        username=st.session_state.email
    else:
        st.warning("⚠ No user is currently logged in.")
        return

    data = auth.get_user(username) 
    if data is None:
        st.error("❌ User not found.")
        return
    
    user = {
        "First Name": data[0],
        "Last Name": data[1],
        "Email": data[2],
        "Mobile": data[4],
        "Gender": data[5],
        "Address": data[6],
        "City": data[7],
        "State": data[8],
        "Pin Code": data[9]
    }

    st.session_state.user_profile = user

    col1,col2=st.columns(2)

    with col1:
        st.subheader("🧾 Basic Information")
        st.write(f"First Name: {user['First Name']}")
        st.write(f"Last Name: {user['Last Name']}")
        st.write(f"Gender: {user['Gender']}")
        st.write(f"Mobile: {user['Mobile']}")

    with col2:
        st.subheader("📬 Contact Information")
        st.write(f"Email: {user['Email']}")
        st.write(f"Address: {user['Address']}")
        st.write(f"City: {user['City']}")
        st.write(f"State: {user['State']}")
        st.write(f"Pin Code: {user['Pin Code']}")

    st.markdown("---")
    col1,col2=st.columns(2)
    with col1:
        if st.button("🚪 Log Out"):
            st.session_state.user_profile=None
            st.session_state.email=None
            st.success("You have been logged out.")
            st.session_state.page='login'
    with col2:
        # st.session_state.edit_mode = False
        if st.button('✏ Edit'):
            st.session_state.edit_mode = True

    if st.session_state.get("edit_mode", False):
        with st.form("edit_form"):
            st.subheader("✏ Edit Profile")
            first_name=st.text_input('First Name', placeholder='Enter new first name')
            last_name=st.text_input('Last Name',  placeholder='Enter new last name')
            password=st.text_input('Password', type="password", placeholder='Enter new password')

            submitted=st.form_submit_button("Update")
            if first_name and last_name and password:
                if submitted:
                    if auth.update_details(first_name,last_name,password,username):
                        st.success("Details updated sucessfully!")
                        st.session_state.edit_mode = False
                        st.session_state.page='User'
                        st.rerun()
            else:
                st .warning("please fill all fields")


def about_dev():
    st.markdown("""
        <style>
            .dev-card {
                background-color: #f5f5f5;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 4px 4px 12px rgba(0,0,0,0.6);
                transition: transform 0.2s;
            }
            .dev-card:hover {
                transform: scale(1.02);
                box-shadow: 6px 6px 20px rgb(15, 10, 222);
            }
            .dev-name {
                font-size: 22px;
                font-weight: bold;
                color: #4a4a4a;
            }
            .dev-bio {
                font-size: 16px;
                color: #333333;
                margin-bottom: 15px;
            }
            .linkedin-link {
                font-size: 16px;
                color: #0072b1;
                text-decoration: none;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("# 👨‍💻Meet Minds Behind the Code")

    developers1=[
        {
            "name": "Ayush Raj Pathak",
            "bio": "A passionate problem solver and a code enthusiast, Ayush is a 2nd-year BCA student known for his leadership and vision. With a rock-solid command over C, C++, Java, Python, MySQL, React, and Node.js, he has spearheaded several impactful projects and led his team to victory in multiple inter-college hackathons. His hunger for innovation, paired with sharp debugging instincts, makes him a core pillar of the development squad. Ayush doesn't just code — he creates experiences.",
            "linkedin": "https://www.linkedin.com/in/ayush-raj-pathak05"
        },
        {
            "name": "Ajit Kumar Gupta",
            "bio": "Ajit is a coding prodigy who blends logic and creativity with remarkable ease. Currently in his 2nd year, he has already gained expertise in C, C++, Java, Python, MySQL, React. Known for his calm problem-solving approach and strong backend skills, Ajit has been instrumental in developing several robust and scalable applications. His contributions have consistently led his team to gold in both college and inter-college hackathons. Ajit is the go-to guy when it comes to building powerful tech that just works.",
            "linkedin": "https://www.linkedin.com/in/ajit-kumar-gupta-89405b297"
        }
    ]
    developers2=[
        {
            "name": "Anuj Saini",
            "bio": "Focused, innovative, and driven by curiosity, Anuj is a 2nd-year developer who thrives in solving real-world problems with clean and efficient code. Whether it's Java logic,C, C++, Python React components, or database schemas in MySQL, he handles it all with flair. Anuj’s ability to think out of the box has helped the team bag top spots in multiple hackathons. His dedication to continuous learning and excellence makes him a cornerstone of the dev team. With Anuj onboard, innovation is always just a sprint away.",
            "linkedin": "https://www.linkedin.com/posts/anuj-saini-48a17b297"
        },
        {
            "name": "Anu Sharma",
            "bio": "Smart, sharp, and solution-oriented — Anu brings energy and precision to every project. As a 2nd-year techie, her fluency in both frontend and backend technologies including React, Node.js, and MySQL, along with deep knowledge of C, C++, Java, and Python, enables her to build full-stack applications with finesse. Her knack for turning complex problems into elegant code has earned her and her team more than two 1st-place finishes in high-stakes hackathons. Anu is not just a developer — she’s a creative architect of digital solutions.",
            "linkedin": "https://www.linkedin.com/in/anu-sharma05"
        }
    ]

    def display_devs(developers):
        cols=st.columns(2)
        for col,dev in zip(cols, developers):
            with col:
                st.markdown(f"""
                    <div class="dev-card">
                        <div class="dev-name">{dev["name"]}</div>
                        <div class="dev-bio">{dev["bio"]}</div>
                        <a class="linkedin-link" href="{dev['linkedin']}" target="_blank">🔗 LinkedIn</a>
                    </div>
                """, unsafe_allow_html=True)
    display_devs(developers1)
    st.markdown("---")
    display_devs(developers2)


def help():
    # st.set_page_config(page_title="Support & Help", layout="centered")
    st.title("🛟 Support & Help")
    st.markdown("Need help with something? Select a category and let us know what's wrong!")
    options = [
        "Home",
        "Restaurant",
        "Show Ticket Booking",
        "Metro Ticket Booking",
        "Cab Booking",
        "View Profile"
    ]
    selected_option = st.selectbox("🔽 Select a category:", options)
    problem = st.text_area("📝 Describe the problem you are facing:")
    if st.button("🚀 Send Bug"):
        if problem.strip() == "":
            st.warning("Please describe the problem before submitting.")
        else:
            st.success("✅ Thank you for contacting us! We will get back to you soon.")


def cab():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url('background.png') no-repeat center center fixed;
            background-size: cover;
        }}
        .stButton > button {{
            background-color: #ffcc00;
            color: black;
            font-weight: bold;
            font-size: 16px;
            border-radius: 8px;
            height: 3em;
            width: 100%;
            margin-top: 1rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    def mock_calculate_distance_km(pickup, destination):
        return round(random.uniform(2, 25), 2)

    def estimate_fare(vehicle, distance):
        rates = {
            "Bike": {"base": 20, "per_km": 5},
            "Auto": {"base": 30, "per_km": 8},
            "Mini Cab": {"base": 40, "per_km": 10},
            "Sedan": {"base": 50, "per_km": 12}
        }
        if vehicle in rates:
            return round(rates[vehicle]["base"] + rates[vehicle]["per_km"] * distance, 2)
        return 0

    locations = [
        None,
        "Meerut Cantt",
        "Begum pul",
        "Abu Lane",
        "Sadar Bazaar",
        "Suraj Kund Park",
        "Augarnath Temple",
        "Ecological Park",
        "Shopprix Mall",
        "PL Sharma Road",
        "Mangal Pandey Park",
        "Lohia Nagar",
        "Shastri Nagar",
        "Ganga Nagar",
        "Rohta Road",
        "Jagrati Vihar",
        "Hapur Adda",
        "Mawana Road",
        "Transport Nagar",
        "Delhi Road",
        "PVS Mall",
        "Other"
    ]
    st.title("Book Your Cab 🚕")
    pickup_selection = st.selectbox("📍 Pickup Location", locations)
    pickup_location = st.text_input("✏ Enter Pickup Location", placeholder="Type your location") if pickup_selection == "Other" else pickup_selection 
    destination_selection = st.selectbox("🏁 Destination", locations)
    destination = st.text_input("✏ Enter Destination", placeholder="Type your destination") if destination_selection == "Other" else destination_selection

    vehicle_type = st.selectbox("🛵 Choose Vehicle", ["Bike", "Auto", "Mini Cab", "Sedan"])

    option = st.radio("🕒 Arrival Time Preference", [
        "🚆 When train arrives",
        "⏰ Set custom arrival time"
    ])

    selected_date = st.date_input("📅 Date", value=date.today())

    if "custom" in option.lower():
        selected_time = st.time_input("🕒 Time", value=time(12, 0))
    else:
        selected_time = time(0, 0)

    if "distance_km" not in st.session_state:
        st.session_state.distance_km = None

    distance_km = None
    estimated_fare = None
    if pickup_location and destination:
        if pickup_location == destination:
            st.warning("⚠ Pickup and Destination cannot be the same.")
        else:
            if (
                st.session_state.get("last_pickup") != pickup_location or
                st.session_state.get("last_destination") != destination
            ):
                st.session_state.last_pickup = pickup_location
                st.session_state.last_destination = destination
                st.session_state.distance_km = mock_calculate_distance_km(pickup_location, destination)

            distance_km = st.session_state.distance_km
            estimated_fare = estimate_fare(vehicle_type, distance_km)
            st.info(f"""
            📏 Approximate Distance: {distance_km} km  
            💰 Estimated Fare: ₹{estimated_fare}
            """)

    if st.button("🚕 Book Ride Now"):
        if pickup_location == destination:
            st.error("❌ Pickup and Destination cannot be the same.")
        elif not pickup_location or not destination:
            st.error("❌ Please enter both Pickup and Destination.")
        else:
            arrival_type = "Train Arrival" if "train" in option.lower() else "Custom Time"
            time_display = "As per train arrival" if arrival_type == "Train Arrival" else selected_time.strftime('%H:%M')

            st.success(f"""
            ✅ Booking Confirmed!
            📍 Pickup: {pickup_location}  
            🏁 Destination: {destination}  
            🚘 Vehicle: {vehicle_type}  
            💰 Estimated Fare: ₹{estimated_fare if estimated_fare else 'N/A'}  
            🗓 Date: {selected_date}  
            ⏰ Time: {time_display}  
            📌 Arrival: {arrival_type}  
            📏 Distance: {f"{distance_km} km" if distance_km else "N/A"}
            """)


def flight():
    flights_data = [
    {"flight_no": "AI202", "origin": "Delhi", "destination": "Mumbai", "time": "10:00 AM"},
    {"flight_no": "6E101", "origin": "Mumbai", "destination": "Bangalore", "time": "1:00 PM"},
    {"flight_no": "SG333", "origin": "Chennai", "destination": "Kolkata", "time": "5:00 PM"},
    {"flight_no": "AI305", "origin": "Delhi", "destination": "Chennai", "time": "9:00 AM"},
    {"flight_no": "6E204", "origin": "Bangalore", "destination": "Delhi", "time": "11:30 AM"},
    {"flight_no": "SG122", "origin": "Hyderabad", "destination": "Ahmedabad", "time": "3:15 PM"},
    {"flight_no": "AI450", "origin": "Pune", "destination": "Kolkata", "time": "7:45 PM"},
    {"flight_no": "6E302", "origin": "Kolkata", "destination": "Mumbai", "time": "6:50 AM"},
    {"flight_no": "SG404", "origin": "Jaipur", "destination": "Hyderabad", "time": "8:20 AM"},
    {"flight_no": "AI789", "origin": "Delhi", "destination": "Pune", "time": "4:00 PM"},
    {"flight_no": "6E509", "origin": "Mumbai", "destination": "Chennai", "time": "6:15 PM"},
    {"flight_no": "SG888", "origin": "Bangalore", "destination": "Lucknow", "time": "5:45 AM"},
    {"flight_no": "AI666", "origin": "Lucknow", "destination": "Delhi", "time": "2:00 PM"},
    {"flight_no": "6E777", "origin": "Kolkata", "destination": "Chennai", "time": "10:30 AM"},
    {"flight_no": "SG909", "origin": "Hyderabad", "destination": "Mumbai", "time": "1:50 PM"},
    {"flight_no": "AI121", "origin": "Delhi", "destination": "Ahmedabad", "time": "12:40 PM"},
    {"flight_no": "6E654", "origin": "Pune", "destination": "Delhi", "time": "3:25 PM"},
    {"flight_no": "SG717", "origin": "Chandigarh", "destination": "Bangalore", "time": "9:50 AM"},
    {"flight_no": "AI505", "origin": "Mumbai", "destination": "Jaipur", "time": "7:20 AM"},
    {"flight_no": "6E303", "origin": "Ahmedabad", "destination": "Chennai", "time": "4:30 PM"},
    {"flight_no": "SG401", "origin": "Kolkata", "destination": "Bhubaneswar", "time": "6:45 PM"},
    {"flight_no": "AI112", "origin": "Bhubaneswar", "destination": "Delhi", "time": "8:10 AM"},
    {"flight_no": "6E909", "origin": "Indore", "destination": "Mumbai", "time": "2:30 PM"},
    {"flight_no": "SG212", "origin": "Chennai", "destination": "Trivandrum", "time": "5:10 PM"},
    {"flight_no": "AI999", "origin": "Trivandrum", "destination": "Bangalore", "time": "7:40 AM"}
]

    st.title("✈ Flight Booking Portal")
    if "tickets" not in st.session_state:
        st.session_state.tickets = []
    if "main_menu" not in st.session_state:
        st.session_state.main_menu = "Book"

    st.markdown("""
    <style>
    .css-18e3th9 {
        padding-top: 0rem;
    }
    button[kind="primary"] {
        background-color: #4CAF50 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px 20px;
        margin: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    with cols[0]:
        if st.button("📖 Book Ticket"):
            st.session_state.main_menu = "Book"
    with cols[1]:
        if st.button("❌ Cancel Ticket"):
            st.session_state.main_menu = "Cancel"
    with cols[2]:
        if st.button("📄 View My Tickets"):
            st.session_state.main_menu = "View"
    with cols[3]:
        if st.button("📋 Flight Schedule"):
            st.session_state.main_menu = "Schedule"

    if st.session_state.main_menu == "Book":
        st.subheader("Book a Flight Ticket")
        name = st.text_input("Your Name")
        selected_flight = st.selectbox(
            "Select Flight",
            [f"{f['flight_no']} | {f['origin']} → {f['destination']} | {f['time']}" for f in flights_data]
        )
        date = st.date_input("Travel Date", min_value=datetime.date.today())

        if st.button("Book Ticket", type="primary"):
            if name:
                ticket_id = f"TKT{len(st.session_state.tickets) + 1:03d}"
                st.session_state.tickets.append({
                    "ticket_id": ticket_id,
                    "name": name,
                    "flight": selected_flight,
                    "date": date
                })
                st.success(f"✅ Ticket Booked! Your Ticket ID: {ticket_id}")
            else:
                st.warning("Please enter your name before booking.")

    elif st.session_state.main_menu == "Cancel":
        st.subheader("Cancel a Ticket")
        ticket_id = st.text_input("Enter Ticket ID to Cancel")
        if st.button("Cancel Ticket", type="primary"):
            original_count = len(st.session_state.tickets)
            st.session_state.tickets = [
                t for t in st.session_state.tickets if t["ticket_id"] != ticket_id
            ]
            if len(st.session_state.tickets) < original_count:
                st.success(f"❌ Ticket {ticket_id} has been cancelled.")
            else:
                st.error("Ticket ID not found.")

    elif st.session_state.main_menu == "View":
        st.subheader("Your Booked Tickets")
        if st.session_state.tickets:
            for ticket in st.session_state.tickets:
                st.info(
                    f"🎫 Ticket ID: {ticket['ticket_id']}\n\n"
                    f"👤 Name: {ticket['name']}\n"
                    f"✈ Flight: {ticket['flight']}\n"
                    f"📅 Date: {ticket['date']}"
                )
        else:
            st.warning("You have no tickets booked yet.")

    elif st.session_state.main_menu == "Schedule":
        st.subheader("Available Flights Today")
        for flight in flights_data:
            st.write(f"✈ {flight['flight_no']} - {flight['origin']} → {flight['destination']} at {flight['time']}")


def metro():
    metro_data = [
    {"train_no": "M101", "origin": "Rajiv Chowk", "destination": "Kashmere Gate", "time": "06:00 AM"},
    {"train_no": "M102", "origin": "Kashmere Gate", "destination": "Yamuna Bank", "time": "06:30 AM"},
    {"train_no": "M103", "origin": "Yamuna Bank", "destination": "Noida City Centre", "time": "07:00 AM"},
    {"train_no": "M104", "origin": "Noida Sector 18", "destination": "Botanical Garden", "time": "07:30 AM"},
    {"train_no": "M105", "origin": "Dwarka Sector 21", "destination": "Rajiv Chowk", "time": "08:00 AM"},
    {"train_no": "M106", "origin": "Huda City Centre", "destination": "Saket", "time": "08:30 AM"},
    {"train_no": "M107", "origin": "Saket", "destination": "Central Secretariat", "time": "09:00 AM"},
    {"train_no": "M108", "origin": "Rithala", "destination": "Netaji Subhash Place", "time": "09:30 AM"},
    {"train_no": "M109", "origin": "Rajouri Garden", "destination": "Karol Bagh", "time": "10:00 AM"},
    {"train_no": "M110", "origin": "Inderlok", "destination": "Ashok Park Main", "time": "10:30 AM"},
    {"train_no": "M111", "origin": "AIIMS", "destination": "Lajpat Nagar", "time": "11:00 AM"},
    {"train_no": "M112", "origin": "Green Park", "destination": "Nehru Place", "time": "11:30 AM"},
    {"train_no": "M113", "origin": "Lajpat Nagar", "destination": "Okhla", "time": "12:00 PM"},
    {"train_no": "M114", "origin": "Sarai Kale Khan", "destination": "Ghaziabad", "time": "12:30 PM"},
    {"train_no": "M115", "origin": "Ghaziabad", "destination": "Modinagar", "time": "01:00 PM"},
    {"train_no": "M116", "origin": "Modinagar", "destination": "Meerut South", "time": "01:30 PM"},
    {"train_no": "M117", "origin": "Meerut South", "destination": "Meerut Central", "time": "02:00 PM"},
    {"train_no": "M118", "origin": "Meerut Central", "destination": "Modinagar", "time": "02:30 PM"},
    {"train_no": "M119", "origin": "Modinagar", "destination": "Ghaziabad", "time": "03:00 PM"},
    {"train_no": "M120", "origin": "Ghaziabad", "destination": "Anand Vihar", "time": "03:30 PM"},
    {"train_no": "M121", "origin": "Anand Vihar", "destination": "Rajiv Chowk", "time": "04:00 PM"},
    {"train_no": "M122", "origin": "Meerut Central", "destination": "Sarai Kale Khan", "time": "04:30 PM"},
    {"train_no": "M123", "origin": "Kashmere Gate", "destination": "Meerut South", "time": "05:00 PM"},
    {"train_no": "M124", "origin": "Botanical Garden", "destination": "Meerut Central", "time": "05:30 PM"},
]

    st.title("🚇 Metro Booking Portal")

    if "tickets" not in st.session_state:
        st.session_state.tickets = []
    if "main_menu" not in st.session_state:
        st.session_state.main_menu = "Book"

    st.markdown("""
    <style>
    .menu-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        background-color: #003366;
        border-radius: 12px;
        padding: 12px 0;
        margin-bottom: 20px;
    }
    .menu-btn {
        background-color: #005a9c;
        color: white;
        font-weight: bold;
        padding: 10px 24px;
        margin: 6px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-size: 15px;
        transition: 0.3s;
    }
    .menu-btn:hover {
        background-color: #007acc;
    }
    .ticket-card {
        background-color: #f0f8ff;
        padding: 10px 16px;
        border-left: 5px solid #005a9c;
        margin: 10px 0;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

    # st.markdown('<div class="menu-container">', unsafe_allow_html=True)
    # st.markdown('---')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🎟 Book Ticket", key="book"):
            st.session_state.main_menu = "Book"
    with col2:
        if st.button("❌ Cancel Ticket", key="cancel"):
            st.session_state.main_menu = "Cancel"
    with col3:
        if st.button("📄 View Tickets", key="view"):
            st.session_state.main_menu = "View"
    with col4:
        if st.button("🗓 Schedule", key="schedule"):
            st.session_state.main_menu = "Schedule"
    st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.main_menu == "Book":
        st.subheader("🎟 Book a Metro Ticket")
        name = st.text_input("👤 Your Name")
        qrname=name
        selected_metro = st.selectbox(
            "🚇 Select Metro",
            [f"{m['train_no']} | {m['origin']} → {m['destination']} | {m['time']}" for m in metro_data]
        )
        date = st.date_input("📅 Travel Date", min_value=datetime.date.today())

        if st.button("✅ Book Ticket"):
            if name:
                ticket_id = f"MT-{len(st.session_state.tickets)+1:03d}"
                st.session_state.tickets.append({
                    "ticket_id": ticket_id,
                    "name": name,
                    "train": selected_metro,
                    "date": date
                })
                st.success(f"🚇 Ticket Booked! Your Ticket ID: {ticket_id}")
                qr(qrname)
            else:
                st.warning("⚠ Please enter your name.")

    elif st.session_state.main_menu == "Cancel":
        st.subheader("❌ Cancel a Ticket")
        ticket_id = st.text_input("Enter Ticket ID")
        if st.button("Cancel Ticket"):
            count_before = len(st.session_state.tickets)
            st.session_state.tickets = [t for t in st.session_state.tickets if t["ticket_id"] != ticket_id]
            if len(st.session_state.tickets) < count_before:
                st.success(f"✅ Ticket {ticket_id} cancelled.")
            else:
                st.error("❌ Ticket ID not found.")

    elif st.session_state.main_menu == "View":
        st.subheader("📄 Your Booked Tickets")
        if st.session_state.tickets:
            for t in st.session_state.tickets:
                st.markdown(f"""
                <div class='ticket-card'>
                    <b>🎫 Ticket ID:</b> {t[0]}<br>
                    <b>👤 Name:</b> {t[1]}<br>
                    <b>🚇 Metro:</b> {t[2]}<br>
                    <b>📅 Date:</b> {t[3]}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No tickets booked yet.")

    elif st.session_state.main_menu == "Schedule":
        st.subheader("🗓 Metro Schedule Today")
        for m in metro_data:
            st.write(f"🚇 {m['train_no']} — {m['origin']} → {m['destination']} at {m['time']}")
    
def qr(data):
    data = "ayush"
    if data:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            buf = io.BytesIO()
            img.save(buf)
            buf.seek(0)
            st.image(buf)


st.markdown("---")
if st.session_state.page == "login":
    login()
elif st.session_state.page == "signup":
    sign_up()
elif st.session_state.page == "Home":
    home()
elif st.session_state.page == "Restaurant":
    Resturant()
elif st.session_state.page == "Ticket":
    view_tickets()
elif st.session_state.page == "User":
    profile() 
elif st.session_state.page == "About":
    about_dev()
elif st.session_state.page =="Metro":
    metro()
elif st.session_state.page == "Cab":
    cab()
elif st.session_state.page == "Help":
    help()
elif st.session_state.page == "Flight":
    flight()