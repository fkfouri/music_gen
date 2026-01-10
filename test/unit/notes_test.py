from src.sound_library import get_note, tab_to_notes


def test_notes(PIANO):
    """Testa a execução de uma sequência de notas"""
    # Arrange - define as notas a tocar
    # Act
    a = get_note("C", 4)
    b = get_note("E", 4)
    c = get_note("G", 4)
    d = get_note("C#4")
    e = get_note("Ab4")
    f = get_note("E5")
    g = get_note("A")
    h = get_note("A#")
    i = get_note("EB")
    j = get_note("Fb", 3)  # Testa F natural como E#

    notes = [a, b, c, d, e, f, g, h, i, j]
    for note in notes:
        PIANO.play_note(note, 0.5, 0.25)

    # Assert
    assert a == 60 and b == 64 and c == 67
    assert d == 61 and e == 68 and f == 76
    assert g == 69 and h == 70 and i == 63 and j == 52


def test_tab(PIANO):
    """Testa a conversão de tablatura para notas MIDI"""
    tab_parte_a = """E|-------------0--------------------------|
# B|---------0------0-----------------------|
# G|-----0--------------0-------------------|
# D|----------------------------------------|
# A|----------------------------------------|
# E|-0--------------------------------------|"""
    parte_a = tab_to_notes(tab_parte_a)

    parte_b = tab_to_notes(
        """ 
E|----------0------7--7---------7p0-------|
B|-------0-----0---------0------0----0----|
G|----0---------------------0---0-------0-|
D|----------------------------------------|
A|----------------------------------------|
E|--0-----------------0-------------------|
"""
    )

    music = parte_a + parte_b
    expected_notes_parte_a = [[40], [55], [59], [64], [59], [55]]
    expected_notes_parte_b = [[40], [55], [59], [64], [59], [71], [71, 40], [59], [55], [71, 59, 55], [64], [59], [55]]

    for i,pitch in enumerate(music):
        if isinstance(pitch, list):
            PIANO.play_chord(pitch, 0.5, 0.5)
        else:
            PIANO.play_note(pitch, 0.5, 0.25)

    assert parte_a == expected_notes_parte_a
    assert parte_b == expected_notes_parte_b
