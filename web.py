import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

    

todos = functions.get_todos()

st.title('My To-do List')
st.write('Welcome to your to-do list app! Here are the things you need to do today:')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input('Add a new to-do:', placeholder="Shop, clean, sleep", key='new_todo', on_change=add_todo)