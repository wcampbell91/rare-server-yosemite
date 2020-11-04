import datetime

class Comment():
     
      def __init__(self, id, subject, content, author, post_id):
          self.id = id
          self.subject = subject
          self.content = content
          self.author = author
          self.post_id = post_id
          # self.creation_date = datetime.datetime.now()
