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

class Sources:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

