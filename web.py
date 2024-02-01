import streamlit as st
import functions

tasks = functions.get_tasks()
def add_task():

    task = st.session_state["new_task"] + "\n"
    tasks.append(task)
    functions.write_tasks(tasks)


st.title("My Task App")
st.subheader("My app")
st.write("App to for productivity")

for index, task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_tasks(tasks)
        del st.session_state[task]
        st.rerun()

st.text_input(label="Enter a task:", placeholder="Task",
              on_change=add_task, key="new_task")
