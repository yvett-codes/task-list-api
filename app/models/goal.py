from app import db

class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goal", lazy=True)

    def to_dict(self):
        goal_as_dict = {}
        goal_as_dict["id"] = self.goal_id
        goal_as_dict["title"] = self.title
        return goal_as_dict
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title = data_dict["title"]
        )