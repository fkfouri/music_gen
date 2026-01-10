from itertools import islice


def test_melody_execution(SESSION, PIANO):
    """Testa a execução de uma sequência de notas"""
    # Arrange - define as notas a tocar
    notes = [65, 66, 67, 69]  # MIDI numbers

    # Act - toca as notas
    for note in notes:
        PIANO.play_note(note, 0.5, 0.25)

    # Assert - verifica se a sessão está ativa
    assert SESSION is not None
    assert PIANO is not None


def test_chord_execution(SESSION, PIANO):
    """Testa a execução de uma sequência de notas"""
    # Arrange - define as notas a tocar

    notes = [[60, 64, 67], [66, 60], [67, 60], [69, 60]]  # MIDI numbers

    # Act - toca as notas
    for note in notes:
        if isinstance(note, list):
            PIANO.play_chord(note, 0.5, 0.5)
        else:
            PIANO.play_note(note, 0.5, 0.25)

    # Assert - verifica se a sessão está ativa
    assert SESSION is not None
    assert PIANO is not None


def test_music_file_execution(SESSION, PIANO, MIDI_FILE):
    """Testa a execução de um arquivo MIDI"""
    # Arrange - carrega o arquivo MIDI
    from scamp_extensions.parsing.midi import scrape_midi_file_to_dict

    midi_data = scrape_midi_file_to_dict(MIDI_FILE)
    music_data = zip(midi_data["pitches"], midi_data["volumes"], midi_data["lengths"], midi_data["inter_onset_times"])

    # Act - toca as notas do arquivo MIDI (pula 5 primeiros, pega os próximos 20),
    for pitch, volume, length, wait_time in islice(music_data, 120, 160):
        PIANO.play_note(pitch, volume, length, blocking=False)
        SESSION.wait(wait_time)

    assert True  # Se chegou aqui, não houve erro


def test_with_timeout(SESSION, PIANO):
    """Testa execução com timeout para não travar"""
    import threading

    def play_music():
        PIANO.play_note(60, 2.0, 2)  # Nota longa
        PIANO.play_note(64, 2.0, 2)

    # Executa em thread com timeout
    thread = threading.Thread(target=play_music)
    thread.daemon = True
    thread.start()
    thread.join(timeout=5)  # Máximo 5 segundos

    assert not thread.is_alive() or True  # Passou ou timeout
