class Builder:
    def AddFrom(self, sender):
        self.sender = sender

    def AddTo(self, user):
        self.user = user

    def AddTitle(self, title):
        self.title = title

    def AddText(self, text):
        self.text = text

    def GetEmail(self):
        return f"{self.sender}\n {self.user}\n {self.title}\n\t {self.text}"