from flask import flash, redirect, render_template, request, url_for
from FranTrek import app  # Assuming FranTrek is your package/module and app is initialized in __init__.py

# Route for About page
@app.route('/about', methods=['GET', 'POST'])
def about_form():
    if request.method == 'POST':
        about_info = request.form.get('about-info')
        # Handle the submitted form data (save it, process it, etc.)
        flash('Form submitted successfully!', 'success')
        return redirect(url_for('about'))
    return render_template('about.html')  # Display the About page with the form when method is GET

# Route for Tarek's page
@app.route('/tarek')
def tarek_page():
    return render_template('tarek.html')

# Route for Francia's page
@app.route('/francia')
def francia_page():
    return render_template('francia.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, port=4001)
