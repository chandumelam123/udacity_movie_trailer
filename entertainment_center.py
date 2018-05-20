import media
import fresh_tomatoes
#first movie
winner=media.Movie("Winner","The story of a person who lost his father and mett his father after few years","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvMCIN4RZp5Qh1D93HsbXQaTDncUdsaNv1Uk5yoX6Qlf83klDR","https://www.youtube.com/watch?v=iEokJEmGj94")
#second movie
spyder=media.Movie("Spyder","The story of a person who spy on public and saves them from dangers","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRF5_yDMXkrjHn7T63_XpMzMKJ73Gp7aG9Y-YrOmL_o91EAuYAUTQ","https://www.youtube.com/watch?v=og1zP3u0b4k")
#third movie
sarinodu=media.Movie("Sarinodu","The story of a person who fight with bad people","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStdeOm5YbufbKhLp6cSAo0ULIAFYMjFbZ9n8LmzF3YnL4xkbTW","https://www.youtube.com/watch?v=D42rl5OVYU0")
#fourth movie
dhruva=media.Movie("dhruva","The story of a great police","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSszkg7YGUn-oSsgRs_4nkhS7nAEuT0FcTQRQ2I5xdpNyVNzaQH","https://www.youtube.com/watch?v=r_yVN37aCYI")
#fifth movie
baahubali2=media.Movie("baahubali","The story of a great fighter","https://qph.fs.quoracdn.net/main-qimg-95f2a0c9a6772c729556563d396ed27d-c","https://www.youtube.com/watch?v=qD-6d8Wo3do")
#sixth movie
nanakuprematho = media.Movie("NanakuPrematho","Love towards father","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyBM-sikmdF3iXxXtIKpqwLFRfgOR3fMfDfx-Rs29l8c3hC24A4w","https://www.youtube.com/watch?v=Om69gF1iiT4")
#list of all the movie objects
movies=[winner,spyder,sarinodu,dhruva,baahubali2,nanakuprematho]
#call the function of fresh_tomatoes file
fresh_tomatoes.open_movies_page(movies)
