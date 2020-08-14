class MovieDB:

    def __init__(self):
        self.genre_list = []

    def add_genre(self, genre_name):
        gen_ = Genre(genre_name)
        self.genre_list.append(gen_)
        print(f"\'{genre_name}\' is added to genre_list ")

    def find(self, genre_name):
        for gen_ in self.genre_list:
            if genre_name == gen_.genre_name:
                return gen_
            else:
                print("no genre match! add the genre first!")

    def remove_genre(self, genre_name):
        gen_ = Genre(genre_name)
        self.genre_list.remove(gen_)
        print(f"\'{genre_name}\' is removed from genre_list ")

    def pnt(self):
        for gen in self.genre_list:
            print(gen.genre_name)

    def load(self):
        pass


class Genre:

    def __init__(self, genre_name):
        self.genre_name = genre_name
        self.movie_list = []

    def add_movie(self, title):
        mov_ = Movie(title)
        self.movie_list.append(mov_)
        print(f"\'{title}\' is added to movie_list ")

    def remove_movie(self, title):
        mov_ = Movie(title)
        self.movie_list.remove(mov_)
        print(f"\'{title}\' is removed to movie_list ")

    def pnt(self):
        for mov in self.movie_list:
            print(mov.title)


class Movie:
    title = ""

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"title: {self.title}"


if __name__ == '__main__':
    movieDB = MovieDB()

    while True:
        command = input("명령어:").split()
        if command[0] == "add_genre":
            movieDB.add_genre(command[1])

        elif command[0] == "add_movie":
            genre = movieDB.find(command[1])
            genre.add_movie(command[2])

        elif command[0] == "remove_genre":
            movieDB.remove_genre(command[1])

        elif command[0] == "remove_movie":
            genre = movieDB.find(command[1])
            genre.remove_movie(command[2])

        elif command[0] == "print_genre":
            movieDB.pnt()

        elif command[0] == "print_all":

            for _gen in movieDB.genre_list:
                print(_gen.genre_name)
                _gen.pnt()

        elif command[0] == "exit":
            break
        else:
            print("잘못된 입력입니다.")
