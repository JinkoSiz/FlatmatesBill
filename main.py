from flask.views import MethodView
from wtforms import Form, StringField, SubmitField, FloatField, IntegerField
from flask import Flask, render_template, request
from flatmates_bill.flat import Bill, Flatmate

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=bill_form)


class ResultPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)

        amount = bill_form.amount.data
        period = bill_form.period.data

        first_name = bill_form.first_name.data
        days_first = bill_form.days_first.data

        second_name = bill_form.second_name.data
        days_second = bill_form.days_second.data

        the_bill = Bill(amount=amount, period=period)

        flatmate_first = Flatmate(name=first_name, days_in_house=days_first)
        flatmate_second = Flatmate(name=second_name, days_in_house=days_second)

        return render_template('results.html', first_name=flatmate_first.name, second_name=flatmate_second.name,
                               first_amount=flatmate_first.pays(bills=the_bill, flatmate2=flatmate_second),
                               second_amount=flatmate_second.pays(bills=the_bill, flatmate2=flatmate_first))


class BillForm(Form):
    amount = FloatField('Bill Amount: ', default=100.75)
    period = StringField('Bill Period: ', default='April 2023')

    first_name = StringField('Name: ', default='John')
    days_first = IntegerField('Days in the house: ', default=20)

    second_name = StringField('Name: ', default='Marry')
    days_second = IntegerField('Days in the house: ', default=12)

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))

app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))

app.add_url_rule('/results', view_func=ResultPage.as_view('results_page'))

app.run(debug=True)
