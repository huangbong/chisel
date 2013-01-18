#!./venv/bin/python
# Chisel
# David Zhou

import sys
import re
import time
import os
import codecs
import string

import jinja2
import markdown

# Settings
SOURCE = "./posts/" # end with slash
DESTINATION = "./www/" # end with slash
HOME_SHOW = 10 # numer of entries to show on homepage
TEMPLATE_PATH = "./templates/"
TEMPLATE_OPTIONS = {}
TEMPLATES = {
    'index': "index.html",
    'detail': "detail.html",
    'archive': "archive.html",
}
TIME_FORMAT = "%B %d, %Y"
# FORMAT should be a callable that takes in text
# and returns formatted text
FORMAT = lambda text: markdown.markdown(text, ['fenced_code']) 

STEPS = []

def slug(title):
    title = title.lower()
    for char in title:
        if char in ' ':
            title = title.replace(char, '-')
        if char not in string.lowercase + string.digits:
            title = title.replace(char, '')
    return title

def step(func):
    def wrapper(*args, **kwargs):
        print func.__name__ + "..."
        func(*args, **kwargs)
    STEPS.append(wrapper)
    return wrapper

def get_tree(source):
    files = []
    for root, ds, fs in os.walk(source):
        for name in fs:
            if name[0] == ".": continue
            path = os.path.join(root, name)
            f = open(path, "rU")
            lines = f.readlines()
            title = lines[0].strip()
            date = time.strptime("%s %s %s" % (name.split("-")[0], name.split("-")[1], name.split("-")[2]), "%Y %m %d")
            content = ''.join(lines[1:]).decode('UTF-8')
            year, month, day = date[:3]
            content_md = ''.join(lines).decode('UTF-8')
            f.close()

            files.append({
                'title': title,
                'epoch': time.mktime(date),
                'content': FORMAT(content),
                'url': '/'.join([str(year), "%.2d" % month, "%.2d" % day, slug(title) + ".html"]),
                'content_md': content_md,
                'url_md':  '/' + '/'.join([str(year), "%.2d" % month, "%.2d" % day, slug(title) + ".md"]),
                'pretty_date': time.strftime(TIME_FORMAT, date),
                'date': date,
                'year': year,
                'month': month,
                'day': day,
                'filename': name,
            })
    return files

def compare_entries(x, y):
    result = cmp(-x['epoch'], -y['epoch'])
    if result == 0:
        return -cmp(x['filename'], y['filename'])
    return result

def write_file(url, data):
    path = DESTINATION + url
    dirs = os.path.dirname(path)
    if not os.path.isdir(dirs):
        os.makedirs(dirs)
    file = open(path, "w")
    file.write(data.encode('UTF-8'))
    file.close()

@step
def generate_homepage(f, e):
    """Generate homepage"""
    template = e.get_template(TEMPLATES['index'])
    write_file("index.html", template.render(entries=f[:HOME_SHOW]))

@step
def master_archive(f, e):
    """Generate master archive list of all entries"""
    template = e.get_template(TEMPLATES['archive'])
    write_file("archive.html", template.render(entries=f))

@step
def detail_pages(f, e):
    """Generate detail pages of individual posts"""
    template = e.get_template(TEMPLATES['detail'])
    for file in f:
        write_file(file['url'], template.render(entry=file))
        print "\t\t\t%s written." % file['url']
        write_file(file['url_md'], file['content_md'])
        print "\t\t\t%s written." % file['url_md']

def main():
    print "Chiseling..."
    print "\tReading files...",
    files = sorted(get_tree(SOURCE), cmp=compare_entries)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_PATH), **TEMPLATE_OPTIONS)
    print "Done."
    print "\tRunning steps..."
    for step in STEPS:
        print "\t\t",
        step(files, env)
    print "\tDone."
    print "Done."

if __name__ == "__main__":
    sys.exit(main())
