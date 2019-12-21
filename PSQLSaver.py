from BaseHandler import BaseHandler

class PSQLSaver(BaseHandler):

    def handle(self, request):
        if 'info' in request.lower() or 'warning' in request.lower(
        ) or 'critical' in request.lower():
            print('Database PostgreSQL: ' + str(request))
        
        return super().handle(request)