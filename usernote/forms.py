from .models import Asmuo, Bankas
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField, IntegerField
    )
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField


def asmuo_query():
    return Asmuo.query


def bankas_query():
    return Bankas.query


class SaskaitaForm(FlaskForm):
    numeris = StringField('Saskaitos numeris', [DataRequired()])
    balansas = IntegerField('Balansas', [DataRequired()])

    asmuo = QuerySelectField(
        query_factory=asmuo_query,
        allow_blank=False,
        get_label='vardas',
        get_pk=lambda x: str(x)
    )
    bankas = QuerySelectField(
        query_factory=bankas_query,
        allow_blank=False,
        get_label='pavadinimas',
        get_pk=lambda x: str(x)
    )
    submit = SubmitField('Submit')


class AsmuoForm(FlaskForm):
    vardas = StringField('Vardas', [DataRequired()])
    pavarde = StringField('Pavarde', [DataRequired()])
    ak = IntegerField('Asmens kodas', [DataRequired()])
    tel = StringField('Tel.nr.', [DataRequired()])
    submit = SubmitField('Submit')


class BankasForm(FlaskForm):
    pavadinimas = StringField('Pavadinimas', [DataRequired()])
    adresas = StringField('Adresas', [DataRequired()])
    banko_kodas = StringField('Banko kodas', [DataRequired()])
    swift = StringField('SWIFT', [DataRequired()])
    submit = SubmitField('Submit')


class InfoForm(FlaskForm):
    id = IntegerField('Asmens ID', [DataRequired()])
    submit = SubmitField('Submit')