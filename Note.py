import json
from datetime import datetime

class Note:
    def __init__(self, id, date, title, text):
        self.id = id
        self.date = date.strftime("%Y-%m-%d")
        self.title = title
        self.text = text
    
    @staticmethod
    def from_dict(id, date_str, title, text):
        note = Note(int(id), datetime.strptime(date_str, "%Y-%m-%d"), title, text)
        return note

    def to_string(self) -> str:
        return f"id: {self.id}\ndate: {self.date}\ntitle: {self.title}\ntext: {self.text}"
    
    def to_string_id_and_title(self) -> str:
           return f"id: {self.id} title: {self.title}"
    
    def check_if_date_in_range(self, start_date, end_date) -> bool:
         if datetime.strptime(self.date, "%Y-%m-%d") < start_date:
              return False
         if datetime.strptime(self.date, "%Y-%m-%d") > end_date:
              return False
         return True    

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)
    
    @staticmethod
    def fromJSON(date, id, text, title):
         note = Note(id, date, title, text)
         return note