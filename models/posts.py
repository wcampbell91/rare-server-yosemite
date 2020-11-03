from datetime import date

class Post():
     
      def __init__(self, id, title, content, category_id, header_img):
          self.id = id
          self.title = title
          self.content = content
          self.category_id = category_id
          self.header_img = header_img
          self.publishDate = date.today()
