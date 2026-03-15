import re

skills_list = [
"python","java","sql","machine learning",
"data analysis","docker","aws"
]

languages = ["english","french","arabic"]

def extract_experience(text):

    match = re.findall(r'(\d+) years', text)

    if match:
        return max([int(x) for x in match])

    return 0


def extract_skills(text):

    found = []

    for skill in skills_list:
        if skill in text:
            found.append(skill)

    return found


def extract_languages(text):

    langs=[]

    for l in languages:
        if l in text:
            langs.append(l)

    return langs
