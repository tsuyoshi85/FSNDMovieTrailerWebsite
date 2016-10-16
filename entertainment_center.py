import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and hist toys come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", # NQDA
						"https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", # NQDA
					 "https://youtu.be/5PSNL1qE6VY")

seven_samurai = media.Movie("Seven Samurai",
							"A poor village under attack by bandits recruits seven unemployed samurai to help them defend themselves.", # NQDA
							"https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5MDY1MjU5MF5BMl5BanBnXkFtZTgwNDM2OTE4MzE@._V1_SY1000_CR0,0,712,1000_AL_.jpg", # NQDA
							"https://www.youtube.com/watch?v=7mw6LyyoeGE")

independence_day = media.Movie("Independence Day",
							   "The aliens are coming and their goal is to invade and destroy Earth. Fighting superior technology, mankind's best weapon is the will to survive.", # NQDA
							   "https://upload.wikimedia.org/wikipedia/en/b/bb/Independence_day_movieposter.jpg", # NQDA
							   "https://www.youtube.com/watch?v=oj16vfbsM9A")

school_of_rock = media.Movie("School of Rock",
							 "After being kicked out of a rock band, Dewey Finn becomes a substitute teacher of a strict elementary private school, only to try and turn it into a rock band.", # NQDA
							 "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_.jpg", # NQDA
							 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

basic = media.Movie("Basic",
					"A DEA agent investigates the disappearance of a legendary Army ranger drill sergeant and several of his cadets during a training exercise gone severely awry.", # NQDA
					"https://images-na.ssl-images-amazon.com/images/M/MV5BYzRiMTBlZDktODkwZi00MWU2LTkyMGQtODBiYjRlNDRmMWJlXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,690,1000_AL_.jpg", # NQDA
					"https://youtu.be/BiCIXD5biYI")

movies = [toy_story, avatar, seven_samurai, independence_day, school_of_rock, basic]
fresh_tomatoes.open_movies_page(movies)
