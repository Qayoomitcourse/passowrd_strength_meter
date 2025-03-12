import streamlit as st
import re 

st.set_page_config(page_title="Password Strength Meter", layout="wide")
st.title("🔐 Password Strength Meter App by Abdul Qayoom")

st.markdown("""
### Welcome to the ultimate password strength controller!
Use this simple tool to check your password strength.
""")

password = st.text_input("Enter your password", type="password")

feedback = []
score = 0


if password: 
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper and Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions below.")
    
    if feedback:
        st.write("## Improvement Suggestions:")
        for tips in feedback:
            st.write(tips)
else:
    st.info("Please enter your password to get started.")
