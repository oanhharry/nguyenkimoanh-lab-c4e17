from youtube_dl import YoutubeDL

#1 dowload single video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=nfs8NYg7yQM'])

#2 multiple video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=sj25Ar9VRqE', 'https://www.youtube.com/watch?v=OmketaeA0m0'])

#3 dowload audio
# options = {
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=c3jHlYsnEe0'])

#4: Search and then download the first video
# options = {
#     'default_search': 'ytsearch',
#     'max_downloads': 1
# }
# dl = YoutubeDL(options)
# dl.download(['Perfect'])

#5: Search and then download the first audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Bài hát viết cho em Phạm Hoài Nam'])
