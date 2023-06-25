from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    customer_name = request.form['customer_name']
    item_name = request.form['item_name']
    item_quantity = request.form['item_quantity']
    item_price = request.form['item_price']
    total_amount = float(item_quantity) * float(item_price)
    
    return render_template('invoice.html', customer_name=customer_name, item_name=item_name,
                           item_quantity=item_quantity, item_price=item_price, total_amount=total_amount)

if __name__ == '__main__':
    app.run(debug=True)
