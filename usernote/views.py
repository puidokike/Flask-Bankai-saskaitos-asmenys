from usernote import app, db
from .models import Saskaita, Bankas, Asmuo
from .forms import InfoForm, AsmuoForm, BankasForm, SaskaitaForm
from flask import render_template, redirect, url_for


@app.route('/')
def home():
    all_saskaitos = Saskaita.query.all()
    all_bankai = Bankas.query.all()
    all_asmenys = Asmuo.query.all()
    return render_template('index.html', saskaitos=all_saskaitos, bankai=all_bankai, asmenys=all_asmenys)


@app.route('/info', methods=['GET', 'POST'])
def asmuo_info():
    form = InfoForm()
    if form.validate_on_submit():
        asmuo = Asmuo.query.get(form.id.data)
        saskaita = Saskaita.query.filter_by(asmuo_id=asmuo.id)
        return render_template('asmuo_info.html', asmuo=asmuo, saskaita=saskaita)
    return render_template('info.html', form=form)


@app.route('/asmuo', methods=['GET', 'POST'])
def asmuo():
    all_asmenys = Asmuo.query.all()
    form = AsmuoForm()
    if form.validate_on_submit():
        new_asmuo = Asmuo(vardas=form.vardas.data, pavarde=form.pavarde.data, ak=form.ak.data, tel=form.tel.data)
        db.session.add(new_asmuo)
        db.session.commit()
        all_asmenys = Asmuo.query.all()
        return render_template('asmuo.html', form=form, asmenys=all_asmenys)
    return render_template('asmuo.html', form=form, asmenys=all_asmenys)


@app.route('/bankas', methods=['GET', 'POST'])
def bankas():
    all_bankai = Bankas.query.all()
    form = BankasForm()
    if form.validate_on_submit():
        new_bankas = Bankas(pavadinimas=form.pavadinimas.data,
                            adresas=form.adresas.data,
                            banko_kodas=form.banko_kodas.data,
                            swift=form.swift.data)
        db.session.add(new_bankas)
        db.session.commit()
        all_bankai = Bankas.query.all()
        return render_template('bankas.html', form=form, bankai=all_bankai)
    return render_template('bankas.html', form=form, bankai=all_bankai)


@app.route('/saskaita', methods=['GET', 'POST'])
def saskaita():
    all_saskaitos = Saskaita.query.all()
    form = SaskaitaForm()
    if form.validate_on_submit():
        new_saskaita = Saskaita(numeris=form.numeris.data,
                                balansas=form.balansas.data,
                                asmuo_id=form.asmuo.data.id,
                                bankas_id=form.bankas.data.id)
        db.session.add(new_saskaita)
        db.session.commit()
        all_saskaitos = Saskaita.query.all()
        return render_template('saskaita.html', form=form, saskaitos=all_saskaitos)
    return render_template('saskaita.html', form=form, saskaitos=all_saskaitos)


@app.route('/update_asmuo/<int:id>', methods=['GET', 'POST'])
def update_asmuo(id):
    asmuo = Asmuo.query.get(id)
    form = AsmuoForm()
    if form.validate_on_submit():
        asmuo.vardas = form.vardas.data
        asmuo.pavarde = form.pavarde.data
        asmuo.ak = form.ak.data
        asmuo.tel = form.tel.data
        db.session.commit()
        return redirect(url_for('asmuo'))
    return render_template('update_asmuo.html', form=form, asmuo=asmuo)


@app.route('/update_bankas/<int:id>', methods=['GET', 'POST'])
def update_bankas(id):
    bankas = Bankas.query.get(id)
    form = BankasForm()
    if form.validate_on_submit():
        bankas.pavadinimas = form.pavadinimas.data
        bankas.adresas = form.adresas.data
        bankas.banko_kodas = form.banko_kodas.data
        bankas.swift = form.swift.data
        db.session.commit()
        return redirect(url_for('bankas'))
    return render_template('update_bankas.html', form=form, bankas=bankas)


@app.route('/update_saskaita/<int:id>', methods=['GET', 'POST'])
def update_saskaita(id):
    saskaita = Saskaita.query.get(id)
    form = SaskaitaForm()
    if form.validate_on_submit():
        saskaita.numeris = form.numeris.data
        saskaita.balansas = form.balansas.data
        saskaita.asmuo = form.asmuo.data
        saskaita.bankas = form.bankas.data
        db.session.commit()
        return redirect(url_for('saskaita'))
    return render_template('update_saskaita.html', form=form, saskaita=saskaita)
