import unittest
import Peliculapro

# Testear el insert

class TestInsert(unittest.TestCase):

	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_insertarPelicula(self):
		pelicula = Peliculapro.Pelicula('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')
		resultado = Peliculapro.Sqlitedb.insertarPelicula(self, pelicula)
		self.assertEqual(resultado, [('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')])
		res2 = Peliculapro.Sqlitedb.insertarPelicula(self, "bhcskbc%$#")
		self.assertEqual(res2, "No se pudo agregar la pelicula a la tabla, probablemente no está en la api")

class TestDelete(unittest.TestCase):
	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')""")
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()


	def test_eliminarPelicula(self):
		pelicula = Peliculapro.Pelicula('111111111', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')
		resultado = Peliculapro.Sqlitedb.eliminarPelicula(self, pelicula)
		self.assertEqual(resultado, "No se puede eliminar la película porque no está en la base de datos")
		resultado2 = Peliculapro.Sqlitedb.eliminarPelicula(self, None)
		self.assertEqual(resultado, "No se puede eliminar la película porque no está en la base de datos")

#Testear el update
class TestUpdate(unittest.TestCase):

	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', Null, Null, Null)""")
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_agregarLink(self):
		pelicula = Peliculapro.Pelicula('111111111', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')
		resultado = Peliculapro.Sqlitedb.agregarLink(self, pelicula, "Youtube.com/watch=gdhbsjkvdh3")
		self.assertEqual(resultado, "No se puede actualizar el link de la película porque no está en la base de datos")
		resultado2 = Peliculapro.Sqlitedb.agregarLink(self, None, "Youtube.com/watch=gdhbsjkvdh3")
		self.assertEqual(resultado2, "No se puede actualizar el link de la película porque no está en la base de datos")
		pelicula2 = Peliculapro.Pelicula('tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')
		resultado3 = Peliculapro.Sqlitedb.agregarLink(self, pelicula2, "Youtube.com/watch=gdhbsjkvdh3")
		self.assertEqual(resultado3, [('tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'Youtube.com/watch=gdhbsjkvdh3')])
		pelicula3 = Peliculapro.Pelicula('tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', None, None, None)
		resultado4 = Peliculapro.Sqlitedb.agregarLink(self, pelicula3, "Youtube.com/watch=gdhbsjkvdh3")
		self.assertEqual(resultado4, [('tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', None, None, 'Youtube.com/watch=gdhbsjkvdh3')])

class TestSelect(unittest.TestCase):

	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', Null, Null, Null)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')""")
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_consultarPelicula(self):
		pelicula = Peliculapro.Pelicula('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')
		resultado = Peliculapro.Sqlitedb.consultarPelicula(self, pelicula)
		self.assertEqual(resultado, [('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')])
		resultado2 = Peliculapro.Sqlitedb.consultarPelicula(self, None)
		self.assertEqual(resultado2, "La película que buscas no está en la base de datos")
		pelicula2 = Peliculapro.Pelicula('tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')
		resultado3 = Peliculapro.Sqlitedb.consultarPelicula(self, pelicula2)
		self.assertEqual(resultado3, [('tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')])
		pelicula3 = Peliculapro.Pelicula('tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', None, None, None)
		resultado4 = Peliculapro.Sqlitedb.consultarPelicula(self, pelicula3)
		self.assertEqual(resultado4, [('tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', None, None, None)])

class TestGetSqlite(unittest.TestCase):

	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', Null, Null, Null)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')""")
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_get_pelicula(self):
		res = Peliculapro.Sqlitedb.get_pelicula(self, "It")
		pelicula = Peliculapro.Pelicula('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')
		self.assertEqual(res.id, pelicula.id)
		res2 = Peliculapro.Sqlitedb.get_pelicula(self, "bhdlfnjla")
		self.assertEqual(res2, None)
		res3 = Peliculapro.Sqlitedb.get_pelicula(self, 'Spider Man 2')
		pelicula2 = Peliculapro.Pelicula('tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', None, None, None)
		self.assertEqual(res3.id, pelicula2.id)

class TestGetOMDBApi(unittest.TestCase):

	def setUp(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute("""CREATE TABLE IF NOT EXISTS peliculas (
					ID text PRIMARY KEY,
					TITULO text,
					GENERO text,
					FECHA_DE_LANZAMIENTO text,
					POSTER text,
					RATING text,
					SINOPSIS text,
					TRAILER text,
					RELACIONADAS text,
					LINK text)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt1245672', 'Spider Man', 'Action, Fiction, SuperHeroes', '08 Sep 2003', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.4', 'A student obtain powers from a spider', 'http://youtube.com/whatch=ruefon321nknd', 'Spider Man 2, Spider Man 3', 'www.cuevana.com')""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt8839922', 'Spider Man 2', 'Action, Fiction, SuperHeroes', '17 Jun 2005', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '9.9', 'A student obtain powers from a spider', Null, Null, Null)""")
		c.execute("""INSERT INTO peliculas VALUES (
		'tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether', 'http://youtube.com/whatch=ruefonhfkjdnknd', 'It 2, It 3', 'www.cuevana.com')""")
		conn.commit()
		conn.close()

	def tearDown(self):
		conn = Peliculapro.sqlite3.connect('peliculas.db')
		c = conn.cursor()
		c.execute('''DELETE FROM peliculas''')
		conn.commit()
		conn.close()

	def test_get_pelicula(self):
		api = Peliculapro.OmdbApi()
		res = Peliculapro.OmdbApi.get_pelicula(api, "It")
		pelicula = Peliculapro.Pelicula('tt1396484', 'It', 'Drama, Horror, Thriller', '08 Sep 2017', 'https://m.media-amazon.com/images/euihfiuehfihefiukefjnfkjdn.jpg', '7.4', 'In the summer of 1989, agroup of kids band toghether to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.', 'http://youtube.com/whatch=ruefonhfkjdnknd')
		self.assertEqual(res.id, pelicula.id)
		res2 = Peliculapro.OmdbApi.get_pelicula(api, "562re7gdwqud")
		self.assertEqual(res2, "No se encontró la pelicula en la Api")
		res3 = Peliculapro.OmdbApi.get_pelicula(api, 'Toy Story 3')
		pelicula2 = Peliculapro.Pelicula("tt0435761", 'Toy Story 3', 'Animation, Adventure, Comedy, Family, Fantasy', '18 Jun 2010', "https://m.media-amazon.com/images/M/MV5BMTgxOTY4Mjc0MF5BMl5BanBnXkFtZTcwNTA4MDQyMw@@._V1_SX300.jpg", '8.3', "The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.", None, None, None)
		self.assertEqual(res3.id, pelicula2.id)

if __name__ == '__main__':
	unittest.main()
#FALTA TEST DE CONSULTAR, CREAR TABLA, GET PELICULA DE SQLITE Y OMDB
