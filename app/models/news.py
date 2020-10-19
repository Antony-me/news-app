class News:
    '''
    News class to define Movie Objects
    '''

    def __init__(self,author,title,urlToImage,description,content,url,publishedAt):
        self.author =author
        self.title = title
        self.urlToImage = urlToImage
        self.description = description
        self.content = content
        self.url = url
        self.publishedAt = publishedAt
