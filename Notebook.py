from Note import Note

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
        print("End of Notes")

    def print_all_titles_and_id(self):
        print("All Notes:")
        for note in self.notes:
            print(note.to_string_id_and_title())
        print("End of Notes")
    

