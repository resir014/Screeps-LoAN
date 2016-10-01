from screeps_loan.models import db

class UserQuery():
    def find_name_by_alliances(self, alliances):
        query = "SELECT ign, alliance FROM users where alliance = ANY(%s)"
        result = db.find_all(query, (alliances,))
        return [{"name": row[0], "alliance": row[1]} for row in result]

    def update_alliance_by_screeps_id (self, id, alliance):
        query = "UPDATE users SET alliance = %s WHERE screeps_id=%s"
        db.execute(query, (alliance, id))