from flask import Blueprint, render_template, request, session, redirect, url_for
from models import User, OTP, db
from utils import generate_otp
from datetime import datetime

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session["user_id"] = user.id
            return redirect(url_for("auth.color_auth"))

        return render_template("login.html", error="Invalid username or password.")

    return render_template("login.html")


@auth_blueprint.route("/color-auth", methods=["GET", "POST"])
def color_auth():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("auth.login"))

    user = User.query.get(user_id)

    if request.method == "POST":
        selected_color = request.form.get("color")
        if selected_color == user.favorite_color:
            otp_code = generate_otp()
            otp_entry = OTP(user_id=user.id, otp_code=otp_code)
            db.session.add(otp_entry)
            db.session.commit()

            # Send OTP (replace with email integration)
            print(f"OTP for {user.username}: {otp_code}")

            return redirect(url_for("auth.otp_verification"))

        return render_template("color_auth.html", error="Incorrect color.")

    return render_template("color_auth.html")


@auth_blueprint.route("/otp-verification", methods=["GET", "POST"])
def otp_verification():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        entered_otp = request.form.get("otp")
        otp_entry = OTP.query.filter_by(user_id=user_id, otp_code=entered_otp).order_by(OTP.created_at.desc()).first()

        if otp_entry and otp_entry.is_valid():
            session.pop("user_id")
            return redirect(url_for("auth.success"))

        return render_template("otp_verification.html", error="Invalid or expired OTP.")

    return render_template("otp_verification.html")


@auth_blueprint.route("/success")
def success():
    return render_template("success.html")
