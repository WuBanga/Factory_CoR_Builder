from BaseHandler import BaseHandler
from Builder import Builder


class EmailSaver(BaseHandler):
    def handle(self, request):
        builder = Builder()
        if 'critical' in request.lower():
            builder.AddFrom('test@mail.ru')
            builder.AddTo('user@mail.ru')
            builder.AddTitle('Logs')
            builder.AddText(str(request))
            print(f'\n{builder.GetEmail()}')
        
        return super().handle(request)