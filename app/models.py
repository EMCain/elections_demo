from app import db 
from sqlalchemy.schema import PrimaryKeyConstraint

class Candidate(db.Model):
    """
    a specific person who is running, may run, or has previously run for office 
    """
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(64))
     # TODO change these fields to contact info model 
    city = db.Column(db.String(64)) 
    county = db.Column(db.String(64))
    zip_code_1 = db.Column(db.String(5))
    zip_code_2 = db.Column(db.String(4))

    # TODO many to many with Race 

class CandidateRace(db.Model):
    """
    the candidate is running in the race (or considering it, has run, etc.)
    """
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=False)
    status = db.Column(db.Integer) # TODO add a constraint; this can be 'declared', 'considering', 'won', 'lost', etc. 
    write_in = db.Column(db.Boolean, default=False) 

    __table_args__ = (
        PrimaryKeyConstraint(candidate_id, race_id),
    )

class Race(db.Model):
    # in the sense of "election contest for a specific seat," not "ethnic group"
    # Not sure if we want to have an "election" object or not but it's low priority
    id = db.Column(db.Integer, primary_key=True)
    # date = db.Column(db.Date(), null=False)  getting weird bugs with this 
    office_name = db.Column(db.String(255))  # TODO eliminate in favor of a fk relationship with Office

    # office_id = db.Column(db.Integer, db.ForeignKey('office.id'))


class Office(db.Model):
    """
    a specific government office, like "Governor of Oregon" or "Portland City Council Seat #3" 
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    # TO DO make this its own class once I can get more info from ColorPAC
    district = db.Column(db.String(255))