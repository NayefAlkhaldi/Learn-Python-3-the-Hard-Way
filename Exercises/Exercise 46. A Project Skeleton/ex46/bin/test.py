#!/usr/bin/env python
from textwrap import dedent
CodingLanguages_Comments = {

	'Python': '#',
	'Java Script': '//',
	' C ': '/*',
}

for name, comment in CodingLanguages_Comments.items():
	print(dedent(f"""
		{comment}

	{comment} {name} {comment}

		{comment}
	"""))