\version "2.24.4"
\language "english"
\include "C:\Users\fkfouri\AppData\Local\SCAMP\scamp_lilypond_template.ly"
\header
{
    title = "On the Code Again"
    composer = "The Rubytles"
}
\score
{
    % OPEN_BRACKETS:
    \new Score
    <<
        % OPEN_BRACKETS:
        \context Staff = "piano"
        \with
        {
            instrumentName = #"piano"
        }
        {
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                % OPENING:
                    % COMMANDS:
                    \time 3/4
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    e'16
                    fs'16
                    b'16
                    cs''16
                    d''16
                    fs'16
                    e'16
                    cs''16
                    b'16
                    fs'16
                    d''16
                    cs''16
                % CLOSE_BRACKETS:
                }
                % OPEN_BRACKETS:
                \context Voice = "TempoVoice"
                {
                    % BEFORE:
                    % COMMANDS:
                    \tempo 4=100
                    s4
                    s4
                    s4
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                    e'16
                    fs'16
                    b'16
                    cs''16
                    d''16
                    fs'16
                    e'16
                    cs''16
                    b'16
                    fs'16
                    d''16
                    cs''16
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                    e'16
                    fs'16
                    b'16
                    cs''16
                    d''16
                    fs'16
                    e'16
                    cs''16
                    b'16
                    fs'16
                    d''16
                    cs''16
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                    e'16
                    fs'16
                    b'16
                    cs''16
                    d''16
                    fs'16
                    e'16
                    cs''16
                    b'16
                    fs'16
                    d''16
                    cs''16
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                    e'16
                    fs'16
                    b'16
                    cs''16
                    d''16
                    fs'16
                    e'16
                    cs''16
                    b'16
                    fs'16
                    d''16
                    cs''16
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                    e'16
                    fs'16
                    b'16
                    cs''16
                    d''16
                    fs'16
                    r8
                    r4
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
        % CLOSE_BRACKETS:
        }
        % OPEN_BRACKETS:
        \context Staff = "piano [2]"
        \with
        {
            instrumentName = #"piano [2]"
        }
        {
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                % OPENING:
                    % COMMANDS:
                    \time 3/4
                    % OPENING:
                    % COMMANDS:
                    \clef "treble"
                    e'16
                    fs'16
                    b'16
                    cs''16
                    d''16
                    fs'16
                    e'16
                    cs''16
                    b'16
                    fs'16
                    d''16
                    cs''16
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                    e'16
                    fs'16
                    b'16
                    cs''16
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    cs''64
                    d''32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    d''64
                    fs'32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    fs'64
                    e'32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    e'64
                    cs''32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    cs''64
                    b'32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    b'64
                    fs'32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    fs'64
                    d''32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    d''64
                    cs''32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                    cs''64
                    e'32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    e'64
                    fs'32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    fs'64
                    b'32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    b'64
                    cs''32.
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    % OPEN_BRACKETS:
                    \times 2/3
                    {
                        cs''32
                        d''16.
                        fs'16.
                        e'32
                        % AFTER:
                        % SPANNER_STARTS:
                        ~
                        e'16
                        cs''16
                        % AFTER:
                        % SPANNER_STARTS:
                        ~
                    % CLOSE_BRACKETS:
                    }
                    % OPEN_BRACKETS:
                    \times 2/3
                    {
                        cs''32
                        b'16.
                        fs'16.
                        d''32
                        % AFTER:
                        % SPANNER_STARTS:
                        ~
                        d''16
                        cs''16
                        % AFTER:
                        % SPANNER_STARTS:
                        ~
                    % CLOSE_BRACKETS:
                    }
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                    % OPEN_BRACKETS:
                    \times 2/3
                    {
                        cs''32
                        e'16.
                        fs'16.
                        b'32
                        % AFTER:
                        % SPANNER_STARTS:
                        ~
                        b'16
                        cs''16
                        % AFTER:
                        % SPANNER_STARTS:
                        ~
                    % CLOSE_BRACKETS:
                    }
                    cs''32
                    d''16
                    fs'32
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    fs'32
                    e'16
                    cs''32
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    cs''32
                    b'16
                    fs'32
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    fs'32
                    d''16
                    cs''32
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                    cs''32
                    e'16
                    fs'32
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    fs'32
                    b'16
                    cs''32
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    cs''32
                    d''16
                    fs'32
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    fs'32
                    e'16
                    cs''32
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    cs''32
                    b'16
                    fs'32
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                    fs'32
                    d''16
                    cs''32
                    % AFTER:
                    % SPANNER_STARTS:
                    ~
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
            % OPEN_BRACKETS:
            <<
                % OPEN_BRACKETS:
                \context Voice = "voiceOne"
                {
                    % OPEN_BRACKETS:
                    \times 2/3
                    {
                        cs''16
                        e'16
                        % AFTER:
                        % SPANNER_STARTS:
                        ~
                        e'32
                        fs'16.
                        b'16.
                        cs''32
                        % AFTER:
                        % SPANNER_STARTS:
                        ~
                    % CLOSE_BRACKETS:
                    }
                    % OPEN_BRACKETS:
                    \times 2/3
                    {
                        cs''16
                        d''16
                        % AFTER:
                        % SPANNER_STARTS:
                        ~
                        d''32
                        r8..
                    % CLOSE_BRACKETS:
                    }
                    r4
                    % AFTER:
                    % COMMANDS:
                    \bar "|."
                % CLOSE_BRACKETS:
                }
            % CLOSE_BRACKETS:
            >>
        % CLOSE_BRACKETS:
        }
    % CLOSE_BRACKETS:
    >>
}
