import streamlit as st
import datetime
import pandas as pd
import os

# Fungsi untuk menyimpan data ke file CSV
def save_data(todos):
    df = pd.DataFrame(todos)
    df.to_csv('todos.csv', index=False)

# Fungsi untuk memuat data dari file CSV
@st.cache_data
def load_data():
    if os.path.exists('todos.csv'):
        df = pd.read_csv('todos.csv')
        return df.to_dict('records')
    return []

# Inisialisasi session state
if 'todos' not in st.session_state:
    st.session_state.todos = load_data()

# Konfigurasi halaman
st.set_page_config(
    page_title="Streamlit Todo List",
    page_icon="✅",
    layout="wide"
)

# Sidebar untuk input baru
with st.sidebar:
    st.header("Tambah Todo Baru")
    with st.form(key='todo_form'):
        new_todo = st.text_input("Deskripsi Task")
        due_date = st.date_input("Due Date", datetime.date.today())
        priority = st.selectbox("Prioritas", ["Low", "Medium", "High"])
        submitted = st.form_submit_button("Tambah Task")

        if submitted and new_todo:
            new_task = {
                "task": new_todo,
                "due_date": due_date.strftime("%Y-%m-%d"),
                "priority": priority,
                "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "completed": False
            }
            st.session_state.todos.append(new_task)
            save_data(st.session_state.todos)
            st.success("Task berhasil ditambahkan!")

# Main content
st.title("📝 Todo List Interaktif")
st.write("Aplikasi manajemen task sederhana dengan Streamlit")

# Filter dan pencarian
col1, col2 = st.columns([2, 1])
with col1:
    search_term = st.text_input("Cari task")

with col2:
    filter_priority = st.selectbox(
        "Filter berdasarkan prioritas",
        ["All", "High", "Medium", "Low"]
    )

# Tampilkan todos
for index, todo in enumerate(st.session_state.todos):
    # Filter data
    if search_term.lower() not in todo['task'].lower():
        continue
    if filter_priority != "All" and todo['priority'] != filter_priority:
        continue
    
    # Layout untuk setiap todo item
    with st.container(border=True):
        cols = st.columns([1, 4, 2, 2, 1])
        
        # Checkbox status
        with cols[0]:
            completed = st.checkbox(
                "✓",
                value=todo['completed'],
                key=f"completed_{index}",
                on_change=lambda i=index: toggle_status(i)
            )
        
        # Deskripsi task
        with cols[1]:
            if todo['completed']:
                st.markdown(f"~~{todo['task']}~~")
            else:
                st.markdown(todo['task'])
        
        # Prioritas dengan warna
        with cols[2]:
            priority_color = {
                "High": "🔴",
                "Medium": "🟡",
                "Low": "🟢"
            }
            st.markdown(f"{priority_color[todo['priority']]} {todo['priority']}")
        
        # Due date
        with cols[3]:
            due_date = datetime.datetime.strptime(todo['due_date'], "%Y-%m-%d").date()
            days_left = (due_date - datetime.date.today()).days
            date_color = "red" if days_left < 3 else "green"
            st.markdown(f"Due: <span style='color:{date_color}'>{todo['due_date']}</span>", 
                        unsafe_allow_html=True)
        
        # Tombol hapus
        with cols[4]:
            if st.button("❌", key=f"delete_{index}"):
                delete_todo(index)

def toggle_status(index):
    st.session_state.todos[index]['completed'] = not st.session_state.todos[index]['completed']
    save_data(st.session_state.todos)

def delete_todo(index):
    del st.session_state.todos[index]
    save_data(st.session_state.todos)
    st.rerun()

# Statistik
st.divider()
st.subheader("Statistik Task")
col1, col2, col3 = st.columns(3)
total_tasks = len(st.session_state.todos)
completed_tasks = len([t for t in st.session_state.todos if t['completed']])
pending_tasks = total_tasks - completed_tasks

with col1:
    st.metric("Total Task", total_tasks)

with col2:
    st.metric("Task Selesai", completed_tasks)

with col3:
    st.metric("Task Pending", pending_tasks)
