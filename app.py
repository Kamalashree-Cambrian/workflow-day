import streamlit as st
import pandas as pd
from task_manager import add_task

st.set_page_config(page_title="Employee Task Tracker", page_icon="📋")
st.title("📋 Employee Task Tracker")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

employee = st.text_input("Employee Name")
task = st.text_input("Task")
status = st.selectbox("Status", ["To Do", "In Progress", "Done"])

if st.button("Add Task"):
    try:
        add_task(st.session_state.tasks, employee, task, status)
        st.success("Task added!")
    except ValueError as e:
        st.warning(str(e))

if st.session_state.tasks:
    df = pd.DataFrame(st.session_state.tasks)

    status_filter = st.selectbox(
        "Filter by status", ["All"] + sorted(df["Status"].unique().tolist())
    )
    if status_filter != "All":
        df = df[df["Status"] == status_filter]

    st.dataframe(df, use_container_width=True)
else:
    st.info("No tasks yet. Add one above to get started.")
