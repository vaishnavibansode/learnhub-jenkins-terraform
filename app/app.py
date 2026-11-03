from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LearnHub | Online Learning Platform</title>
        <style>
            body { margin: 0; font-family: Arial, sans-serif; color: #1f2937; background: #f4f7fb; }
            header { background: #173b6c; color: white; padding: 24px 8%; }
            header h1 { margin: 0 0 8px; }
            main { max-width: 1000px; margin: 32px auto; padding: 0 20px; }
            .intro { background: white; padding: 28px; border-radius: 12px; box-shadow: 0 2px 10px #00000010; }
            .courses { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 20px; }
            .course { background: white; padding: 22px; border-radius: 12px; border-top: 4px solid #3478c7; }
            .course h3 { margin-top: 0; color: #173b6c; }
            .status { display: inline-block; background: #e4f7eb; color: #17643a; padding: 8px 12px; border-radius: 20px; }
            footer { text-align: center; padding: 24px; color: #64748b; }
            a { color: #205ca5; }
        </style>
    </head>
    <body>
        <header>
            <h1>LearnHub</h1>
            <div>Online Learning Platform — Learn Anywhere, Anytime</div>
        </header>
        <main>
            <section class="intro">
                <h2>Welcome to LearnHub</h2>
                <p>Explore learning paths designed to build practical skills in technology and data.</p>
                <p><span class="status">Platform status: Running on AWS EC2</span></p>
                <p>Deployment managed with Ansible configuration management.</p>
                <a href="/health">View platform health status</a>
            </section>
            <section class="courses">
                <article class="course">
                    <h3>Python Programming</h3>
                    <p>Learn core Python concepts, functions, and practical problem solving.</p>
                    <strong>Level:</strong> Beginner
                </article>
                <article class="course">
                    <h3>Data Analytics</h3>
                    <p>Explore data preparation, analysis, and visualization fundamentals.</p>
                    <strong>Level:</strong> Intermediate
                </article>
                <article class="course">
                    <h3>Machine Learning</h3>
                    <p>Understand model training, evaluation, and introductory ML workflows.</p>
                    <strong>Level:</strong> Intermediate
                </article>
            </section>
        </main>
        <footer>LearnHub demo application | Flask + Ansible + AWS EC2</footer>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "application": "LearnHub Online Learning Platform",
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

