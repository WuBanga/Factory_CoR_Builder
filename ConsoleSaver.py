from BaseHandler import BaseHandler

class ConsoleSaver(BaseHandler):

    def handle(self, request):
        if 'debug' in request.lower():
            print('Console: ' + str(request))
        
        return super().handle(request)