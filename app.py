import streamlit as st

# --- PAGE CONFIGURATION ---
# This sets the tab title and forces a wide layout.
st.set_page_config(
    page_title="Brand Strategy | Digital Streaks Solutions Inc.",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (THEMING & LANDING PAGE ENFORCEMENT) ---
# We hide the default Streamlit menu to prevent users from navigating away.
# We also apply Digital Streaks colors: Teal (#0E6A82), Orange (#FF5722), and force text colors.
custom_css = """
<style>
    /* Hide Streamlit Header, Footer, and Menu to prevent navigation */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main Background */
    .stApp {
        background-color: #F8F9FA !important;
    }
    
    /* FORCE ALL TEXT TO BE DARK (Fixes the invisible text bug in Dark Mode) */
    h1, h2, h3, h4, h5, h6, p, span, label, li, div[data-testid="stMarkdownContainer"] {
        color: #2C3E50 !important;
    }
    
    /* Ensure the button text stays WHITE so it doesn't blend in */
    div.stButton > button:first-child p, 
    div.stButton > button:first-child span {
        color: #FFFFFF !important; 
    }

    /* Hero Section Styling - Centered for Landing Page Feel */
    .hero-title {
        color: #0E6A82 !important;
        font-size: 3.5rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    .hero-subtitle {
        color: #2C3E50 !important;
        font-size: 1.25rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    /* Primary CTA Button Styling */
    div.stButton > button:first-child {
        background-color: #FF5722 !important;
        color: white !important;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-size: 1.25rem;
        font-weight: bold;
        border: none;
        width: 100%;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        background-color: #E64A19 !important;
        border: none;
    }
    
    /* Package Card Styling */
    .package-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-top: 5px solid #0E6A82;
        margin-bottom: 15px;
    }
    .package-card.popular {
        border-top: 5px solid #FF5722;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- HERO SECTION (The 2-Second Elevator Pitch) ---
st.markdown('<div class="hero-title">Stop Being the Best Kept Secret.</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Professional branding that helps you scale your business, build trust, and cut overhead costs. Designed for remote-first leaders.</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("BOOK YOUR FREE STRATEGY CALL NOW", key="hero_cta"):
        st.success("Redirecting to Calendar... (Link goes here)")

st.divider()

# --- INTERACTIVE #1: BRAND SCALABILITY AUDIT (Marketing Hook) ---
st.header("1. The Brand Scalability Audit")
st.write("Take this 2-question pulse check to see if your current brand is helping or hurting your conversions.")

audit_q1 = st.radio(
    "When a lead visits your online profiles, do they instantly know why you are better than the competition?", 
    ["Select an answer...", "Yes, my messaging is crystal clear.", "No, it's a bit generic.", "I'm not sure."]
)

audit_q2 = st.radio(
    "Are your visual assets (logo, colors, graphics) consistent across every platform?", 
    ["Select an answer...", "Yes, 100% consistent.", "Somewhat, but it's messy.", "No, it's all over the place."]
)

if audit_q1 != "Select an answer..." and audit_q2 != "Select an answer...":
    st.info("**Audit Result:** Consistency and clarity are the pillars of trust. Let's fix the gaps together.")
    if st.button("Discuss My Audit Results", key="audit_cta"):
        st.success("Redirecting to Calendar...")

st.divider()

# --- INTERACTIVE #2: MOOD / STYLE PICKER ---
st.header("2. Choose Your Business Identity")
st.write("What vibe best represents the future of your company? (Select one to see your next step)")

vibe_choice = st.selectbox(
    "Select a Brand Archetype:", 
    ["Choose a style...", "Modern Tech & Minimalist", "Human-Centric & Warm", "Bold & Disruptive"]
)

if vibe_choice != "Choose a style...":
    st.success(f"Excellent choice. A **{vibe_choice}** brand requires specific font pairings and color psychology.")
    # Supervisor rule applied: CTA immediately after brand color/style selection
    if st.button(f"Book a Consultation to Build Your {vibe_choice} Brand", key="vibe_cta"):
         st.success("Redirecting to Calendar...")

st.divider()

# --- PACKAGES (Information Only, No Direct Selling) ---
st.header("3. Managed Outsourcing Branding Tiers")
st.write("We don't just design; we partner with you. Which level fits your current growth stage?")

pack_col1, pack_col2, pack_col3 = st.columns(3)

with pack_col1:
    st.markdown('<div class="package-card">', unsafe_allow_html=True)
    st.subheader("Starter Tier")
    st.write("Perfect for new startups needing a professional visual identity.")
    st.write("- Primary & Secondary Logos\n- Color Palette\n- Typography Guidelines")
    st.button("Inquire About Starter", key="btn_starter")
    st.markdown('</div>', unsafe_allow_html=True)

with pack_col2:
    st.markdown('<div class="package-card popular">', unsafe_allow_html=True)
    st.subheader("Growth Tier (Popular)")
    st.write("For scaling businesses needing a full digital presence makeover.")
    st.write("- Everything in Starter\n- Social Media Templates\n- Brand Voice Guide")
    st.button("Inquire About Growth", key="btn_growth")
    st.markdown('</div>', unsafe_allow_html=True)

with pack_col3:
    st.markdown('<div class="package-card">', unsafe_allow_html=True)
    st.subheader("Premium Tier")
    st.write("Total brand and strategy management for established leaders.")
    st.write("- Everything in Growth\n- Full Messaging Strategy\n- Priority Design Support")
    st.button("Inquire About Premium", key="btn_premium")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# --- INTERACTIVE #3: THE BRAND DOCTOR ---
st.header("4. What is your biggest branding roadblock?")
tab1, tab2, tab3 = st.tabs(["Unclear Messaging", "Inconsistent Visuals", "Lack of Trust"])

with tab1:
    st.write("**The Diagnosis:** Your audience doesn't understand what you do quickly enough.")
    st.write("**The Solution:** We craft 'Elevator Pitch' copy that converts.")
with tab2:
    st.write("**The Diagnosis:** Your materials look like they belong to 5 different companies.")
    st.write("**The Solution:** We build a strict, easy-to-use brand guideline.")
with tab3:
    st.write("**The Diagnosis:** High traffic, but low conversions. People bounce.")
    st.write("**The Solution:** We elevate your aesthetic to match your premium service quality.")

st.divider()

# --- VIDEO PROOF ---
st.header("5. See Our Process in Action")
# Placeholder for the Digital Streaks video
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Replace with actual company video URL

st.divider()

# --- FINAL CTA & FOOTER ---
st.markdown("<h2 style='text-align: center; color: #0E6A82 !important;'>Ready to Make Your Mark Today?</h2>", unsafe_allow_html=True)
col_a, col_b, col_c = st.columns([1, 2, 1])
with col_b:
    if st.button("BOOK YOUR BRANDING CALL", key="final_cta"):
        st.success("Redirecting to Calendar...")

st.caption("---")
st.caption("© 2026 Digital Streaks Solutions Inc. | Cebu City, Philippines | Managed Outsourcing & Digital Marketing")