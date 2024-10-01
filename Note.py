class Note:
    def __init__(self, id, date, title, text):
        self.id = id
        self.date = date
        self.title = title
        self.text = text
    
    def to_string(self) -> str:
        return f"id: {self.id}\ndate: {self.date}\ntitle: {self.title}\ntext: {self.text}"
    
    def to_string_id_and_title(self) -> str:
           return f"id: {self.id} title: {self.title}"

    
