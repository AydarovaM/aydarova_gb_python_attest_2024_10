#Программа должна:
# 1. Уметь создавать заметку (с датой создания/последнего редактирования)
# 2. Уметь сохранять заметку в json-файл
# 3. Уметь выводить список заметок
# 4. Уметь выводить список заметок с указанным диапазоном дат
# 5. Уметь удалять заметку
# 6. Уметь редактировать заметку

from datetime import datetime
from Note import Note
from Notebook import Notebook
import json

def main(): 
    print("==Notes app==")
    #add_test_notes(notebook)
    notebook = load_from_json()
    if type(notebook) is not Notebook:
        notebook = Notebook()

    want_to_exit = False
    while(not want_to_exit):
        want_to_exit = handle_input(notebook)

def handle_input(notebook) -> bool:
    answer = input("Enter 0 to exit,\n1 to output test note,\n2 to create note,\n3 to print all notes,\n4 to enter delete mode,\n5 to enter edit mode,\n6 to print note in date range,\n7 - to save to json-file:\n")
    answer = answer.lower().strip()
    if answer == "0":
        return True
    if answer == "1":
        print_test_note()
    if answer == "2":
        new_note = create_note(notebook.last_id + 1)
        addition_result = notebook.add_note(new_note)
        if not addition_result:
            print("Note was not created!")
    if answer == "3":
        notebook.print_all()

    if answer == "4":
        delete_note(notebook)
    if answer == "5":
        edit_mode(notebook)    
    if answer == "6":
        date_range_mode(notebook)    
    if answer == "7":
        save_to_file(notebook)    
    
    return False

def print_test_note():
    date = datetime.now()
    print(date)
    note = Note(0, date, "TestTitle", "TestText")
    print(note.to_string())

def add_test_notes(notebook):
    note_0 = Note(0, datetime(2010, 10, 10), "TestTitle", "TestText")
    note_1 = Note(1, datetime(2012, 10, 10), "TestTitle2", "TestText2")
    note_2 = Note(2, datetime(2014, 10, 10), "TestTitle3", "TestText3")
    note_3 = Note(3, datetime(2016, 10, 10), "TestTitle4", "TestText4")
    notebook.add_note(note_0)
    notebook.add_note(note_1)
    notebook.add_note(note_2)
    notebook.add_note(note_3)

    

def create_note(id) -> Note:
    print("Create new note")
    answer = input("Enter 0 to cancel or any to proceed:\n")
    if answer == "0":
        return

    title = input("Please enter title:\n")
    text = input("Please enter text:\n")
    date = datetime.now()
    note = Note(id, date, title, text)

    print(note.to_string())

    return note

def delete_note(notebook):
    print("DELETE MODE!")
    note_id = get_note_id(notebook, "Select is of note to delete:", "Enter note's id to remove:")
    deletion_result = notebook.delete_note(note_id)
    if deletion_result:
        print(f"Note with id {note_id} was deleted successfully.")
    else:
        print(f"Note with id {note_id} was not found.")

def get_note_id(notebook, title, input_text) -> int:
    print(title)
    notebook.print_all_titles_and_id()
    note_id_str = input(f"{input_text}\n")
    note_id = int(note_id_str)
    return note_id

def get_date(input_text) -> datetime:
    format = '%Y-%m-%d'
    date_str = input(f"{input_text} in format: {format}\n")
    date_parsed = datetime.strptime(date_str, format)
    return date_parsed

def edit_mode(notebook):
    print("EDIT MODE!")
    note_id = get_note_id(notebook, "Select is of note to edit:", "Enter note's id to edit:")
    note_to_edit = notebook.find_note_by_id(note_id)
    if type(note_to_edit) != Note:
        print(f"Can't find note with id {note_id}")
        return
    
    was_changed = False
    answer = input("Want to change title? (y/n)")
    if answer.lower().strip() == "y":
        print(f"Old title:\n{note_to_edit.title}")
        new_title = input("Enter new title:\n")
        note_to_edit.title = new_title
        was_changed = True

    answer = input("Want to change text? (y/n)")
    if answer.lower().strip() == "y":
        print(f"Old text:\n{note_to_edit.text}")
        new_text = input("Enter new text:\n")
        note_to_edit.text = new_text
        was_changed = True

    if was_changed:
        note_to_edit.date = datetime.now()

def date_range_mode(notebook):
    print("Select range!")
    start_date = get_date("Input start date")
    end_date = get_date("Input end date")
    notebook.print_in_range(start_date, end_date)

def save_to_file(notebook):
    json_data = notebook.toJSON() 
    print("saved to file: notes.txt")
    with open("notes.txt", "w") as text_file:
        text_file.write(json_data)

def load_from_json() -> Notebook:
    with open('notes.txt') as f:
        print("loaded from file: notes.txt")
        json_data = f.read()
        j = json.loads(json_data)
        notebook = Notebook.fromJSON(**j)
        return notebook

main()