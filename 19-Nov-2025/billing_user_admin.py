# app.py
import streamlit as st
from PIL import Image
import qrcode
import io
from fpdf import FPDF

st.set_page_config(page_title="Advanced Billing", layout="centered")

# ---------------------- Session State Init ----------------------
if "items" not in st.session_state:
    st.session_state["items"] = []
if "qr_image" not in st.session_state:
    st.session_state["qr_image"] = None
if "admin_logged_in" not in st.session_state:
    st.session_state["admin_logged_in"] = False
if "gst_enabled" not in st.session_state:
    st.session_state["gst_enabled"] = True
if "gst_percent" not in st.session_state:
    st.session_state["gst_percent"] = 18.0

# ---------------------- Styles ----------------------
st.markdown("""
<style>
    .main { background-color: #eaf6f2; padding: 1.5rem; }
    h1, h2 { color: #2a6b4a; font-family: 'Georgia', serif; }
    label { font-weight: 600; }
    .stButton>button { background-color: #5aa36a; color: white; border-radius: 6px; padding: 8px 14px; }
    .stTextInput>div>input, .stNumberInput>div>input { border: 1px solid #cfded8; padding: 6px; border-radius: 3px; }
    .cost-box { background-color: #ffffff; border: 1px solid #d9e9df; padding: 8px; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<h1>Advanced Billing System</h1>", unsafe_allow_html=True)

# ---------------------- Role Selection ----------------------
role = st.selectbox("Select Role:", ["Admin", "User"])

# ---------------------- ADMIN LOGIN ----------------------
if role == "Admin" and not st.session_state["admin_logged_in"]:
    st.subheader("Admin Login")
    admin_user = st.text_input("User ID")
    admin_pass = st.text_input("Password", type="password")
    if st.button("Login"):
        if admin_user == "Vishwajeet3007" and admin_pass == "Vishwajeet@123":
            st.session_state["admin_logged_in"] = True
            st.success("Login Successful!")
        else:
            st.error("Invalid credentials!")

# ---------------------- ADMIN PANEL ----------------------
if role == "Admin" and st.session_state["admin_logged_in"]:
    st.subheader("Admin Panel")

    # -------- Multi-item billing --------
    st.markdown("### Add Items")
    col1, col2, col3 = st.columns(3)
    with col1:
        item_name = st.text_input("Item Name", key="item_name")
    with col2:
        item_rate = st.number_input("Rate", min_value=0.0, format="%.2f", key="item_rate")
    with col3:
        item_qty = st.number_input("Quantity", min_value=0, step=1, key="item_qty")
    if st.button("Add Item"):
        if item_name and item_qty > 0:
            st.session_state["items"].append({"name": item_name, "rate": item_rate, "qty": item_qty})
            st.success(f"Added {item_name}")
        else:
            st.warning("Enter valid item name and quantity")

    # Display items with delete buttons
    if st.session_state["items"]:
        st.markdown("### Current Items")
        total = 0
        for idx, itm in enumerate(st.session_state["items"]):
            col1, col2 = st.columns([4,1])
            with col1:
                st.write(f"{idx+1}. {itm['name']} - ₹{itm['rate']} x {itm['qty']} = ₹{itm['rate']*itm['qty']:.2f}")
            with col2:
                if st.button("Delete", key=f"del_{idx}"):
                    st.session_state["items"].pop(idx)
                    st.experimental_rerun()
            total += itm['rate']*itm['qty']

        # GST option
        st.checkbox("Apply GST", value=st.session_state["gst_enabled"], key="gst_enabled")
        gst_rate = st.number_input("GST %", value=st.session_state["gst_percent"], step=1.0, key="gst_percent")
        st.session_state["gst_percent"] = gst_rate
        gst_amount = (total * gst_rate / 100) if st.session_state["gst_enabled"] else 0
        total_with_gst = total + gst_amount

        st.markdown(f"**Subtotal:** ₹{total:.2f}")
        if st.session_state["gst_enabled"]:
            st.markdown(f"**GST ({gst_rate}%):** ₹{gst_amount:.2f}")
        st.markdown(f"**Total:** ₹{total_with_gst:.2f}")

    # -------- QR Upload / Generate --------
    st.markdown("---")
    st.markdown("### Payment QR")
    uploaded_qr = st.file_uploader("Upload QR image (PNG/JPG)", type=["png", "jpg", "jpeg"])
    gen_link = st.text_input("Or paste payment link to generate QR:")
    if st.button("Generate QR from link") and gen_link.strip():
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=8, border=2)
        qr.add_data(gen_link.strip())
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        st.session_state["qr_image"] = Image.open(buf)
        st.image(st.session_state["qr_image"], caption="Generated QR", width=240)
        st.download_button("Download QR", data=buf, file_name="payment_qr.png", mime="image/png")
        st.success("QR ready for users")

    # Use uploaded QR
    if uploaded_qr is not None:
        st.session_state["qr_image"] = Image.open(uploaded_qr)
        st.image(st.session_state["qr_image"], caption="Uploaded QR", width=240)
        st.success("QR uploaded successfully!")

    # -------- Generate PDF Invoice --------
    if st.button("Generate PDF Invoice"):
        if not st.session_state["items"]:
            st.warning("Add items first!")
        elif st.session_state["qr_image"] is None:
            st.warning("Set QR first!")
        else:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(0, 10, "Invoice", ln=True, align="C")
            pdf.ln(5)
            pdf.set_font("Arial", '', 12)
            total = 0
            for itm in st.session_state["items"]:
                pdf.cell(0, 8, f"{itm['name']} - ₹{itm['rate']} x {itm['qty']} = ₹{itm['rate']*itm['qty']:.2f}", ln=True)
                total += itm['rate']*itm['qty']
            gst_amount = (total * st.session_state["gst_percent"]/100) if st.session_state["gst_enabled"] else 0
            total_with_gst = total + gst_amount
            pdf.ln(5)
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 8, f"Subtotal: ₹{total:.2f}", ln=True)
            if st.session_state["gst_enabled"]:
                pdf.cell(0, 8, f"GST ({st.session_state['gst_percent']}%): ₹{gst_amount:.2f}", ln=True)
            pdf.cell(0, 8, f"Total: ₹{total_with_gst:.2f}", ln=True)
            pdf.ln(10)
            # Save QR temporarily
            buf = io.BytesIO()
            st.session_state["qr_image"].save(buf, format="PNG")
            buf.seek(0)
            pdf.image(buf, x=80, w=50)
            # Download PDF
            pdf_buf = io.BytesIO()
            pdf.output(pdf_buf)
            pdf_buf.seek(0)
            st.download_button("Download PDF Invoice", data=pdf_buf, file_name="invoice.pdf", mime="application/pdf")

# ---------------------- USER SIDE ----------------------
if role == "User":
    st.subheader("Make Payment")
    if st.button("Make Payment"):
        if st.session_state["qr_image"] is None:
            st.warning("QR not set by Admin yet")
        else:
            st.success("Scan this QR to make payment")
            st.image(st.session_state["qr_image"], caption="Payment QR", width=360)

st.markdown("</div>", unsafe_allow_html=True)
