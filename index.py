import webbrowser

def generate_html():
html_code = """
<!DOCTYPE html>
<html>
<head>
<title>My Python HTML Page</title>
</head>
<body>
<h1>Hello, World!</h1>
</body>
</html>
"""
return html_code

def open_html_in_browser():
html_code = generate_html()
with open('index.html', 'w') as file:
file.write(html_code)
webbrowser.open('index.html')

if __name__ == '__main__':
open_html_in_browser()
