from datetime import datetime

from ..models.model import db, BlackList, BlackListSchema


class BlackListService:

    def add(self, data):

        if 'email' not in data or 'app_uuid' not in data:
            return {"success" : False, "msg" : "email or app_uuid are missing"}

        if 'blocked_reason' not in data:
            data['blocked_reason'] = None

        blacklist = BlackList(
            email = data['email'],
            app_uuid = data['app_uuid'],
            blocked_reason = data['blocked_reason'],
            ip = data['ip'],
            date_created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        )

        db.session.add(blacklist)
        db.session.commit()

        return {"success" : True, "msg" : f"Email {data['email']} was added to the black list successfully"}

    def get(self, data):
        # Agregar logica get Manuel
        pass
