from chapter_parser import chapters_from_mangarock


def test_chapters_from_mangarock():
    chapters = tuple(
        chapters_from_mangarock(url='https://mangarock.com/manga/mrs-serie-241688')
    )
    assert len(chapters) == 58
    assert 'name' in chapters[0] and chapters[0]['name'] is not None
    assert 'url' in chapters[0] and chapters[0]['url'] is not None


test_chapters_from_mangarock()
