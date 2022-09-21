from wtforms import Form, BooleanField, StringField, PasswordField, validators


class RegistrationForm(Form):
    name = StringField("Name", [validators.Length(min=4, max=25)])
    username = StringField("Username", [validators.Length(min=4, max=25)])
    email = StringField(
        "Email ID", [validators.Length(min=6, max=55), validators.Email()]
    )
    password = PasswordField(
        "Password",
        [
            validators.DataRequired(),
            validators.EqualTo("confirm_password", message="passwords must match!"),
        ],
    )
    confirm_password = PasswordField("Confirm Password")
