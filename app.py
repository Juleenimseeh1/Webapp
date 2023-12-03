import os
from jinja2 import Environment, FileSystemLoader

# Define quiz questions and answers
questions = [
    {
        'question': 'What does HTML stand for?',
        'options': ['Hyper Text Markup Language', 'High Tech Machine Learning', 'Hyper Transfer Markup Language'],
        'correct_answer': 'Hyper Text Markup Language',
        'explanation': 'HTML stands for Hyper Text Markup Language. It is the standard markup language for creating web pages.'
    },
    {
        'question': 'Which programming language is known as the "language of the web"?',
        'options': ['Java', 'Python', 'JavaScript'],
        'correct_answer': 'JavaScript',
        'explanation': 'JavaScript is often referred to as the "language of the web" as it is widely used for client-side scripting in web development.'
    },
    {
        'question': 'What does CSS stand for?',
        'options': ['Counter Style Sheets', 'Computer Style Sheets', 'Cascading Style Sheets'],
        'correct_answer': 'Cascading Style Sheets',
        'explanation': 'CSS stands for Cascading Style Sheets. It is a style sheet language used for describing the look and formatting of a document written in HTML or XML.'
    },
    {
        'question': 'Which of the following is a backend programming language?',
        'options': ['HTML', 'CSS', 'Python'],
        'correct_answer': 'Python',
        'explanation': 'Python is a versatile programming language used for backend development, data analysis, artificial intelligence, and more.'
    },
    {
        'question': 'What is the purpose of the <head> tag in HTML?',
        'options': ['To define a header for a document', 'To define a section containing navigation links', 'To contain metadata about the document'],
        'correct_answer': 'To contain metadata about the document',
        'explanation': 'The <head> tag in HTML is used to define a section that contains metadata about the document, such as title, character set, styles, and more.'
    },
    {
        'question': 'Which of the following is a version control system?',
        'options': ['Python', 'Git', 'Java'],
        'correct_answer': 'Git',
        'explanation': 'Git is a distributed version control system used for tracking changes in source code during software development.'
    },
    {
        'question': 'What does API stand for?',
        'options': ['Automated Programming Interface', 'Application Programming Interface', 'Advanced Program Integration'],
        'correct_answer': 'Application Programming Interface',
        'explanation': 'API stands for Application Programming Interface. It defines a set of rules for building and interacting with software applications.'
    },
    {
        'question': 'Which company developed the Python programming language?',
        'options': ['Microsoft', 'Google', 'Dropbox'],
        'correct_answer': 'Dropbox',
        'explanation': 'Python was not developed by Dropbox. The correct answer is the Python Software Foundation.'
    },
    {
        'question': 'What is the primary function of a database management system (DBMS)?',
        'options': ['To create and manage databases', 'To design user interfaces', 'To develop mobile applications'],
        'correct_answer': 'To create and manage databases',
        'explanation': 'A Database Management System (DBMS) is software that provides an interface for interacting with databases, storing, retrieving, and managing data.'
    },
    {
        'question': 'In web development, what does the acronym URL stand for?',
        'options': ['Universal Resource Locator', 'Unified Registration Link', 'User Registration Language'],
        'correct_answer': 'Universal Resource Locator',
        'explanation': 'URL stands for Universal Resource Locator. It is a reference or address used to access resources on the internet, such as web pages.'
    },
   
]


# Set up Jinja2 environment
template_env = Environment(loader=FileSystemLoader(searchpath="./templates"))
quiz_template = template_env.get_template("quiz.html")
answer_template = template_env.get_template("answer.html")
index_template = template_env.get_template("index.html")
summary_template = template_env.get_template("summary.html")

# Create 'docs' folder if not exists
os.makedirs("docs", exist_ok=True)

# Repository name
repo_name = "Webapp"

# Generate HTML files for each question
for index, question in enumerate(questions):
    html_content = quiz_template.render(
        question=question,
        question_index=index + 1,
        next_question_url=f"question_{index + 2}.html" if index + 2 <= len(questions) else "summary.html"
    )
    with open(f"docs/question_{index + 1}.html", "w") as html_file:
        html_file.write(html_content)

# Generate HTML file for the index page
html_content = index_template.render(next_question_url="question_1.html")
with open("docs/index.html", "w") as html_file:
    html_file.write(html_content)

# Generate HTML file for the answer page
html_content = answer_template.render(question=questions[0])  # Pass a sample question for rendering
with open("docs/answer.html", "w") as html_file:
    html_file.write(html_content)



# Generate HTML file for the summary page
summary_content = summary_template.render(questions=questions)
with open("docs/summary.html", "w") as html_file:
    html_file.write(summary_content)
