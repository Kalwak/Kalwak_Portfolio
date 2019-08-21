import re

new_file_content = ""
with open("./frontend/templates/index.html", "r") as file:
    for line in file.readlines():
        regex = r"(href|src)=(\/|[a-zA-Z0-9]|\.|-|_)*"
        if ("href" in line or "src" in line) and "https" not in line and "<base" not in line:
            matches = re.finditer(regex, line)
            for matchNum, match in enumerate(matches, start=1):
                equals_sign_position = line.find("href=")
                padding = 5
                if equals_sign_position == -1:
                    equals_sign_position = line.find("src=")
                    padding = 4
                new_link = '{% static "' + line[equals_sign_position + padding:match.end()] + '" %}'
                new_link = new_link.replace("./", "/")

                new_tag = line[:match.start() + padding] + new_link + line[match.end():]
                new_file_content += new_tag
        else:
            new_file_content += line

with open("./frontend/templates/index.html", "w") as file:
    file.write(new_file_content)
