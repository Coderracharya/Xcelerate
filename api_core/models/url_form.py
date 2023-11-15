from wtforms import Form, StringField, validators


class URLForm(Form):
    url = StringField('URL', validators=[validators.URL()])