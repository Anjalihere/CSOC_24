from flask import Flask, render_template, request, redirect, url_for, make_response


app = Flask(__name__)


@app.route('/')
def intro():
    return render_template('index.html')


# Serve the index.html file
@app.route('/reconnaissance')
def reconnaissance():
    return render_template('reconnaissance.html')


# Handle path traversal challenge and template rendering
@app.route('/reconnaissance/<path:path>', methods=['GET'])
def navigate(path):
    # Validate the path and serve appropriate content or response
    if path == 'secret_login':
        return render_template('secret_login.html')
    else:
        return 'Path not found. Keep searching for clues!', 404


# Handle login form submission
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    # Simulate login logic
    if email == 'b0ss@moebius.com' or (username == 'Hui Chan' and password == 'Assemblyman'):
        return redirect(url_for('database'))
    else:
        return render_template('secret_login.html', error='Invalid credentials. Please try again.')



workers = [
    {"name": "Kim Jong-suk", "address": "70-5, Yanggeun ri 7, Yangpyeong-eup, Gyeonggi-do", "level": "Pro", "skills": "Fighting, Karate", "crimes": "Theft, Assault"},
    {"name": "Park Ji-hoon", "address": "122-1, Dunsan-dong, Daejeon", "level": "Midway", "skills": "Boxing, Stealth", "crimes": "Burglary, Illegal Hacking"},
    {"name": "Choi Eun-ha", "address": "68-8, Injeuidae, Gaegeum 2(i)-dong, Jin-gu, Busan", "level": "Rookie", "skills": "Agility, Lockpicking", "crimes": "Fraud, Forgery"},
    {"name": "Lee Min-woo", "address": "260-1, Songjeongri, Jeondong-myeon, Chungcheongnam-do", "level": "Pro", "skills": "Martial Arts, Weaponry", "crimes": "Murder, Kidnapping"},
    {"name": "Kang Soo-jin", "address": "307-1, Geunhwabeullubirapateu, Seokhyeon-dong, Jeollanam-do", "level": "Midway", "skills": "Survival Skills, Tracking", "crimes": "Drug Trafficking, Extortion"},
    {"name": "Ma Dae-Young", "address": "105-10, Hanguk 1 chaapateu, Maetan 2(i)-dong, Gyeonggi-do", "level": "Pro", "skills": "Martial Arts, Sniper", "crimes": "Murdered Park Deong Cheol"}
]

@app.route('/database')
def database():
    return render_template('database.html')

@app.route('/search')
def search():
    query = request.args.get('query', '')
    results = []

    if 'murder' in query.lower() or 'murder' in query.upper():
        results.extend([
            {"name": "Lee Min-woo", "address": "260-1, Songjeongri, Jeondong-myeon, Chungcheongnam-do", "level": "Pro",
             "skills": "Martial Arts, Weaponry", "crimes": "Murder, Kidnapping"},
            {"name": "Ma Dae-Young", "address": "105-10, Hanguk 1 chaapateu, Maetan 2(i)-dong, Gyeonggi-do",
             "level": "Pro", "skills": "Martial Arts, Sniper", "crimes": "Murdered Park Deong Cheol"}
        ])
    return render_template('search.html', results=results,show_fingerprint_button='murder' in query)


@app.route('/identity', methods=['GET', 'POST'])
def identity():
    resp = make_response(render_template('identity.html'))
    resp.set_cookie('b0ss', "7MaYPFu")

    # Retrieve cookie 'admin' from the request
    boss_cookie = request.cookies.get("b0ss")

    # Check if the 'admin' cookie is set to '1nU51X' before showing 'fingerprint.html'
    if boss_cookie == '1nU51X':
        return render_template('fingerprint.html')

    return resp


if __name__ == '__main__':
    app.run(debug=True)

#
#
