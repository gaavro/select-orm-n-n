from flask import Blueprint, jsonify, request
from app.models.developer_model import Developer
from app.models.tech_model import Tech
from sqlalchemy import func

bp_developer_tech = Blueprint('bp_developer_tech', __name__)

@bp_developer_tech.get("/developers")

def get_devs():
    keys = request.args.keys()
    tech = str(request.args.get('tech'))
    job = str(request.args.get('job_role'))
    age = request.args.get('age')
    if request.args == {}:
        list = Developer.query.all()

    if "tech" in keys:
        list = Developer.query.join(Developer.result).filter(
            func.lower(Tech.name)==tech.lower()).all()

    if "age" in keys:
        list = Developer.query.filter(Developer.age==age).all()

    if "job_role" in keys:
        list = Developer.query.filter(
            func.lower(Developer.job_role)==job.lower()).all()

    if "tech" in keys and "job_role" in keys:
        list = Developer.query.join(Developer.result).filter(
            func.lower(Tech.name)==tech.lower(),
            func.lower(Developer.job_role)==job.lower()).all()

    if "tech" in keys and "job_role" in keys and "age" in keys:
        list = Developer.query.join(Developer.result).filter(
            func.lower(Tech.name)==tech.lower(),
            Developer.age==age,
            func.lower(Developer.job_role)==job.lower()).all()
            
    return jsonify([
        {
            "name": dev.name,
            "age": dev.age,
            "job_role": dev.job_role,
            "technologies": [
                {
                "name": tech.name
                } for tech in dev.technologies
            ]
        } for dev in list
    ]), 200