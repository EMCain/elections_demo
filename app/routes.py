from flask import Flask, render_template, url_for

from app import app
from app.models import Candidate, Race

@app.route('/')
def hello_world():
    candidates = Candidate.query.all()
    for c in candidates: 
        c.race_names = [f'{r.office_name} on {r.date.strftime("%B %e, %Y")}' for r in c.races]
    return render_template(
        'base.html', 
        content='page content here', 
        title='Example Page', 
        candidates=candidates
    )