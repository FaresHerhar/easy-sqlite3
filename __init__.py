if __name__ == '__main__':
    import Yfetch.mainlib as ml
    import Yfetch.items.channel as channel
    import Yfetch.items.video as video

    video_id = 'BvpAeRGnkJ4'
    channel_id = 'UCnYMOamNKLGVlJgRUbamveA'
    channel_link = ['https://www.youtube.com/user/chemssouvideo',
                    'https://www.youtube.com/channel/UCnoN3upJZ1DPFgX9Y0CA8SA']
    video_link = 'https://www.youtube.com/watch?v=6zge0N962aw'


    print('\n\n** test the IDs extraction **')

    # test the IDs extraction
    print(ml.extractChannelId(channel_link[0]))
    print(ml.extractChannelId(channel_link[1]))
    print(ml.extractVideoId(video_link))

    print('\n\n** test the creation of data for a video and a channel **')

    # test the creation of data for a video and a channel
    ml.makeChannel(True, channel_id) # for channel
    ml.makeVideo(video_id) #for video

    print('\n\n** test the load of the data from the files **')

    # test the load of the data from the files
    print(video.videoAllData(video_id)) # load the video data
    print(channel.channelAllData(channel_id))  # channel the video data