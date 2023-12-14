import pandas as pd
from flask import render_template
from project import prime_selector
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os


def primes_to_dataframe(min_limit, max_limit):
    """
    Generate a DataFrame with prime numbers in the given range.

    :param min_limit: Minimum limit
    :type min_limit: int
    :param max_limit: Maximum limit
    :type max_limit: int
    :return: DataFrame with prime numbers
    :rtype: pandas.DataFrame
    """
    primes = prime_selector(min_limit, max_limit)
    data = {"No": range(1, len(primes) + 1), "Prime Number": primes}
    df = pd.DataFrame(data)
    return df[["No", "Prime Number"]]


def generate_html(dataframe: pd.DataFrame):
    table_html = dataframe.to_html(
        classes="table table-striped", table_id="table", index=False
    )
    html = f"""
    <html>
    <head>
        <!-- Add Bootstrap CSS link here -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
        <!-- Add DataTables CSS link here -->
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css">
        <style>
            #table thead th {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <div class="container mt-3">
            <h1>Generated Prime Numbers</h1>
            {table_html}
        </div>
        <!-- Add jQuery and DataTables JS scripts here -->
        <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js"
                integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
        <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
        <script>
            $(document).ready( function () {{
                $('#table').DataTable();
            }});
        </script>
    </body>
    </html>
    """
    return html


def distribution(min, max):
    with plt.ion():
        prime_numbers = prime_selector(min, max)

        # Visualize prime numbers using a bar chart
        plt.bar(range(1, len(prime_numbers) + 1), prime_numbers, color="blue")
        plt.xlabel("Index")
        plt.ylabel("Prime Numbers")
        plt.title(f"Prime Numbers from {min} up to {max}")
        plt.show()

    # Save the plot
    plot_path = os.path.join("static", "images", "distr.png")
    plt.savefig(plot_path)

    # Close the plot to release resources
    plt.close()
    return plot_path


def distr_his(min, max):
    with plt.ion():
        prime_numbers = prime_selector(min, max)

        # Visualize the distribution of prime numbers using a histogram
        plt.hist(prime_numbers, bins=20, color="blue", edgecolor="black")
        plt.xlabel("Prime Numbers")
        plt.ylabel("Frequency")
        plt.title(f"Distribution of Prime Numbers from {min} up to {max}")
        plt.show()

    plot_path2 = os.path.join("static", "images", "histo.png")
    plt.savefig(plot_path2)

    # Close the plot to release resources
    plt.close()
    return plot_path2


def patern(min, max):
    with plt.ion():
        prime_numbers = prime_selector(min, max)

        # Visualize the pattern of prime numbers using a scatter plot
        plt.scatter(
            range(1, len(prime_numbers) + 1), prime_numbers, color="red", marker="."
        )
        plt.xlabel("Index")
        plt.ylabel("Prime Numbers")
        plt.title(f"Pattern of Prime Numbers from {min} up to {max}")
        plt.show()

    plot_path3 = os.path.join("static", "images", "patrn.png")
    plt.savefig(plot_path3)

    # Close the plot to release resources
    plt.close()
    return plot_path3


def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code
