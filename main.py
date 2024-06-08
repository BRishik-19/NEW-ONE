import streamlit as st
import Functions

dir(st)



def update():
    new_todo=st.session_state["todoss"]+"\n"

    new= Functions.get_todos("todos_items.txt")
    new.append(new_todo)

    Functions.write_todos(new, "todos_items.txt")

st.title("My todo app")
st.subheader("This is my new app")
st.write("A simple app adding,editing,completing todos items...")
todos= Functions.get_todos("todos_items.txt")

for ind,i in enumerate(todos):
    checkbox=st.checkbox(i,key=i)
    if checkbox:
        todo= Functions.get_todos("todos_items.txt")
        todo.pop(ind)
        Functions.write_todos(todo, "todos_items.txt")
        del st.session_state[i]
        st.experimental_rerun()



st.text_input(label="",placeholder="add a new todo",key="todoss",on_change=update)
st.session_state
