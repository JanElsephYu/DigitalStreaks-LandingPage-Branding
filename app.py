import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Brand Strategy | Digital Streaks Solutions",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- SESSION STATE FOR QUIZ ---
# This allows the quiz to update dynamically one question at a time
if 'quiz_step' not in st.session_state:
    st.session_state.quiz_step = 1

def next_question():
    st.session_state.quiz_step += 1

# --- ADVANCED CUSTOM CSS ---
custom_css = """
<style>
    /* 1. Hide Streamlit Nav & Footer */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 2. Global Dark Background & Fonts */
    .stApp {
        background-color: #0B0E14 !important;
    }
    
    /* Force Text Colors for Dark Theme */
    h1, h2, h3, h4, h5, h6, p, span, label, li, div[data-testid="stMarkdownContainer"] {
        color: #E0E6ED !important;
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    
    /* 3. Hero Section - Gradient Typography */
    .hero-title {
        background: linear-gradient(90deg, #7B61FF 0%, #00D1FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 4.5rem;
        font-weight: 900;
        line-height: 1.1;
        margin-bottom: 1rem;
        text-align: center;
        letter-spacing: -1.5px;
    }
    .hero-subtitle {
        color: #A0ABB8 !important;
        font-size: 1.3rem;
        font-weight: 400;
        margin-bottom: 3rem;
        text-align: center;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* 4. Master Button Styling */
    div.stButton > button {
        background: linear-gradient(90deg, #7B61FF 0%, #00D1FF 100%) !important;
        color: #FFFFFF !important;
        border-radius: 50px !important;
        padding: 0.8rem 2.5rem !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        border: none !important;
        width: 100%;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(123, 97, 255, 0.3);
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 209, 255, 0.5);
    }
    
    /* Quiz Card Styling */
    .quiz-container {
        background-color: #161A23;
        padding: 40px;
        border-radius: 16px;
        border: 1px solid #2A2F3A;
        text-align: center;
        max-width: 700px;
        margin: 0 auto;
    }
    
    /* 5. Package Cards Styling */
    .package-card {
        background-color: #161A23;
        padding: 40px 30px;
        border-radius: 16px;
        border: 1px solid #2A2F3A;
        transition: all 0.3s ease;
        height: 100%;
        text-align: center;
    }
    .package-card:hover {
        transform: translateY(-5px);
        border-color: #7B61FF;
        box-shadow: 0 10px 30px rgba(123, 97, 255, 0.15);
    }
    .package-card.popular {
        background: linear-gradient(180deg, #1A1F2B 0%, #161A23 100%);
        border: 1px solid #00D1FF;
        position: relative;
    }
    
    /* Center align headers */
    .section-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #FFFFFF !important;
        margin-bottom: 0.5rem;
        margin-top: 2rem;
        text-align: center;
    }
    .section-desc {
        color: #A0ABB8 !important;
        margin-bottom: 2.5rem;
        font-size: 1.1rem;
        text-align: center;
    }
    
    /* Custom sleek divider */
    .custom-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #2A2F3A, transparent);
        border: none;
        margin: 4rem 0;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- HERO SECTION ---
st.markdown('<div style="margin-top: 3rem;"></div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">Your Brand is Your Best Salesperson.<br>Is it Closing the Deal?</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Digital Streaks builds high-impact visual identities that scale. Stop blending in with the generic competition; start leading your industry.</div>', unsafe_allow_html=True)

# Centering the hero button perfectly
col_h1, col_h2, col_h3 = st.columns([1, 1.5, 1])
with col_h2:
    if st.button("BOOK YOUR FREE STRATEGY CALL", key="hero_cta"):
        st.success("Redirecting to Calendar...")

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- INTERACTIVE #1: THE BRAND ARCHETYPE QUIZ (Dynamic Step-by-Step) ---
st.markdown('<div class="section-title">1. The Brand Persona Discovery</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">Find out what aesthetic attracts your ideal clients. (Takes 30 seconds)</div>', unsafe_allow_html=True)

# Centered container for the quiz
q_col1, q_col2, q_col3 = st.columns([1, 2, 1])

with q_col2:
    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
    
    if st.session_state.quiz_step == 1:
        st.markdown('<h3>Question 1 of 6</h3>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.2rem; color:#A0ABB8;">When people see your brand, what is the first word you want them to think of?</p>', unsafe_allow_html=True)
        st.radio(" ", ["Innovative & Modern", "Trustworthy & Established", "Bold & Rebellious", "Premium & Exclusive"], key="q1", label_visibility="collapsed")
        st.button("Next Question →", on_click=next_question, key="btn1")
        
    elif st.session_state.quiz_step == 2:
        st.markdown('<h3>Question 2 of 6</h3>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.2rem; color:#A0ABB8;">If your brand were a person, how would they dress?</p>', unsafe_allow_html=True)
        st.radio(" ", ["Sleek tech-wear", "A sharp, tailored suit", "Vibrant, trendy streetwear", "Minimalist designer fashion"], key="q2", label_visibility="collapsed")
        st.button("Next Question →", on_click=next_question, key="btn2")
        
    elif st.session_state.quiz_step == 3:
        st.markdown('<h3>Question 3 of 6</h3>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.2rem; color:#A0ABB8;">What is the main reason your dream clients haven\'t bought from you yet?</p>', unsafe_allow_html=True)
        st.radio(" ", ["They don't know we exist.", "We look like everyone else.", "Our value isn't clearly communicated.", "We don't look professional enough yet."], key="q3", label_visibility="collapsed")
        st.button("Next Question →", on_click=next_question, key="btn3")
        
    elif st.session_state.quiz_step == 4:
        st.markdown('<h3>Question 4 of 6</h3>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.2rem; color:#A0ABB8;">How do you want your audience to feel after visiting your site?</p>', unsafe_allow_html=True)
        st.radio(" ", ["Inspired to take action", "Completely relieved and secure", "Excited for the future", "Ready to invest in premium quality"], key="q4", label_visibility="collapsed")
        st.button("Next Question →", on_click=next_question, key="btn4")
        
    elif st.session_state.quiz_step == 5:
        st.markdown('<h3>Question 5 of 6</h3>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.2rem; color:#A0ABB8;">Which of these sounds like your current visual aesthetic?</p>', unsafe_allow_html=True)
        st.radio(" ", ["A bit all over the place.", "Clean, but a little boring.", "A solid start, but needs polish.", "We don't really have one yet."], key="q5", label_visibility="collapsed")
        st.button("Next Question →", on_click=next_question, key="btn5")
        
    elif st.session_state.quiz_step == 6:
        st.markdown('<h3>Question 6 of 6</h3>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.2rem; color:#A0ABB8;">What is your biggest business goal for the next 6 months?</p>', unsafe_allow_html=True)
        st.radio(" ", ["Launch a new product or service", "Double my lead generation", "Confidently raise my prices", "Build undeniable industry authority"], key="q6", label_visibility="collapsed")
        st.button("See My Brand Results →", on_click=next_question, key="btn6")
        
    elif st.session_state.quiz_step > 6:
        st.markdown('<h3>✨ Your Brand Archetype Is Ready</h3>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:1.2rem; color:#00D1FF;">Based on your answers, your brand needs a <strong>Bold & Disruptive</strong> aesthetic to capture the attention of your target market.</p>', unsafe_allow_html=True)
        st.markdown('<p style="color:#A0ABB8; margin-bottom: 20px;">A brand like this requires specific font pairings, high-contrast colors, and a confident tone of voice to convert traffic into clients.</p>', unsafe_allow_html=True)
        
        # Micah's specific rule applied here
        if st.button("BOOK CONSULTATION TO BUILD THIS BRAND", key="quiz_cta"):
            st.success("Redirecting to Calendar...")
        
        # Added a reset link loop
        st.write("<br>", unsafe_allow_html=True)
        if st.button("↺ Retake Quiz", key="reset_quiz"):
            st.session_state.quiz_step = 1
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- PACKAGES (Information Only, highly aligned) ---
st.markdown('<div class="section-title">2. Managed Outsourcing Branding Tiers</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">We don\'t just design; we partner with you. Explore our foundational pathways.</div>', unsafe_allow_html=True)

# Added padding columns to center the 3 cards nicely on wide screens
pack_pad1, pack_col1, pack_col2, pack_col3, pack_pad2 = st.columns([0.5, 2, 2, 2, 0.5])

with pack_col1:
    st.markdown('<div class="package-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #FFFFFF; margin-top:0;">Starter Tier</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: #00D1FF; font-size: 1.8rem; font-weight: bold; margin-bottom: 15px;">$499</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #A0ABB8; font-size: 0.95rem; min-height: 45px;">Perfect for new startups needing a professional baseline.</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul style='color: #E0E6ED; font-size: 1rem; line-height: 2; padding-left: 0; list-style-position: inside; text-align: left;'>
        <li>✓ Primary & Secondary Logos</li>
        <li>✓ Core Color Palette</li>
        <li>✓ Typography Guidelines</li>
    </ul><br>
    """, unsafe_allow_html=True)
    st.button("Discuss Starter", key="btn_starter")
    st.markdown('</div>', unsafe_allow_html=True)

with pack_col2:
    st.markdown('<div class="package-card popular">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #FFFFFF; margin-top:0;">Growth Tier</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: #00D1FF; font-size: 1.8rem; font-weight: bold; margin-bottom: 15px;">$1,499</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #A0ABB8; font-size: 0.95rem; min-height: 45px;">For scaling businesses needing a full digital presence makeover.</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul style='color: #E0E6ED; font-size: 1rem; line-height: 2; padding-left: 0; list-style-position: inside; text-align: left;'>
        <li>✓ Everything in Starter</li>
        <li>✓ Social Media Templates</li>
        <li>✓ Brand Voice Guide</li>
        <li>✓ Presentation Deck Design</li>
    </ul><br>
    """, unsafe_allow_html=True)
    st.button("Discuss Growth", key="btn_growth")
    st.markdown('</div>', unsafe_allow_html=True)

with pack_col3:
    st.markdown('<div class="package-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #FFFFFF; margin-top:0;">Premium Tier</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: #00D1FF; font-size: 1.8rem; font-weight: bold; margin-bottom: 15px;">$3,499</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #A0ABB8; font-size: 0.95rem; min-height: 45px;">Total brand strategy and management for established leaders.</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul style='color: #E0E6ED; font-size: 1rem; line-height: 2; padding-left: 0; list-style-position: inside; text-align: left;'>
        <li>✓ Everything in Growth</li>
        <li>✓ Full Messaging Strategy</li>
        <li>✓ Custom Collateral Suite</li>
        <li>✓ Priority Design Support</li>
    </ul><br>
    """, unsafe_allow_html=True)
    st.button("Discuss Premium", key="btn_premium")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- INTERACTIVE #3: THE BRAND DOCTOR ---
st.markdown('<div class="section-title">3. Why Most Brands Fail</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">Select your biggest roadblock to see how our agency solves it.</div>', unsafe_allow_html=True)

# Align the tabs cleanly in the center
tab_col1, tab_col2, tab_col3 = st.columns([1, 2, 1])
with tab_col2:
    tab1, tab2, tab3 = st.tabs(["Unclear Messaging", "Inconsistent Visuals", "Lack of Trust"])

    with tab1:
        st.markdown("<br><p style='font-size: 1.1rem;'>⚠️ <strong>The Diagnosis:</strong> Your audience doesn't understand what you do quickly enough.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.1rem; color: #00D1FF;'>✅ <strong>The Solution:</strong> We craft 'Elevator Pitch' copy that cuts through the noise and converts.</p>", unsafe_allow_html=True)
    with tab2:
        st.markdown("<br><p style='font-size: 1.1rem;'>⚠️ <strong>The Diagnosis:</strong> Your materials look like they belong to 5 different companies.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.1rem; color: #00D1FF;'>✅ <strong>The Solution:</strong> We build a strict, easy-to-use brand guideline for your entire team.</p>", unsafe_allow_html=True)
    with tab3:
        st.markdown("<br><p style='font-size: 1.1rem;'>⚠️ <strong>The Diagnosis:</strong> High traffic, but low conversions. People bounce.</p>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 1.1rem; color: #00D1FF;'>✅ <strong>The Solution:</strong> We elevate your aesthetic to match your premium service quality, building instant credibility.</p>", unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- VIDEO PROOF ---
st.markdown('<div class="section-title">4. See The Power of Branding</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">A quick breakdown of why brand identity is the ultimate growth lever.</div>', unsafe_allow_html=True)

# Real, public digital marketing/branding explainer video
vid_col1, vid_col2, vid_col3 = st.columns([1, 3, 1])
with vid_col2:
    st.video("https://www.youtube.com/watch?v=sO-XhEBBkNU") 

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- FINAL CTA & FOOTER ---
st.markdown("<div class='section-title' style='font-size: 3rem;'>Ready to Make Your Mark?</div>", unsafe_allow_html=True)
st.markdown("<div class='section-desc' style='margin-bottom: 2rem;'>Your solution to high overhead and inconsistent branding is just one call away.</div>", unsafe_allow_html=True)

col_f1, col_f2, col_f3 = st.columns([1, 1.5, 1])
with col_f2:
    if st.button("BOOK YOUR BRANDING STRATEGY CALL", key="final_cta"):
        st.success("Redirecting to Calendar...")

st.write("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #A0ABB8; font-size: 0.85rem; padding-top: 2rem; border-top: 1px solid #2A2F3A;'>
    © 2026 Digital Streaks Solutions Inc. | Cebu City, Philippines | Managed Outsourcing & Digital Marketing
</div>
""", unsafe_allow_html=True)