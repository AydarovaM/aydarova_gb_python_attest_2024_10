from Note import Note
from datetime import datetime
import json

class Notebook:
    def __init__(self):
        self.notes = []
        self.last_id = 0

    def add_note(self, new_note) -> bool:
        if type(new_note) is Note:
            self.last_id = new_note.id
            self.notes.append(new_note)
            return True
        else:
            return False
        
    def find_note_by_id(self, id) -> Note:
        for note in self.notes:
            if note.id == id:
                return note
        return
        
    def delete_note(self, id) -> bool:
        note = self.find_note_by_id(id)
        if type(note) is Note:
            self.notes.remove(note)
            return True  
        return False
        
    def print_all(self):
        print("All Notes:")
        for note in self.notes:
            print(note.to_string())
            print("")
        print("End of Notes")

    def print_all_titles_and_id(self):
        print("All Notes:")
        for note in self.notes:
            print(note.to_string_id_and_title())
            print("")
        print("End of Notes")
    
    def print_in_range(self, start_date, end_date):
        print(f"All notes in range: {start_date} .. {end_date}")
        for note in self.notes:
            if note.check_if_date_in_range(start_date, end_date):
                print(note.to_string())
                print("")
        print("End of Notes")

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)
    
    @staticmethod
    def fromJSON(last_id, notes):
        notebook = Notebook()
        notebook.last_id = last_id
        notebook.notes = []
        print("notes")
        for i in notes:
            note = Note.from_dict(i["id"], i["date"], i["title"], i["text"])
            notebook.add_note(note)
            print(i)
        
        #notebook.notes = Note[](notes)
        return notebook
