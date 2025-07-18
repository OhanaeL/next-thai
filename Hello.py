import streamlit as st
import datetime
import io
from streamlit.logger import get_logger
import google.generativeai as genai
import markdown2
from xhtml2pdf import pisa

LOGGER = get_logger(__name__)

genai.configure(api_key=st.secrets["GPT_API_KEY"])
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])
budget_min = 1000
budget_max = 15000
ms = st.session_state
chat = None
responded = False
greeting_message = 'Your Thailand Trip Planner Powered by AI. Simplify your travels across Thailand with personalized itineraries crafted just for you. Discover the best of Thailand effortlessly with Next Thai.'

if 'AIModel' not in ms:
    chat = model.start_chat(history=[])
    chat.send_message("Your current role in this system is that of an AI travel planner and itinerary maker. Users will come to you with a prompt detailing their travel date range, budget, destinations, trip types, number of people and more. Your job is to make sure the dates and budgets in your plan do not go over the submitted values in the prompt. The budget will include the transportation fee from the starting point to the first destination. Make sure to allot time and budget to go back to the starting destination before the duration is over when you make a plan and include that in the itinerary. Make sure that the itinerary does not go over the user's submitted budget and date range. If the trip is not possible or very difficult, instead of making the plan, say so and you can suggest changes the users could make to the prompt; for example extending the duration or removing a destination. Put a title of the trip at the top of the plan. Don't use first person pronouns for yourself or refer to yourself as an AI. Give links to hotels suggested.")
    ms['AIModel'] = chat
else:
    chat = ms['AIModel']

if 'replyText' not in ms:
    ms['replyText'] = greeting_message
if ms['replyText'] == greeting_message:
    responded = False
else: 
    responded = True
if "themes" not in ms: 
    ms.themes = {"current_theme": "dark", "refreshed": True}

def convert_markdown_to_html(markdown_text):
    # Convert markdown text to HTML
    html_content = markdown2.markdown(markdown_text)
    return html_content

def generate_pdf_from_html(html_content):
    buffer = io.BytesIO()  # Create a buffer to store the PDF
    pisa_status = pisa.CreatePDF(io.StringIO(html_content), dest=buffer)  # Convert HTML to PDF
    buffer.seek(0)
    return buffer  # Return the buffer containing the PDF

def reply(prompt):
    global chat, replyText
    st.session_state['replyText'] = chat.send_message(prompt).text
    
    # Convert markdown to HTML
    html_content = convert_markdown_to_html(st.session_state['replyText'])
    
    # Generate PDF from HTML
    pdf_buffer = generate_pdf_from_html(html_content)
    
    # Store PDF buffer in session state for download
    st.session_state['pdf_buffer'] = pdf_buffer
    return

def run():
    global replyText, responded

    st.set_page_config(
        page_title="Next Thai - Travels",
        page_icon="✈️",
        layout="wide"
    )
    st.image('images/Group 1.png', caption="")
    st.markdown("# Customize Your Journey Here!")
    st.subheader("Your Dream Trip with Next Thai.")
    st.sidebar.header("Customize Your Journey Here!")

    today = datetime.datetime.now()

    max_year = datetime.date(today.year +5, 12, 31)

    start = st.sidebar.selectbox('Starting Point', ("Bangkok", "Nonthaburi", "Pak Kret", "Hua Hin", "Hat Yai", "Chaophraya Surasak", "Surat Thani","Nakhon Ratchasima","Chiang Mai","Udon Thani","Pattaya","Khon Kaen","Nakhon Si Thammarat","Laem Chabang","Rangsit","Nakhon Sawan","Phuket","Chiang Rai","Ubon Ratchathani","Nakhon Pathom","Ko Samui","Samut Sakhon","Phitsanulok","Rayong","Songkhla","Yala","Trang","Om Noi","Sakon Nakhon","Lampang","Samut Prakan" ,"Phra Nakhon Si Ayutthaya","Mae Sot"))

    destinations = st.sidebar.multiselect('Destination', ["Bangkok", "Nonthaburi", "Pak Kret", "Hua Hin", "Hat Yai", "Chaophraya Surasak", "Surat Thani","Nakhon Ratchasima","Chiang Mai","Udon Thani","Pattaya","Khon Kaen","Nakhon Si Thammarat","Laem Chabang","Rangsit","Nakhon Sawan","Phuket","Chiang Rai","Ubon Ratchathani","Nakhon Pathom","Ko Samui","Samut Sakhon","Phitsanulok","Rayong","Songkhla","Yala","Trang","Om Noi","Sakon Nakhon","Lampang","Samut Prakan" ,"Phra Nakhon Si Ayutthaya","Mae Sot"])

    duration = st.sidebar.date_input("Duration Date", (today, datetime.date(today.year , today.month, today.day +1)), today, max_year, format="MM.DD.YYYY")
    difference = 1
    if len(duration) > 1:
        difference = duration[1].day-duration[0].day + 1

    people = st.sidebar.number_input('How Many People?', min_value = 1, max_value = 30, value = 1, step = 1)

    cost = st.sidebar.slider('Total Cost per Person', int(budget_min*difference), int(budget_max*difference), int(budget_min*difference) + 3500, 500)

    trip_type = st.sidebar.multiselect('Trip Type', ["Adventure Trip", "Backpacking Journey", "Beach Vacation", "Camping Expedition", "City Break", "Cultural Tour", "Cycling Tour", "Eco-Tourism Trip", "Educational Excursion", "Family Holiday", "Foodie Expedition", "Historical Tour", "Hiking and Trekking Adventure", "Luxury Getaway", "Mountain Climbing Expedition", "Photography Tour", "Pilgrimage Journey", "Relaxation Retreat", "Road Trip", "Romantic Retreat", "Safari Adventure", "Sailing Expedition", "Scuba Diving Trip", "Shopping Excursion", "Skiing and Snowboarding Trip", "Solo Expedition", "Spiritual Retreat", "Wellness Retreat", "Wildlife Safari", "Volunteer Travel Experience", "Wine Tasting Tour", "Yoga Retreat"])

    additional_trip = st.sidebar.text_input('Additional Trip Type')
    if len(destinations) <= 0:
        destinations.append(start)
    if st.sidebar.button('Generate'):
        responded = True
        prompt = "I want to make a detailed trip planner with " + str(start)+ ", Thailand as the starting point, and I want to visit only " + list_to_string(destinations) + ". The duration is: " + str(difference) + " at a starting date of "+ str(duration[0]) +". Make sure to not go over that. I want the cost for each person to be a maximum of " + str(cost) + "in Thai Bhat, for a total of " + str(people) +" people. Make sure to not go over that. The trip type must include: " + list_to_string(trip_type) + additional_trip +"."
        with st.spinner('GENERATING Travel Plan...'):
            reply(prompt)
    else:
        pass
    st.write(st.session_state['replyText'])
    if responded:
        # Generate PDF and provide download option
        pdf_buffer = st.session_state.get('pdf_buffer', None)
        if pdf_buffer:
            st.download_button('Download Plan as PDF', pdf_buffer, file_name="Thailand_Trip_Plan.pdf", mime="application/pdf")


def list_to_string(lst, delimiter=', '):
    return delimiter.join(lst)

if __name__ == "__main__":
    run()
