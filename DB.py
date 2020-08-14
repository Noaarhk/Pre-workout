if __name__ == '__main__':
    class MovieDB:
        def __init__(self):
            self.genre_list = []

        def add_genre(self,genre_name):
            Gen_ = Ganre(genre_name)
            self.genre_list.append(Gen_)

        def find(self,genre_name):
            for genre in self.genre_list:
                if genre_name == genre.genre_name:
                    return genre

    class Ganre:
        def __init__(self, genre_name):
            self.genre_name = genre_name
            self.movie_list = []


    class Movies:
        def __init__(self, title):
            self.title = title


DB_1 = MovieDB()
DB_1.add_genre('sf')
print(DB_1.genre_list[0].genre_name)
