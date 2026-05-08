import streamlit as st
import requests
import pandas as pd

# --- API Base URL ---
url_base = 'https://v6.exchangerate-api.com/v6/4b1aac5e548e6658f98c349a/latest/'


# --- PAGE TITLE ---
st.markdown("""    
<div style="border-left: 6px solid #4CAF50; padding-left: 12px;">
    <h3 style="margin-bottom:0;">💱 Smart Currency Converter</h3>
    <p style="color: orange; margin-top:0;">Real-time global exchange rates</p>
</div>
""", unsafe_allow_html=True)

# --- CUSTOM CSS ---
st.markdown("""
<style>
.block-container {
    max-width: 900px;
    margin: auto;
    padding-top: 1rem;
}

/* Selectbox + multiselect style */
div[data-baseweb="select"] {
    background-color: #2b0000;
    border-radius: 8px;
    color: white;
    padding: 6px;
    border: 1px solid #ff4b4b;
}
div[data-baseweb="popover"] {
    background-color: #1c1c1c !important; 
    color: white !important;
    border-radius: 8px !important;
}
div[data-baseweb="select"] span {
    color: white !important;
}
ul li:hover {
    background-color: #550000 !important;
}

/* Button */
div.stButton > button {
    background-color: #ff4b4b;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 8px 18px;
    transition: all 0.2s ease-in-out;
}
div.stButton > button:hover {
    background-color: #ff7070;
}

/* Table */
table {
    border-collapse: collapse;
    width: 100%;
}
thead tr {
    background-color: #4b0000;
    color: white;
    text-align: center;
}
tbody tr:nth-child(even) {
    background-color: #1a1a1a;
}
tbody td, thead th {
    padding: 8px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- UI Layout ---
col1, col2, col3 = st.columns([1.2, 1.2, 0.6])
with col1:
    st.write("### Base Currency")
    base_choice = st.selectbox("", ['PKR', 'USD', 'EUR', 'GBP', 'KWD'])
    base_input = st.text_input(f"Amount in {base_choice}", value="0.00")  # removed +/- buttons

with col2:
    st.write("### Target Currency")
    targ_curr = st.multiselect("", ['PKR', 'USD', 'EUR', 'GBP', 'KWD'])

with col3:
    st.write("&nbsp;")  # visual spacer
    st.write("&nbsp;")
    convert_btn = st.button("Convert 💱")

# --- Conversion Logic ---
if convert_btn:
    if not targ_curr:
        st.warning("⚠️ Please select at least one target currency.")    # Yellow
    else:
        url = url_base + base_choice
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            rates = data.get('conversion_rates', {})

            try:
                base_value = float(base_input)
            except ValueError:
                st.error("❌ Please enter a valid numeric amount.")
                st.stop()

            results = []
            for target in targ_curr:
                if target in rates:
                    rate = rates[target]
                    converted_amount = base_value * rate
                    results.append({
                        'Target Currency': target,
                        'Conversion Rate': f"{rate:.6f}",
                        'Converted Amount': f"{converted_amount:.4f}"
                    })
                else:
                    st.error(f"❌ Rate for {target} not available.")

            if results:
                df = pd.DataFrame(results)
                st.markdown("<hr>", unsafe_allow_html=True)
                st.subheader(f"💹 Conversion Results for {base_choice}")
                st.table(df)

        else:
            st.error("❌ Failed to fetch conversion rates. Please check your API key or connection.")
