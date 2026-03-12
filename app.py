import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Brand Strategy | Digital Streaks Solutions",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- ADVANCED CUSTOM CSS (PREMIUM DARK THEME) ---
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
    
    /* 4. Master Button Styling (Pill-shaped, Gradient, Hover Glow) */
    div.stButton > button:first-child {
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
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0, 209, 255, 0.5);
    }
    div.stButton > button:first-child p {
        color: #FFFFFF !important;
        font-size: 1.1rem !important;
        margin: 0 !important;
    }

    /* 5. Package Cards Styling */
    .package-card {
        background-color: #161A23;
        padding: 30px 25px;
        border-radius: 16px;
        border: 1px solid #2A2F3A;
        transition: all 0.3s ease;
        height: 100%;
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
    .package-card.popular::before {
        content: 'MOST POPULAR';
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(90deg, #7B61FF, #00D1FF);
        color: white;
        font-size: 0.75rem;
        font-weight: bold;
        padding: 4px 12px;
        border-radius: 20px;
        letter-spacing: 1px;
    }
    
    /* 6. Section Titles */
    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #FFFFFF !important;
        margin-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .section-desc {
        color: #A0ABB8 !important;
        margin-bottom: 1.5rem;
        font-size: 1.1rem;
    }
    
    /* 7. Custom sleek divider */
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

col1, col2, col3 = st.columns([1, 1.5, 1])
with col2:
    if st.button("BOOK YOUR FREE STRATEGY CALL", key="hero_cta"):
        st.success("Redirecting to Calendar... (Link goes here)")

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- INTERACTIVE #1: BRAND SCALABILITY AUDIT ---
st.markdown('<div class="section-title">1. The Brand Scalability Audit</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">Take this 2-question pulse check to see if your current brand is helping or hurting your conversions.</div>', unsafe_allow_html=True)

audit_q1 = st.radio(
    "When a lead visits your online profiles, do they instantly know why you are better than the competition?", 
    ["Select an answer...", "Yes, my messaging is crystal clear.", "No, it's a bit generic.", "I'm not sure."]
)

st.write("") # Spacer

audit_q2 = st.radio(
    "Are your visual assets (logo, colors, graphics) consistent across every platform?", 
    ["Select an answer...", "Yes, 100% consistent.", "Somewhat, but it's messy.", "No, it's all over the place."]
)

if audit_q1 != "Select an answer..." and audit_q2 != "Select an answer...":
    st.info("💡 **Audit Result:** Consistency and clarity are the pillars of trust. Let's fix the gaps together.")
    col_a, col_b, col_c = st.columns([1, 2, 1])
    with col_b:
        if st.button("Discuss My Audit Results", key="audit_cta"):
            st.success("Redirecting to Calendar...")

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- INTERACTIVE #2: MOOD / STYLE PICKER ---
st.markdown('<div class="section-title">2. Choose Your Business Identity</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">What aesthetic best represents the future of your company?</div>', unsafe_allow_html=True)

vibe_choice = st.selectbox(
    "Select a Brand Archetype:", 
    ["Choose a style...", "Modern Tech & Minimalist", "Human-Centric & Warm", "Bold & Disruptive", "Premium & Corporate"]
)

if vibe_choice != "Choose a style...":
    st.success(f"✨ Excellent choice. A **{vibe_choice}** brand requires specific font pairings, tone of voice, and color psychology to convert traffic into clients.")
    st.write("")
    col_x, col_y, col_z = st.columns([1, 2, 1])
    with col_y:
        if st.button(f"Book a Consultation to Build a {vibe_choice} Brand", key="vibe_cta"):
             st.success("Redirecting to Calendar...")

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- PACKAGES (Information Only) ---
st.markdown('<div class="section-title">3. Managed Outsourcing Branding Tiers</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">We don\'t just design; we partner with you. Explore our foundational pathways.</div>', unsafe_allow_html=True)

pack_col1, pack_col2, pack_col3 = st.columns(3)

with pack_col1:
    st.markdown('<div class="package-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #FFFFFF; margin-top:0;">Starter Tier</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: #00D1FF; font-size: 1.5rem; font-weight: bold; margin-bottom: 15px;">$499</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #A0ABB8; font-size: 0.9rem;">Perfect for new startups needing a professional baseline.</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul style='color: #E0E6ED; font-size: 0.95rem; line-height: 1.8; padding-left: 20px;'>
        <li>Primary & Secondary Logos</li>
        <li>Core Color Palette</li>
        <li>Typography Guidelines</li>
    </ul><br>
    """, unsafe_allow_html=True)
    st.button("Discuss Starter Tier", key="btn_starter")
    st.markdown('</div>', unsafe_allow_html=True)

with pack_col2:
    st.markdown('<div class="package-card popular">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #FFFFFF; margin-top:0;">Growth Tier</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: #00D1FF; font-size: 1.5rem; font-weight: bold; margin-bottom: 15px;">$1,499</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #A0ABB8; font-size: 0.9rem;">For scaling businesses needing a full digital presence makeover.</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul style='color: #E0E6ED; font-size: 0.95rem; line-height: 1.8; padding-left: 20px;'>
        <li>Everything in Starter</li>
        <li>Social Media Templates</li>
        <li>Brand Voice Guide</li>
        <li>Presentation Deck Design</li>
    </ul><br>
    """, unsafe_allow_html=True)
    st.button("Discuss Growth Tier", key="btn_growth")
    st.markdown('</div>', unsafe_allow_html=True)

with pack_col3:
    st.markdown('<div class="package-card">', unsafe_allow_html=True)
    st.markdown('<h3 style="color: #FFFFFF; margin-top:0;">Premium Tier</h3>', unsafe_allow_html=True)
    st.markdown('<p style="color: #00D1FF; font-size: 1.5rem; font-weight: bold; margin-bottom: 15px;">$3,499</p>', unsafe_allow_html=True)
    st.markdown('<p style="color: #A0ABB8; font-size: 0.9rem;">Total brand strategy and management for established leaders.</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul style='color: #E0E6ED; font-size: 0.95rem; line-height: 1.8; padding-left: 20px;'>
        <li>Everything in Growth</li>
        <li>Full Messaging Strategy</li>
        <li>Custom Collateral Suite</li>
        <li>Priority Design Support</li>
    </ul><br>
    """, unsafe_allow_html=True)
    st.button("Discuss Premium Tier", key="btn_premium")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- INTERACTIVE #3: THE BRAND DOCTOR ---
st.markdown('<div class="section-title">4. Why Most Brands Fail</div>', unsafe_allow_html=True)
st.markdown('<div class="section-desc">Select your biggest roadblock to see how our agency solves it.</div>', unsafe_allow_html=True)

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
st.markdown('<div class="section-title">5. See Our Process in Action</div>', unsafe_allow_html=True)
# Using a clean column setup to prevent the video from being too massive on desktop screens
vid_col1, vid_col2, vid_col3 = st.columns([1, 4, 1])
with vid_col2:
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 

st.markdown('<hr class="custom-divider">', unsafe_allow_html=True)

# --- FINAL CTA & FOOTER ---
st.markdown("<div class='hero-title' style='font-size: 3rem;'>Ready to Make Your Mark?</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle' style='margin-bottom: 2rem;'>Your solution to high overhead and inconsistent branding is just one call away.</div>", unsafe_allow_html=True)

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