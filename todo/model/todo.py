class Todo:

    def __init__(self, code_id: int, title: str, description: str):
        self.code_id:  int = code_id
        self.title:  str = title
        self.description:  str =  description
        self.completed: bool = False
        self.tags: list[str] = []


    def mark_complete(self):
      self.completed = True

    def add_tags(self, tag: str):
       self.tag: str = tag
       if self.tag is not self.tags:
             self.tags.append(tag)

    def __str__(self) -> str:
     return f"{self.  code_id:} - {self.tilte}"

class TodoBook:

    def __init__(self):
        self.todos = todos = {}
