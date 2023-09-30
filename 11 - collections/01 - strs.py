# функция извлечения текста из html-тега
# <h1>Заголовок</h1>


def extract_text_from_tags(tag, html_text):
    opener = '<{}>'.format(tag)
    closer = '</{}>'.format(tag)
    try:
        opener_index = html_text.index(opener)
        closer_index = html_text.index(closer)
    except ValueError:
        return ''
    return html_text[opener_index + len(opener):closer_index]


assert extract_text_from_tags('h1', '<h1>Заголовок</h1>') == 'Заголовок'
assert extract_text_from_tags('h2', '<h1>Заголовок</h1>') == ''
assert extract_text_from_tags('h1', '</h1>Заголовок<h1>') == ''


def extract_text_from_tags(html_text):
    try:
        opener_tag_closer_br_index = html_text.index('>')
        closer_tag_opener_br_index = html_text.index('</')
    except ValueError:
        return ''
    return html_text[opener_tag_closer_br_index + 1:closer_tag_opener_br_index]


assert extract_text_from_tags('<h1>Заголовок</h1>') == 'Заголовок'
assert extract_text_from_tags('</h1>Заголовок<h1>') == ''


def extract_text_from_tags(html_text):
    opener_tag_closer_br_index = html_text.find('>')
    closer_tag_opener_br_index = html_text.find('</')
    if opener_tag_closer_br_index == '-1' or closer_tag_opener_br_index == -1:
        return ''
    return html_text[opener_tag_closer_br_index + 1:closer_tag_opener_br_index]


assert extract_text_from_tags('<h1>Заголовок</h1>') == 'Заголовок'
assert extract_text_from_tags('</h1>Заголовок<h1>') == ''
assert extract_text_from_tags('<h1>Заголовок') == ''
