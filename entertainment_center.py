import media
import fresh_tomatoes

'''
Using media class to store the values for my favorite movies,
using fresh_tomatoes to add the html,javascript, and css
'''
'''
I left the links as-is on purpose, I think the code looks ugly with them broken up
'''

toy_story = media.Movie("Toy Story",
                        "A story about a boy whose toys come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


old_school = media.Movie("Old School",
                         "Man finds wife cheating, and then moves to a college campus",
                         "https://upload.wikimedia.org/wikipedia/en/2/21/Old_s_poster.jpg",
                         "https://www.youtube.com/watch?v=FE4XhgHrmAE")

queen_of_the_damned = media.Movie("Queen of the Damned",
                                  "A modern rockstar vampire has awoken an ancient force",
                                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYxNDEyMzEzMV5BMl5BanBnXkFtZTYwMDM1NjA3._V1_.jpg",
                                  "https://www.youtube.com/watch?v=2Gu9HtN05sc&t=56s")

friday = media.Movie("Friday",
                     "Craig gets fired on his day off and things progressivley get worse",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BYmEwNjNlZTUtNzkwMS00ZTlhLTkyY2MtMjM2MzlmODQyZGVhXkEyXkFqcGdeQXVyNTI4MjkwNjA@._V1_.jpg",
                     "https://www.youtube.com/watch?v=umvFBoLOOgo")

how_to_train_your_dragon = media.Movie("How to Train Your Dragon",
                                       "After being disowned by his father Hickup has to prove himself",
                                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5NDQyMjc2NF5BMl5BanBnXkFtZTcwMjg5ODcyMw@@._V1_SY1000_CR0,0,672,1000_AL_.jpg",
                                       "http://www.imdb.com/title/tt0892769/videoplayer/vi1158218777?ref_=tt_ov_vi")

incredibles = media.Movie("The Incredibles",
                          "After the world shuns them superheros, are forced to be normal. Then evil shows itself",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY5OTU0OTc2NV5BMl5BanBnXkFtZTcwMzU4MDcyMQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                          "https://www.youtube.com/watch?v=eZbzbC9285I")
'''
Passes the movies and values to fresh_tomatoes
which has the html,css,and javascript
'''

movies = (toy_story, old_school,
          queen_of_the_damned, friday,
          how_to_train_your_dragon, incredibles)
fresh_tomatoes.open_movies_page(movies)
