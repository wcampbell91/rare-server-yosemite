from datetime import date

class Post():
     
      def __init__(self, id, title, content, category, imgUrl, tag_id):
          self.id = id
          self.title = title
          self.content = content
          self.category = category
          self.imgUrl = imgUrl
          self.publishDate = date.today()
          self.tag_id = tag_id
