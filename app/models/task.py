from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True)
    goal_id = db.Column(db.Integer, db.ForeignKey("goal.goal_id"), nullable=True)
    goal = db.relationship("Goal", back_populates="tasks")

    def to_dict(self):
        task_as_dict = {}
        task_as_dict["id"] = self.task_id
        task_as_dict["title"] = self.title
        task_as_dict["description"] = self.description
        task_as_dict["is_complete"] = bool(self.completed_at)
        if self.goal_id:
            task_as_dict["goal_id"] = self.goal_id
        return task_as_dict
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            title = data_dict["title"],
            description = data_dict["description"]
        )
