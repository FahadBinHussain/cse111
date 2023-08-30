class MediaItem:
    total_podcast=0
    podcast_repo=[]
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        MediaItem.total_podcast+=1
        MediaItem.podcast_repo.append(self)


    def get_info(self):
        return f"{self.title} ({self.duration} mins)"
    
class Podcast(MediaItem):
    def __init__(self, title, duration, host, *guests):
        super().__init__(title, duration)
        self.host = host
        self.guests = list(guests)

    def get_info(self):
        return f"{self.title} ({self.duration} mins) hosted by {self.host}"

    def add_guest(self, *guests):
        self.guests.extend(guests)

    def guest_info(self):
        if len(self.guests) == 1:
            print(f"The guest of today's Podcast is: {self.guests[0]}")
        else:
            print(f"The updated guest list of today's Podcast is:")
            for i, guest in enumerate(self.guests, 1):
                print(f"{i}. {guest}")

    @classmethod
    def details(cls):
        print("Details of all the Podcast:")
        print(f"Total Number of Podcast:{cls.total_podcast}")
        print("Other Details:")
        for podcast in cls.podcast_repo:
            print(f"Title: {podcast.title}")
            print(f"Host: {podcast.host}")
            print("----------------------")

#Driver Code:
podcast1 = Podcast("Tech Talk", 30, "Alex Smith", 'Sam Carry')
print(podcast1.get_info())
print('1#######################')
podcast1.guest_info()
print('2#######################')
podcast1.add_guest('Julie Chen')
podcast1.guest_info()
print('3#######################')
Podcast.details()
print('4#######################')
podcast2 = Podcast("Talk", 50, "Sara Gilbert", "Jack Paul")
print('5#######################')
podcast2.guest_info()
print('6#######################')
Podcast.details()
print('7#######################')
print(podcast2.get_info())
podcast2.add_guest('Wade Smith', 'Jane Jones')
podcast2.guest_info()
