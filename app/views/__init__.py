from flask import Flask

def init_app(app: Flask):
    from app.views.developer_tech_view import bp_developer_tech
    app.register_blueprint(bp_developer_tech)