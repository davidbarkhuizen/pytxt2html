source_file_path = '/home/mage/Downloads/c0.txt'

template = '''<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>{{title}}</title>
	</head>
	<body class='bodyStyle'>{{body}}</body>
	<style>{{style}}</style>
</html>'''

br = '<br>'

title = 'c0'

style = '''
.bodyStyle {
	background: black;
	color:	white;
	margin-left: 20%;
	margin-right: 20%;
	font-size: large;
}
'''

src_file_string = None
with open(source_file_path) as source_file:
	src_file_string = source_file.read()

src_file_string = src_file_string.replace('\r', '')

body = src_file_string.replace('\n\n', br) 
body = body.replace('\t', br + '&emsp;'*3)

html = template.replace('{{body}}', body)
html = html.replace('{{title}}', title)
html = html.replace('{{style}}', style)

dest_file_path = source_file_path + '.html'

with open(dest_file_path, 'tw') as dest_file:
	dest_file.write(html)
