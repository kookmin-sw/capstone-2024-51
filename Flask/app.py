from flask import Flask, render_template, request, redirect

app = Flask(__name__)

products = {
    "1": {
        "name": "갤럭시 S20",
        "description": "첨단 기술 스마트폰",
        "image": "s20.jpg",
        "suppliers": [
            {"name": "공급처 A", "price": 1000000, "link": "https://example.com/s20/a"},
            {"name": "공급처 B", "price": 950000, "link": "https://example.com/s20/b"}
        ]
    },
    "2": {
        "name": "갤럭시 Note 20",
        "description": "최고의 작업용 스마트폰",
        "image": "note20.jpg",
        "suppliers": [
            {"name": "공급처 C", "price": 1200000, "link": "https://example.com/note20/c"},
            {"name": "공급처 D", "price": 1150000, "link": "https://example.com/note20/d"}
        ]
    }
}

@app.route('/')
def index():
    return render_template('search.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    sort_order = request.args.get('sort', 'asc')
    if not query:
        return render_template('results.html', results=[], query=query)

    filtered_products = [prod for prod in products.values() if query.lower() in prod['name'].lower()]
    if sort_order == 'desc':
        sorted_products = sorted(filtered_products, key=lambda x: x['suppliers'][0]['price'], reverse=True)
    else:
        sorted_products = sorted(filtered_products, key=lambda x: x['suppliers'][0]['price'])

    return render_template('results.html', results=sorted_products, query=query)

@app.route('/product/<product_id>')
def product_detail(product_id):
    print("Requested product_id:", product_id)  # 요청된 product_id 로깅
    product = products.get(product_id)
    if not product:
        return 'Product not found', 404
    return render_template('product_detail.html', product=product)


@app.route('/redirect_to_supplier/<path:url>')
def redirect_to_supplier(url):
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
