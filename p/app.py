import streamlit as st, random, string, math

# Generate Password
def generate_password(length):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    return "".join(random.choices(chars, k=length))

# Analyze Password Strength
def analyze_password(pwd):
    categories = {"Uppercase": sum(c.isupper() for c in pwd), "Lowercase": sum(c.islower() for c in pwd),
                  "Numbers": sum(c.isdigit() for c in pwd), "Symbols": sum(c in string.punctuation for c in pwd)}
    entropy = round(len(pwd) * math.log2(len(set(pwd))), 2)
    score = sum(bool(v) for v in categories.values()) + (len(pwd) >= 8)
    level = ["Weak 🔴", "Good 🟠", "Hard 🟢"][min(score, 3) - 1]
    return level, f"Entropy: {entropy} bits", categories

# Streamlit UI
st.set_page_config(page_title="🔐 Password Tool")
st.title("🔐 Secure Password Generator & Strength Checker")

# Password Generator
length = st.slider("Password Length", 6, 32, 12)
if st.button("Generate Password"):
    st.text_input("Generated Password:", generate_password(length))

# Password Strength Checker
pwd = st.text_input("Check Password Strength", type="password")
if pwd:
    strength, entropy_msg, categories = analyze_password(pwd)
    st.subheader(f"Strength: {strength}")
    st.write(entropy_msg)
    for k, v in categories.items():
        st.write(f"🔹 {k}: {v}")


                      
                      


