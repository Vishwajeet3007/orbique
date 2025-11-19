# app.py
import streamlit as st
from PIL import Image
import qrcode
import io

st.set_page_config(page_title="Billing - Streamlit", layout="centered")

# --- Styles ---
st.markdown(
    """
    <style>
        .main {
            background-color: #eaf6f2;
            padding: 1.5rem;
        }
        h1, h2 {
            color: #2a6b4a;
            font-family: 'Georgia', serif;
        }
        label { font-weight: 600; }

        .stButton>button {
            background-color: #5aa36a;
            color: white;
            border-radius: 6px;
            padding: 8px 14px;
        }

        .stTextInput>div>input, .stNumberInput>div>input {
            border: 1px solid #cfded8;
            padding: 6px;
            border-radius: 3px;
        }

        .cost-box {
            background-color: #ffffff;
            border: 1px solid #d9e9df;
            padding: 8px;
            border-radius: 4px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

with st.container():
    st.markdown("<div class='main'>", unsafe_allow_html=True)

    st.markdown("<h1>File :execution..</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Billing Details</h2>", unsafe_allow_html=True)

    # ---------------------- Inputs ----------------------
    col1, col2 = st.columns([2, 1])

    with col1:
        item_name = st.text_input("Enter Item Name :")
        item_rate = st.number_input("Enter Item Rate :", min_value=0.0, format="%.2f")
        item_qty = st.number_input("Enter Item Qty :", min_value=0, step=1)

    with col2:
        st.write("")  # spacing
        st.write("")

    # ---------------------- Calculate Button ----------------------
    if st.button("Calculate sum"):
        cost = item_rate * item_qty
        st.session_state["last_cost"] = cost
        st.success(f"Calculated cost: ₹ {cost:,.2f}")

    # ---------------------- Cost Display ----------------------
    st.markdown("### Cost")
    cost_display = st.session_state.get("last_cost", "")

    st.markdown(
        f"<div class='cost-box'>{'₹ ' + format(cost_display, ',.2f') if cost_display != '' else ''}</div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # ---------------------- Payment Section ----------------------
    st.markdown("### Make payment")
    st.write("Choose one of the options below:")

    # Upload QR
    uploaded_qr = st.file_uploader("Upload your QR image (PNG/JPG)", type=["png", "jpg", "jpeg"])

    # Generate QR
    gen_link = st.text_input("Or paste a payment link (UPI / payment URL) to generate a QR:")
    generate_btn = st.button("Generate QR from link")

    qr_image = None

    # Uploaded QR
    if uploaded_qr is not None:
        try:
            qr_image = Image.open(uploaded_qr)
            st.image(qr_image, caption="Uploaded QR", width=240)
        except:
            st.error("Invalid image file.")

    # Generate QR
    if generate_btn and gen_link.strip() != "":
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=8,
            border=2,
        )
        qr.add_data(gen_link.strip())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)

        qr_image = Image.open(buf)
        st.image(qr_image, caption="Generated QR", width=240)

        st.download_button(
            "Download QR image",
            data=buf,
            file_name="payment_qr.png",
            mime="image/png"
        )

    # Make Payment Button
    if st.button("Make payment"):
        if qr_image is None:
            st.warning("No QR provided. Upload an image or generate one.")
        else:
            st.success("QR ready. Show this QR to the payer.")
            st.image(qr_image, caption="Payment QR (preview)", width=360)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- Footer ----------------------
st.markdown(
    """
    <div style='font-size:12px; color:#666; margin-top:10px'>
        Tip: Paste a UPI payment link to generate a QR,  
        or upload your existing QR image.  
        Then click 'Make payment' to show the QR.
    </div>
    """,
    unsafe_allow_html=True,
)
