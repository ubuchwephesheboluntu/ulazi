"""
Isikhungo Sezobuchwepheshe Boluntu — Website
=============================================
A Streamlit website for a business/organisation focused on helping
communities develop digitally (digital literacy, tech access, training,
and community upliftment through technology).
 
Run locally with:
    pip install streamlit
    streamlit run app.py
"""
 
from datetime import datetime
from pathlib import Path

import streamlit as st


APP_DIRECTORY = Path(__file__).resolve().parent
HERO_IMAGE = APP_DIRECTORY / "hero-image.png"

# -----------------------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------------------
st.set_page_config(
    page_title="Isikhungo Sezobuchwepheshe Boluntu",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
# -----------------------------------------------------------------------
# GLOBAL STYLING
# -----------------------------------------------------------------------
st.markdown(
    """
    <style>
        .stApp {
            background: #120E08;
            color: #F7E6B2;
        }
        [data-testid="stSidebar"] {
            background: #1D140A;
            border-right: 1px solid #6E4210;
        }
        [data-testid="stSidebar"] * {
            color: #F7E6B2;
        }
        h1, h2, h3, h4, p, label, .stMarkdown, .stText {
            color: #F7E6B2;
        }
        .main-title {
            font-size: 2.6rem;
            font-weight: 800;
            color: #F6C64E;
            text-shadow: 0 0 12px rgba(246, 162, 20, 0.35);
            margin-bottom: 0;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #D9A441;
            margin-top: 0;
        }
        .section-header {
            font-size: 1.8rem;
            font-weight: 700;
            color: #F6C64E;
            border-bottom: 3px solid #D98B17;
            padding-bottom: 6px;
            margin-top: 2rem;
        }
        .card {
            background: linear-gradient(135deg, #2A1A0B, #1B1209);
            color: #F7E6B2;
            padding: 1.2rem;
            border-radius: 12px;
            border: 1px solid #6E4210;
            border-left: 6px solid #E6A62E;
            margin-bottom: 1rem;
        }
        .stat-box {
            text-align: center;
            padding: 1rem;
            background: linear-gradient(135deg, #7A420B, #3A2109);
            color: #FFF0BD;
            border-radius: 12px;
            border: 1px solid #D98B17;
            box-shadow: 0 0 16px rgba(217, 139, 23, 0.2);
        }
        [data-testid="stMetric"] {
            background: #24170B;
            border: 1px solid #6E4210;
            border-radius: 12px;
            padding: 1rem;
        }
        [data-testid="stMetricLabel"] *, [data-testid="stMetricValue"] * {
            color: #F6C64E;
        }
        .stButton > button, [data-testid="stFormSubmitButton"] > button {
            background: #D98B17;
            color: #1A1006;
            border: 1px solid #F6C64E;
            font-weight: 700;
        }
        .stButton > button:hover, [data-testid="stFormSubmitButton"] > button:hover {
            background: #F6C64E;
            color: #1A1006;
            border-color: #FFF0BD;
        }
        [data-baseweb="input"] > div, [data-baseweb="textarea"] > div {
            background-color: #24170B;
            border-color: #6E4210;
        }
        input, textarea {
            color: #FFF0BD !important;
        }
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)
 
# -----------------------------------------------------------------------
# CHAT BOX STATE
# -----------------------------------------------------------------------
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# -----------------------------------------------------------------------
# NAVIGATION (SIDEBAR)
# -----------------------------------------------------------------------
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "About Us", "Our Services", "Our Impact", "Contact Us"],
)
 
st.sidebar.markdown("---")
st.sidebar.markdown("**Isikhungo Sezobuchwepheshe Boluntu**")
st.sidebar.markdown("_Building digital skills, one community at a time._")
 
# -----------------------------------------------------------------------
# HOME PAGE
# -----------------------------------------------------------------------
if page == "Home":
    st.markdown('<p class="main-title">Isikhungo Sezobuchwepheshe Boluntu</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Empowering communities through digital technology and skills development</p>', unsafe_allow_html=True)
 
    st.image(
        HERO_IMAGE,
        use_container_width=True,
        caption="Isikhungo Sezobuchwepheshe Boluntu",
    )
 
    st.markdown("### Welcome")
    st.write(
        """
        **Isikhungo Sezobuchwepheshe Boluntu** (Community Technology Centre) is
        dedicated to helping communities grow and thrive in the digital age.
        We believe that access to technology and digital skills should not be
        a privilege — it should be a right available to everyone, regardless
        of background or location.
 
        Through training, resources, and hands-on support, we help
        individuals, youth, small businesses, and local organisations build
        the digital confidence they need to participate fully in today's
        connected world.
        """
    )
 
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="stat-box"><h2>500+</h2>People Trained</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-box"><h2>20+</h2>Communities Reached</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-box"><h2>50+</h2>Workshops Hosted</div>', unsafe_allow_html=True)
 
# -----------------------------------------------------------------------
# ABOUT US PAGE
# -----------------------------------------------------------------------
elif page == "About Us":
    st.markdown('<p class="section-header">About Us</p>', unsafe_allow_html=True)
 
    st.write(
        """
        Isikhungo Sezobuchwepheshe Boluntu was founded on the belief that
        digital transformation should include everyone — not just those in
        well-resourced areas. We work directly with communities to close the
        digital gap and open up opportunities in education, employment, and
        entrepreneurship.
        """
    )
 
    st.markdown("#### Our Mission")
    st.markdown(
        """
        <div class="card">
        To equip communities with the digital skills, tools, and confidence
        needed to participate meaningfully in the modern economy and society.
        </div>
        """,
        unsafe_allow_html=True,
    )
 
    st.markdown("#### Our Vision")
    st.markdown(
        """
        <div class="card">
        A future where every community — urban or rural — has equal access to
        technology, digital education, and the opportunities that come with
        them.
        </div>
        """,
        unsafe_allow_html=True,
    )
 
    st.markdown("#### Our Values")
    values = {
        "Ubuntu": "We rise together — community first, always.",
        "Access": "Digital opportunity should reach everyone, everywhere.",
        "Empowerment": "We teach skills that last a lifetime, not quick fixes.",
        "Innovation": "We embrace new tools and ideas to solve old problems.",
    }
    for value, description in values.items():
        st.markdown(f"**{value}** — {description}")
 
# -----------------------------------------------------------------------
# SERVICES PAGE
# -----------------------------------------------------------------------
elif page == "Our Services":
    st.markdown('<p class="section-header">Our Services</p>', unsafe_allow_html=True)
    st.write("We offer a range of programmes designed to build digital capacity at every level.")
 
    services = [
        ("💻 Digital Literacy Training", "Basic computer skills, internet use, email, and online safety for beginners."),
        ("📱 Smart Device Workshops", "Practical training on using smartphones and tablets for everyday life, banking, and communication."),
        ("🧑‍💼 Youth Skills Development", "Coding, design, and technology career pathways for young people."),
        ("🏪 Small Business Digital Support", "Helping local entrepreneurs get online — social media, e-commerce, and digital marketing basics."),
        ("🌐 Community Wi-Fi & Access Points", "Working with partners to expand affordable internet access in underserved areas."),
        ("🎓 Train-the-Trainer Programmes", "Equipping community members to become digital skills facilitators themselves."),
    ]
 
    for i in range(0, len(services), 2):
        cols = st.columns(2)
        for col, (title, desc) in zip(cols, services[i:i + 2]):
            with col:
                st.markdown(f'<div class="card"><h4>{title}</h4>{desc}</div>', unsafe_allow_html=True)
 
# -----------------------------------------------------------------------
# IMPACT PAGE
# -----------------------------------------------------------------------
elif page == "Our Impact":
    st.markdown('<p class="section-header">Our Impact</p>', unsafe_allow_html=True)
 
    st.write(
        """
        Since our founding, we have worked hand-in-hand with communities to
        make real, measurable progress in digital inclusion.
        """
    )
 
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("People Trained", "500+")
    col2.metric("Communities Reached", "20+")
    col3.metric("Workshops Hosted", "50+")
    col4.metric("Partner Organisations", "10+")
 
    st.markdown("#### Stories from the Community")
    st.markdown(
        """
        <div class="card">
        "Before the training, I had never used a computer. Now I run my
        small business's online orders myself." — <i>Community member, Workshop participant</i>
        </div>
        <div class="card">
        "The youth coding programme gave my son the confidence to apply for
        a learnership in IT." — <i>Parent, Community programme</i>
        </div>
        """,
        unsafe_allow_html=True,
    )
 
# -----------------------------------------------------------------------
# CONTACT PAGE
# -----------------------------------------------------------------------
elif page == "Contact Us":
    st.markdown('<p class="section-header">Contact Us</p>', unsafe_allow_html=True)
    st.write("We would love to hear from you — whether you want to partner with us, volunteer, or join a programme.")
 
    col1, col2 = st.columns([1, 1])
 
    with col1:
        st.markdown("#### Get in Touch")

        # --- Chat history ---
        if st.session_state.chat_messages:
            chat_container = st.container(height=350)
            with chat_container:
                for chat in st.session_state.chat_messages:
                    with st.chat_message("user"):
                        st.markdown(f"**{chat['name']}** · _{chat['time']}_")
                        st.write(chat["message"])
        else:
            st.info("No messages yet — be the first to drop a chat!")

        # --- New message form ---
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full Name")
            message = st.text_area("Your Message")
            submitted = st.form_submit_button("Send Message")

            if submitted:
                if name and message:
                    st.session_state.chat_messages.append(
                        {
                            "name": name,
                            "message": message,
                            "time": datetime.now().strftime("%d %b %Y, %H:%M"),
                        }
                    )
                    st.success(f"Thank you, {name}! Your message has been dropped in the chat below.")
                    st.rerun()
                else:
                    st.warning("Please fill in all fields before submitting.")
 
    with col2:
        st.markdown("#### Our Details")
        st.markdown(
            """
            <div class="card">
            📍 <b>Address:</b> Community Centre, South Africa<br><br>
            📞 <b>Phone:</b> +27 00 000 0000<br><br>
            ✉️ <b>Email:</b> info@isikhungobuchwepheshe.org<br><br>
            🕒 <b>Office Hours:</b> Mon–Fri, 08:00–16:00
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("#### Follow Us")
        st.write("Facebook | Instagram | Twitter (X) | LinkedIn")
 
# -----------------------------------------------------------------------
# FOOTER (shown on every page)
# -----------------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>© 2026 Isikhungo Sezobuchwepheshe Boluntu. "
    "All rights reserved. | Empowering Communities Through Technology.</p>",
    unsafe_allow_html=True,
)
 
