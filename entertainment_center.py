import fresh_tomatoes
import media

donnie_darko = media.Movie("Donnie Darko",
"The troubled title character seeks the meaning behind his Doomsday-related visions",
"https://upload.wikimedia.org/wikipedia/en/d/db/Donnie_Darko_poster.jpg",
"https://youtu.be/ZZyBaFYFySk?t=4s")

wall_E = media.Movie("WALL-E",
"A robot is designed to clean up an abandoned, waste-covered Earth far in the future",
"https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
"https://youtu.be/8-_9n5DtKOc?t=54s")

without_limits = media.Movie("Without Limits",
"Steve Prefontaine pursues success in professional distance running, demonstrating his unparalleled mettle",
"https://upload.wikimedia.org/wikipedia/en/7/7f/Without_limits.jpg",
"https://youtu.be/e8s5DJBDjnA?t=8s")

mr_nobody = media.Movie("Mr. Nobody",
"Nemo Nobody, a 118 year old man and the last mortal on Earth looks back on his life and the multiple universes he existed in",
"https://upload.wikimedia.org/wikipedia/en/3/32/Mr._Nobody_%28film_poster%29.jpg",
"https://youtu.be/mpi0qsp3v_w?t=6s")

scream = media.Movie("Scream",
"A succession of murders by the elusive ghostface killer drives this mysterious horror film",
"https://upload.wikimedia.org/wikipedia/en/7/78/Scream_movie_poster.jpg",
"https://youtu.be/AWm_mkbdpCA?t=10s")

mad_max = media.Movie("Mad Max: Fury Road",
"In post-apocalyptia, Max and Imperator Furiosa evade Immortan Joe and his army",
"https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
"https://www.youtube.com/watch?v=hEJnMQG9ev8")

toy_story = media.Movie("Toy Story",
"A story of a boy and his toys that come to life",
"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
"http://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
"A marine on an alien planet",
"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
"https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
"http://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
"http://www.youtube.com/watch?v=c3sBBxDAqk")

hunger_games = media.Movie("Hunger Games", "A reality show that is real",
"http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
"http://www.youtube.com/watch?v=PbA63a7HObo")

movies = [wall_E, without_limits, mr_nobody, scream, mad_max, toy_story, avatar, school_of_rock, ratatouille, donnie_darko, hunger_games]
fresh_tomatoes.open_movies_page(movies)
