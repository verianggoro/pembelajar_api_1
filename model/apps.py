from app import db, ma


class Employed(db.Model):
    __tablename__ = 'employed'
    __table_args__ = {'extend_existing': True}


class EmployedSchema(ma.ModelSchema):
    class Meta:
        model = Employed
