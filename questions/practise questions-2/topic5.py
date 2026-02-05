# 1
class Session:
    def __init__(self, topic, duration):
        self.topic = topic
        self.duration = duration  

    def convert_duration(self):
        hours = self.duration // 60
        minutes = self.duration % 60
        return hours, minutes
s = Session("Python Basics", 135)
h, m = s.convert_duration()
print(h, "hours", m, "minutes")


# 2
# Why encapsulation helps prevent bugs
#Encapsulation means hiding internal data and allowing access only through controlled methods.
#this helps prevent bugs because:
#Data cannot be changed accidentally,
#Only valid operations are allowed,
#Internal logic remains safe from misuse.