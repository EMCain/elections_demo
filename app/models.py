from datetime import date

from app import db 
from sqlalchemy.schema import PrimaryKeyConstraint


class CandidateRace(db.Model):
    """
    the candidate is running in the race (or considering it, has run, etc.)
    """
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=False)
    status = db.Column(db.Integer) # TODO add a constraint; this can be 'declared', 'considering', 'won', 'lost', etc. 
    write_in = db.Column(db.Boolean, default=False) 

    candidate = db.relationship('Candidate', foreign_keys='CandidateRace.candidate_id')
    race = db.relationship('Race', foreign_keys='CandidateRace.race_id')

    __table_args__ = (
        PrimaryKeyConstraint(candidate_id, race_id),
    )

cand_race = CandidateRace


class Candidate(db.Model):
    """
    a specific person who is running, may run, or has previously run for office 
    """
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(64))
    county = db.Column(db.String(64))

    # TODO many to many with Race
    # races = db.relationship('Race', secondary='candidate_race', lazy='subquery',
    #    backref=db.backref('candidates', lazy=True))
    # TODO many to many with District
    # TODO many to many (or many to one, really) with Contact

class Contact(db.Model):
    """for simplicity's sake, each of these should correspond to only one other record; but they can be in multiple tables, 
    for example candidates, nonprofits, etc. and so it'll probably be represented as a many-to-many relationship."""
    id = db.Column(db.Integer, primary_key=True)
    # these next two columns refer to the specific person  who will be addressed by this contact info. Can leave blank for general org contacts. 
    full_name = (db.String(255), nullable=True)  # e.g. Jane Wong
    title = (db.String(255), nullable=True)  # e.g. Director of Communications

    contact_description = db.Column(db.String(64), nullable=True) # e.g. "primary email for Tina Alvarez' campaign"
    city = db.Column(db.String(64), nullable=True) 
    zip_code_1 = db.Column(db.String(5), nullable=True)
    zip_code_2 = db.Column(db.String(4), nullable=True)
    phone = db.Column(db.String(10), nullable=True)  # can make multiple Contact records for multiple phone numbers
    fax = db.Column(db.String(10), nullable=True)
    email = db.Column(db.String(255), nullable=True)
    notes = db.Column(db.Text(), nullable=True)



class Deadline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    summary = db.Column(db.String(64))
    description = db.Column(db.Text())
    category = db.Column(db.String(64))
    nonprofit = db.Column(db.ForeignKey())
    # could imagine this as many-to-many but probably simpler not to and allow the interface to bulk add/edit the same deadlines for multiple govt. agencies. 
    govt_body = db.Column(db.ForeignKey())  

class GovernmentBody(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.Text())
    category = db.Column(db.String(64))

class Nonprofit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    # TODO figure out how to better model cause areas 
    description = db.Column(db.Text())


class Race(db.Model):
    # in the sense of "election contest for a specific seat," not "ethnic group"
    # Not sure if we want to have an "election" object or not but it's low priority
    id = db.Column(db.Integer, primary_key=True)
    # TODO this should be a Date/not care about time, required, not default to now, rename to "election day" or something
    date = db.Column(db.DateTime, default=date.today())   
    office_name = db.Column(db.String(255))  # TODO eliminate in favor of a fk relationship with Office

    # office_id = db.Column(db.Integer, db.ForeignKey('office.id'))

    candidates = db.relationship('Candidate', secondary='candidate_race', lazy='subquery',
        backref=db.backref('races', lazy=True))


class Office(db.Model):
    """
    a specific government office, like "Governor of Oregon" or "Portland City Council Seat #3" 
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    # TO DO make this its own class once I can get more info from ColorPAC
    district = db.Column(db.String(255))