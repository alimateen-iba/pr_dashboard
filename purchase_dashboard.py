import streamlit as st

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")

import pandas as pd
from datetime import datetime

st.set_page_config(page_title="IBA - Purchase",
                   page_icon=":bar_chart:",
                   layout="wide"
)

def get_data_from_excel():
    df_po = pd.read_excel(
        io='Purchase orders_637997872068804066.xlsx',
#         engine='openpyxl',
        # sheet_name='Processed',
        skiprows=0,
        # usecols='B:AI',
        # nrows=789
    )

    df_pr = pd.read_excel(
        io='Purchase requisitions_637997869601969954.xlsx',
#         engine='openpyxl',
        # sheet_name='Processed',
        skiprows=0,
        # usecols='B:AI',
        # nrows=789
    )

    df_pr['Created date'] = pd.to_datetime(df_pr['Created date'])

    return df_po, df_pr

df_po, df_pr = get_data_from_excel()

po_approval_status_title = "<p style='text-align: center; color: white; font-size: 20px;'>Purchase Order Approval Status</p>"
st.markdown(po_approval_status_title, unsafe_allow_html=True)

col0, col1, col2, col3, col4 = st.columns(5)

with col0:
    poas_draft_title = "<p style='text-align: center; color: white; font-size: 15px;'>Draft</p>"
    st.markdown(poas_draft_title, unsafe_allow_html=True)
    total_draft_po = (df_po['Approval status'] == 'Draft').sum()
    poas_draft_number = f"""<p style='background-color: rgb(50,75,25); text-align: center; color: white; font-size: 25px;'>{total_draft_po}</style><BR></p>"""
    st.markdown(poas_draft_number,unsafe_allow_html=True)

with col1:
    poas_in_review_title = "<p style='text-align: center; color: white; font-size: 15px;'>In Review</p>"
    st.markdown(poas_in_review_title, unsafe_allow_html=True)
    total_in_review_po = (df_po['Approval status'] == 'In review').sum()
    poas_in_review_number = f"""<p style='background-color: rgb(50,75,25); text-align: center; color: white; font-size: 25px;'>{total_in_review_po}</style><BR></p>"""
    st.markdown(poas_in_review_number,unsafe_allow_html=True)

with col2:
    poas_confirmed_title = "<p style='text-align: center; color: white; font-size: 15px;'>Confirmed</p>"
    st.markdown(poas_confirmed_title, unsafe_allow_html=True)
    total_confirmed_po = (df_po['Approval status'] == 'Confirmed').sum()
    poas_confirmed_number = f"""<p style='background-color: rgb(50,75,25); text-align: center; color: white; font-size: 25px;'>{total_confirmed_po}</style><BR></p>"""
    st.markdown(poas_confirmed_number,unsafe_allow_html=True)

with col3:
    poas_approved_title = "<p style='text-align: center; color: white; font-size: 15px;'>Approved</p>"
    st.markdown(poas_approved_title, unsafe_allow_html=True)
    total_approved_po = (df_po['Approval status'] == 'Approved').sum()
    poas_approved_number = f"""<p style='background-color: rgb(50,75,25); text-align: center; color: white; font-size: 25px;'>{total_approved_po}</style><BR></p>"""
    st.markdown(poas_approved_number,unsafe_allow_html=True)

with col4:
    poas_rejected_title = "<p style='text-align: center; color: white; font-size: 15px;'>Rejected</p>"
    st.markdown(poas_rejected_title, unsafe_allow_html=True)
    total_rejected_po = (df_po['Approval status'] == 'Rejected').sum()
    poas_rejected_number = f"""<p style='background-color: rgb(50,75,25); text-align: center; color: white; font-size: 25px;'>{total_rejected_po}</style><BR></p>"""
    st.markdown(poas_rejected_number,unsafe_allow_html=True)

st.markdown('###')

po_status_title = "<p style='text-align: center; color: white; font-size: 20px;'>Purchase Order Status</p>"
st.markdown(po_status_title, unsafe_allow_html=True)

col5, col6, col7, col8 = st.columns(4)

with col5:
    pos_open_order_title = "<p style='text-align: center; color: white; font-size: 15px;'>Open Order</p>"
    st.markdown(pos_open_order_title, unsafe_allow_html=True)
    total_open_po = (df_po['Purchase order status'] == 'Open order').sum()
    pos_open_number = f"""<p style='background-color: rgb(50,75,25); text-align: center; color: white; font-size: 25px;'>{total_open_po}</style><BR></p>"""
    st.markdown(pos_open_number,unsafe_allow_html=True)

with col6:
    pos_received_title = "<p style='text-align: center; color: white; font-size: 15px;'>Received</p>"
    st.markdown(pos_received_title, unsafe_allow_html=True)
    total_received_po = (df_po['Purchase order status'] == 'Received').sum()
    pos_received_number = f"""<p style='background-color: rgb(50,75,25); text-align: center; color: white; font-size: 25px;'>{total_received_po}</style><BR></p>"""
    st.markdown(pos_received_number,unsafe_allow_html=True)

with col7:
    pos_invoiced_title = "<p style='text-align: center; color: white; font-size: 15px;'>Invoiced</p>"
    st.markdown(pos_invoiced_title, unsafe_allow_html=True)
    total_invoiced_po = (df_po['Purchase order status'] == 'Invoiced').sum()
    pos_invoiced_number = f"""<p style='background-color: rgb(50,75,25); text-align: center; color: white; font-size: 25px;'>{total_invoiced_po}</style><BR></p>"""
    st.markdown(pos_invoiced_number,unsafe_allow_html=True)

with col8:
    pos_cancelled_title = "<p style='text-align: center; color: white; font-size: 15px;'>Cancelled</p>"
    st.markdown(pos_cancelled_title, unsafe_allow_html=True)
    total_cancelled_po = (df_po['Purchase order status'] == 'Canceled').sum()
    pos_cancelled_number = f"""<p style='background-color: rgb(50,75,25); text-align: center; color: white; font-size: 25px;'>{total_cancelled_po}</style><BR></p>"""
    st.markdown(pos_cancelled_number,unsafe_allow_html=True)

st.markdown('---')

pr_status_title = "<p style='text-align: center; color: white; font-size: 20px;'>Purchase Requisition Status</p>"
st.markdown(pr_status_title, unsafe_allow_html=True)

start_dt = st.date_input('Start date', df_pr['Created date'].min())
end_dt = st.date_input('End date', df_pr['Created date'].max())

if start_dt <= end_dt:
    df_pr = df_pr[df_pr['Created date'] >= datetime(start_dt.year, start_dt.month, start_dt.day)]
    df_pr = df_pr[df_pr['Created date'] <= datetime(end_dt.year, end_dt.month, end_dt.day)]

    col9, col10, col11, col12, col13, col14 = st.columns(6)

    with col9:
        prs_draft_title = "<p style='text-align: center; color: white; font-size: 15px;'>Draft</p>"
        st.markdown(prs_draft_title, unsafe_allow_html=True)
        total_draft_pr = (df_pr['Status'] == 'Draft').sum()
        pr_draft_number = f"""<p style='background-color: rgb(150,175,135); text-align: center; color: white; font-size: 25px;'>{total_draft_pr}</style><BR></p>"""
        st.markdown(pr_draft_number,unsafe_allow_html=True)

    with col10:
        prs_in_review_title = "<p style='text-align: center; color: white; font-size: 15px;'>In Review</p>"
        st.markdown(prs_in_review_title, unsafe_allow_html=True)
        total_in_review_pr = (df_pr['Status'] == 'In review').sum()
        pr_in_review_number = f"""<p style='background-color: rgb(150,175,135); text-align: center; color: white; font-size: 25px;'>{total_in_review_pr}</style><BR></p>"""
        st.markdown(pr_in_review_number,unsafe_allow_html=True)
        
    with col11:
        prs_cancelled_title = "<p style='text-align: center; color: white; font-size: 15px;'>Cancelled</p>"
        st.markdown(prs_cancelled_title, unsafe_allow_html=True)
        total_cancelled_pr = (df_pr['Status'] == 'Cancelled').sum()
        pr_cancelled_number = f"""<p style='background-color: rgb(150,175,135); text-align: center; color: white; font-size: 25px;'>{total_cancelled_pr}</style><BR></p>"""
        st.markdown(pr_cancelled_number,unsafe_allow_html=True)

    with col12:
        prs_rejected_title = "<p style='text-align: center; color: white; font-size: 15px;'>Rejected</p>"
        st.markdown(prs_rejected_title, unsafe_allow_html=True)
        total_rejected_pr = (df_pr['Status'] == 'Rejected').sum()
        pr_rejected_number = f"""<p style='background-color: rgb(150,175,135); text-align: center; color: white; font-size: 25px;'>{total_rejected_pr}</style><BR></p>"""
        st.markdown(pr_rejected_number,unsafe_allow_html=True)

    with col13:
        prs_approved_title = "<p style='text-align: center; color: white; font-size: 15px;'>Approved</p>"
        st.markdown(prs_approved_title, unsafe_allow_html=True)
        total_approved_pr = (df_pr['Status'] == 'Approved').sum()
        pr_approved_number = f"""<p style='background-color: rgb(150,175,135); text-align: center; color: white; font-size: 25px;'>{total_approved_pr}</style><BR></p>"""
        st.markdown(pr_approved_number,unsafe_allow_html=True)

    with col14:
        prs_closed_title = "<p style='text-align: center; color: white; font-size: 15px;'>Closed</p>"
        st.markdown(prs_closed_title, unsafe_allow_html=True)
        total_closed_pr = (df_pr['Status'] == 'Closed').sum()
        pr_closed_number = f"""<p style='background-color: rgb(150,175,135); text-align: center; color: white; font-size: 25px;'>{total_closed_pr}</style><BR></p>"""
        st.markdown(pr_closed_number,unsafe_allow_html=True)

else:
    st.error('Start date must be greater than End date')

st.dataframe(df_pr)
