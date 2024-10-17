from flask import redirect, render_template, request, url_for
from FranTrek import app

if __name__ == "__main__":
    app.run(debug=True,port=4001)


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        info = request.form.get('about-info')
        # Traite les informations reçues
        print(info)  # Ici, tu peux faire ce que tu veux avec les données
        return redirect(url_for('about'))
    return render_template('about.html')
