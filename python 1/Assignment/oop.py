class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def show_info(self):
        print(f'{self.title} the {self.author}')
        book1=book('berserk','fin')
        book1=book('time','emmanuel')
        
