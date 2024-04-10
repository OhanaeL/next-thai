import streamlit as st
import datetime
from streamlit.logger import get_logger
import google.generativeai as genai

LOGGER = get_logger(__name__)

genai.configure(api_key="AIzaSyCKNwQ2p9XA71CfMZF5Pfuq2flFjnZoK4k")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
budget_min = 1000
budget_max = 50000
if 'replyText' not in st.session_state:
    st.session_state['replyText'] = ''

def run():
    
    global replyText

    st.set_page_config(
        page_title="Next Thai",
        page_icon="👋",
    )

    st.markdown("# Customize Your Journey Here!")
    st.sidebar.header("Customize Your Journey Here!")

    today = datetime.datetime.now()

    max_year = datetime.date(today.year +5, 12, 31)

    start = st.sidebar.selectbox(
    'Starting Point',
    ("Amnat Charoen", "Ang Thong", "Bangkok", "Bueng Kan", "Chachoengsao", 
    "Chaiyaphum", "Chanthaburi", "Chiang Mai", "Chiang Rai", "Chonburi", 
    "Chumphon", "Hat Yai", "Kalasin", "Kamphaeng Phet", "Kanchanaburi", 
    "Khlong Luang", "Khon Kaen", "Krabi", "Lampang", "Lamphun", 
    "Laem Chabang", "Loei", "Lopburi", "Mae Sot", "Maha Sarakham", 
    "Mukdahan", "Nakhon Nayok", "Nakhon Pathom", "Nakhon Phanom", 
    "Nakhon Ratchasima (Korat)", "Nakhon Sawan", "Nakhon Si Thammarat", 
    "Nan", "Narathiwat", "Nong Bua Lamphu", "Nong Khai", "Nonthaburi", 
    "Pak Kret", "Pak Kret", "Pak Kret", "Pak Kret", "Pattaya", "Phang Nga", 
    "Phatthalung", "Phayao", "Phetchabun", "Phetchabun", "Phetchaburi", 
    "Phetchaburi", "Phichit", "Phitsanulok", "Phra Nakhon Si Ayutthaya", 
    "Phrae", "Phuket", "Prachin Buri", "Prachuap Khiri Khan", "Ranong", 
    "Ratchaburi", "Rayong", "Roi Et", "Sa Kaeo", "Sakon Nakhon", 
    "Samut Prakan", "Samut Sakhon", "Samut Songkhram", "Saraburi", 
    "Satun", "Sing Buri", "Si Racha", "Sisaket", "Songkhla", "Sukhothai", 
    "Suphan Buri", "Surat Thani", "Surin", "Tak", "Trang", "Trat", 
    "Ubon Ratchathani", "Udon Thani", "Uttaradit", "Uthai Thani", "Yala", 
    "Yasothon"))

    destinations = st.sidebar.multiselect(
    'Destination',
    ["Amnat Charoen", "Ang Thong", "Bangkok", "Bueng Kan", "Chachoengsao", 
    "Chaiyaphum", "Chanthaburi", "Chiang Mai", "Chiang Rai", "Chonburi", 
    "Chumphon", "Hat Yai", "Kalasin", "Kamphaeng Phet", "Kanchanaburi", 
    "Khlong Luang", "Khon Kaen", "Krabi", "Lampang", "Lamphun", 
    "Laem Chabang", "Loei", "Lopburi", "Mae Sot", "Maha Sarakham", 
    "Mukdahan", "Nakhon Nayok", "Nakhon Pathom", "Nakhon Phanom", 
    "Nakhon Ratchasima (Korat)", "Nakhon Sawan", "Nakhon Si Thammarat", 
    "Nan", "Narathiwat", "Nong Bua Lamphu", "Nong Khai", "Nonthaburi", 
    "Pak Kret", "Pak Kret", "Pak Kret", "Pak Kret", "Pattaya", "Phang Nga", 
    "Phatthalung", "Phayao", "Phetchabun", "Phetchabun", "Phetchaburi", 
    "Phetchaburi", "Phichit", "Phitsanulok", "Phra Nakhon Si Ayutthaya", 
    "Phrae", "Phuket", "Prachin Buri", "Prachuap Khiri Khan", "Ranong", 
    "Ratchaburi", "Rayong", "Roi Et", "Sa Kaeo", "Sakon Nakhon", 
    "Samut Prakan", "Samut Sakhon", "Samut Songkhram", "Saraburi", 
    "Satun", "Sing Buri", "Si Racha", "Sisaket", "Songkhla", "Sukhothai", 
    "Suphan Buri", "Surat Thani", "Surin", "Tak", "Trang", "Trat", 
    "Ubon Ratchathani", "Udon Thani", "Uttaradit", "Uthai Thani", "Yala", 
    "Yasothon"])

    duration = st.sidebar.date_input(
        "Duration Date",
        (today, today),
        today,
        max_year,
        format="MM.DD.YYYY")
    difference = 1
    if len(duration) > 1:
        difference = duration[1].day-duration[0].day + 1
    people = st.sidebar.number_input('How Many People?', min_value = 1, max_value = 30, value = 1, step = 1)

    cost = st.sidebar.slider('Total Cost per Person', int(budget_min*difference), int(budget_max*difference), int(budget_min*difference) + 3500, 500)

    trip_type = st.sidebar.multiselect(
    'Trip Type',
    [
    "Adventure Trip",
    "Backpacking Journey",
    "Beach Vacation",
    "Camping Expedition",
    "City Break",
    "Cultural Tour",
    "Cycling Tour",
    "Eco-Tourism Trip",
    "Educational Excursion",
    "Family Holiday",
    "Foodie Expedition",
    "Historical Tour",
    "Hiking and Trekking Adventure",
    "Luxury Getaway",
    "Mountain Climbing Expedition",
    "Photography Tour",
    "Pilgrimage Journey",
    "Relaxation Retreat",
    "Road Trip",
    "Romantic Retreat",
    "Safari Adventure",
    "Sailing Expedition",
    "Scuba Diving Trip",
    "Shopping Excursion",
    "Skiing and Snowboarding Trip",
    "Solo Expedition",
    "Spiritual Retreat",
    "Wellness Retreat",
    "Wildlife Safari",
    "Volunteer Travel Experience",
    "Wine Tasting Tour",
    "Yoga Retreat"
    ])

    additional_trip = st.sidebar.text_input('Additional Trip Type')
    if st.sidebar.button('Generate'):
        prompt = "I want to make a detailed trip planner from " + str(start)+ ", Thailand, and I want to visit " + list_to_string(destinations) + " equally. The duration is: " + str(duration) + ". I want the cost for each person to be between " + str(budget_min)+ " and maximum of " + str(cost) + "in Thai Bhat, for a total of " + str(people) +" people. The trip type must include: " + list_to_string(trip_type) + additional_trip +"."
        reply(prompt)
    else:
        pass
    st.write(st.session_state['replyText'])

def reply(prompt):
    global chat, replyText
    st.session_state['replyText'] = chat.send_message(prompt).text
    return

def list_to_string(lst, delimiter=', '):
    return delimiter.join(lst)

if __name__ == "__main__":
    print("TEST")
    run()
