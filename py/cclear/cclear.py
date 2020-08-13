'''Clear golang comments.'''
import os
from glob import glob


def cclear():
    if not os.path.isdir('cc'):
        os.mkdir('cc')
    for old in glob('*.go'):
        clear_comments(old, 'cc/'+old)


def clear_comments(old: str, new: str):
    old_fp = open(old, 'r', encoding='utf-8')
    new_fp = open(new, 'w', encoding='utf-8')
    while (l := old_fp.readline()):
        if l.lstrip().startswith('//'):
            continue
        if '//' in l:
            new_fp.write(l[:l.index('//')])
            continue
        new_fp.write(l)
    old_fp.close()
    new_fp.close()
