import streamlit as st
import db_utility


def report():
	st.markdown("<h1 style='text-align: center; color: black;'>REPORT APP</h1>", unsafe_allow_html=True)
	form = st.form("my_form")
	requested_by = form.text_input("Enter Name")
	kpi = form.selectbox("Select KPI",
		("Uptime", "CPU Utilization", "Memory Utilization", "Temperature"))
	report_type = form.selectbox("Report Type",
		("Raw", "Aggregated"))
	report_priority = form.radio(
    "Report Priority",
    ('Low', 'Medium', 'High'),horizontal=True)

	submit = form.form_submit_button("Submit")
	if submit:
		st.info(f"Report Submitted\n, \
			Details : requested_by :{requested_by}, kpi : {kpi}, \
			report_type : {report_type}, report_priority: {report_priority}")

		db_utility.add_report(requested_by, kpi, report_type, report_priority)


def stats():
	df, size = db_utility.all_records()
	st.subheader(f"Report Submission Count : {size}")
	st.subheader(f"Report details")
	st.write(df)

def main():
	add_selectbox = st.sidebar.selectbox("Select Operation?",("Submit Report", "Report Statistics"))
	if add_selectbox == 'Submit Report':
		report()
	else:
		stats()

if __name__ == '__main__':
	main()