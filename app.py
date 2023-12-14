from flask import Flask, render_template, send_from_directory, request
from helper import (
    primes_to_dataframe,
    generate_html,
    apology,
    distribution,
    distr_his,
    patern,
)
from project import is_prime, sum_primes
import os


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)


@app.route("/generate", methods=["GET", "POST"])
def generate():
    if request.method == "POST":
        min_limit = int(request.form.get("min", 0))
        max_limit = int(request.form.get("max", 0))
        if min_limit < 1 or max_limit < min_limit:
            return apology(
                "Must positive number greather than 1 or Min Limit less than Max Limit"
            )

        df = primes_to_dataframe(min_limit, max_limit)
        html = generate_html(df)

        # Call the distribution function and get the plot path
        plot_path = distribution(min_limit, max_limit)
        plot_path2 = distr_his(min_limit, max_limit)
        plot_path3 = patern(min_limit, max_limit)

        return render_template(
            "prime_rslt.html",
            min_limit=min_limit,
            max_limit=max_limit,
            table_html=html,
            plot_path=plot_path,
            plot_path2=plot_path2,
            plot_path3=plot_path3,
        )

    return render_template("generate.html")


@app.route("/check", methods=["GET", "POST"])
def check():
    if request.method == 'POST':
        num = int(request.form.get("check"))
        if num < 1:
            return apology("Must positive number greather than 1")

        status = is_prime(num)
        return render_template("check_rslt.html", num=num, status=status)

    return render_template("check.html")


@app.route("/sum", methods=["GET", "POST"])
def sum():
    if request.method == 'POST':
        min_limit = int(request.form.get("min", 0))
        max_limit = int(request.form.get("max", 0))
        if min_limit < 1 or max_limit < min_limit:
            return apology(
                "Must positive number greather than 1 or Min Limit less than Max Limit"
            )

        total = sum_primes(min_limit, max_limit)
        return render_template(
            "sum_rslt.html", min_limit=min_limit, max_limit=max_limit, total=total
        )

    return render_template("sum.html")


if __name__ == "__main__":
    app.run(debug=True)
