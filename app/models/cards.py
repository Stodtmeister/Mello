from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
# from .users import user_cards

class Card(db.Model):
    __tablename__ = 'cards'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    listId = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('lists.id')), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    background_color = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # users = db.relationship("User", secondary=user_cards, back_populates="cards")
    comments = db.relationship("Comment", back_populates="card", cascade='all, delete-orphan')
    list = db.relationship("List", back_populates="cards")

    def to_dict(self):
        return {
            'id': self.id,
            'listId': self.listId,
            'name': self.name,
            'description': self.description,
            # 'users': [self_user.to_dict() for self_user in self.users],
            'comments': [comment.to_dict() for comment in self.comments],
            'list': [self.list.to_dict()]
        }

    def to_dict_no_list(self):
        return {
            'id': self.id,
            'listId': self.listId,
            'name': self.name,
            'description': self.description,
            'background_color': self.background_color,
            # 'users': [self_user.to_dict() for self_user in self.users],
            'comments': [comment.to_dict() for comment in self.comments],
        }
