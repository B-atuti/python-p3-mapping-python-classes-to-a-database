from config import CONN, CURSOR


class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    def __repr__(self):
        return f'{self.id} {self.name}, {self.album}'

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS Songs 
                (id INTEGER PRIMARY KEY, 
                name TEXT, 
                album TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO songs (name, album) VALUES (?,?)
        """
        CURSOR.execute(sql, (self.name, self.album))
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM Songs").fetchone()[0]  # retrieve the ID assigned to the song when
                # it is added to the database and set it as the object ID
        CONN.commit()  # close the connection always after saving

    @classmethod
    def create(cls, name, album):  # create and save songs using one method
        song = Song(name, album)
        song.save()
        return song

# CURSOR.execute(" DROP TABLE IF EXISTS Songs")
# Song.create_table()
# song1 = Song("Hello", 15)
# song2 = Song("Jail", 17)
# song3 = Song("Dear God", 13)
# song1.save()
# song2.save()
# song3.save()
#
song4 = Song.create("Dear Mama", "Tupac Shakur")
print(song4)

# songs = CURSOR.execute('SELECT * FROM songs')
# for song in songs:  # print song records from the db
#     print(song)

# print(song1, song2, song3)  # print song OBJECTS