def parse_note(note_str):
    """
    Parse a note string like 'C#4', 'Db3', 'E5' into nota and oitava.

    Parameters
    ----------
    note_str : str
        The note string (e.g. 'C#4', 'Db3', 'E5')

    Returns
    -------
    tuple
        (nota_completa, oitava) where nota_completa is like 'C#', 'Db', 'E'

    """
    note_str = note_str.strip()

    # Extrai a oitava (último caractere)
    oitava = int(note_str[-1])

    # Extrai a nota e o modificador
    nota_parte = note_str[:-1]  # Tudo menos o último caractere

    # Separa nota (1ª letra) do modificador (#, b)
    nota_letra = nota_parte[0].upper()
    modificador = nota_parte[1:].lower() if len(nota_parte) > 1 else ""

    nota_completa = f"{nota_letra}{modificador}"

    return nota_completa, oitava


def get_note(nota, oitava=4):
    """
    Convert a note name and octave into a MIDI note number.

    Parameters
    ----------
    nota : str
        The note name (e.g. C, C#, D, ...) or full notation like 'C#4', 'Db3'
    oitava : int
        The octave number (optional if nota includes octave)

    Returns
    -------
    int
        The MIDI note number

    """
    # Se nota contém número no final, faz parse automático
    if nota and nota[-1].isdigit():
        nota, oitava = parse_note(nota)
    else:
        nota, oitava = parse_note(f"{nota}{oitava}")

    notas = { # fmt: skip
        "C":    0,     "B#": 0,
        "C#":   1,     "Db": 1,
        "D":    2,
        "D#":   3,     "Eb": 3,
        "E":    4,     "Fb": 4,
        "F":    5,     "E#": 5,
        "F#":   6,     "Gb": 6,
        "G":    7,
        "G#":   8,     "Ab": 8,
        "A":    9,
        "A#":  10,     "Bb": 10,
        "B":   11,     "Cb": 11
    } # fmt: skip

    return 12 + (oitava * 12) + notas[nota]


def pitch_to_note(pitch):
    """
    Convert a MIDI pitch number to note name with octave.

    Parameters
    ----------
    pitch : int
        MIDI pitch number (0-127)

    Returns
    -------
    str
        Note name (e.g. 'C4', 'A#4', 'Db3')

    Example
    -------
    pitch_to_note(60)  # Returns 'C4'
    pitch_to_note(70)  # Returns 'A#4'
    pitch_to_note(67)  # Returns 'G4'
    """
    notas_nomes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    oitava = (pitch // 12) - 1
    nota_idx = pitch % 12
    nota_nome = notas_nomes[nota_idx]

    return f"{nota_nome}{oitava}"


def pitches_to_notes(pitches):
    """
    Convert a list of MIDI pitch numbers to note names.
    Handles both flat lists and nested lists (for chords).

    Parameters
    ----------
    pitches : list
        List of MIDI pitch numbers or list of lists of pitches

    Returns
    -------
    list
        List of note names or list of lists of note names

    Example
    -------
    pitches_to_notes([60, 70, 67])
    # Returns ['C4', 'A#4', 'G4']

    pitches_to_notes([[40], [55], [71, 40]])
    # Returns [['E2'], ['G#3'], ['B4', 'E2']]
    """
    # Se o primeiro elemento é uma lista (lista aninhada)
    if pitches and isinstance(pitches[0], list):
        return [[pitch_to_note(p) for p in chord] for chord in pitches]
    else:
        # Lista simples de pitches
        return [pitch_to_note(pitch) for pitch in pitches]


def tab_to_notes(tab_str):
    """
    Convert a guitar tablature to MIDI note numbers.

    Parameters
    ----------
    tab_str : str
        The tablature string (6 lines for standard guitar tuning)

    Returns
    -------
    list
        List of lists containing MIDI note numbers (chords at each time step)

    Example
    -------
    tab = '''E|---0---
    B|---1---
    G|---0---
    D|---2---
    A|---3---
    E|-0-----'''
    notes = tab_to_notes(tab)
    """
    # Notas base de cada corda (standard tuning)
    cordas_notas_base = {
        "E4": "E4",  # Corda 1 (agudo)
        "B3": "B3",  # Corda 2
        "G3": "G3",  # Corda 3
        "D3": "D3",  # Corda 4
        "A2": "A2",  # Corda 5
        "E2": "E2",  # Corda 6
    }

    cordas_ordem = ["E4", "B3", "G3", "D3", "A2", "E2"]  # De cima para baixo no tab

    lines = tab_str.strip().split("\n")

    # Parse das linhas do tab
    tab_lines = {}
    for i, line in enumerate(lines):
        if "|" not in line:
            continue
        parts = line.split("|")
        # corda = parts[0].strip()
        corda_idx = i  # Índice da corda na ordem
        corda = cordas_ordem[corda_idx]

        conteudo = parts[1] if len(parts) > 1 else ""
        tab_lines[corda] = conteudo

    # Determinar número de colunas
    num_colunas = max(len(conteudo) for conteudo in tab_lines.values()) if tab_lines else 0

    notas = []

    # Para cada coluna (momento no tempo)
    for col in range(num_colunas):
        notas_momento = []

        # Para cada corda
        for corda in cordas_ordem:
            if corda not in tab_lines:
                continue

            conteudo = tab_lines[corda]

            if col < len(conteudo):
                char = conteudo[col]

                if char == "p":
                    x = 1

                # Se é um número, pega o traste
                if char.isdigit():
                    traste = int(char)
                    nota_base = cordas_notas_base.get(corda, "C4")
                    midi_note = get_note(nota_base) + traste
                    notas_momento.append(midi_note)

        # Adiciona notas encontradas neste momento
        if notas_momento:
            notas.append(notas_momento)

    return notas
