# racket_copilot.py 
# version:      1.0
# author:       Nikolai Jenki
# date:         14.11.2023
# copyright:    CC BY-NC 4.0
# usage:        see the HELP string

HELP = """Willkommen zu dem Programm, dass Ihnen hoffentlich mehrere Stunden Lebenszeit sparen wird.

Kopieren Sie in dieses Fenster den Kommentar Ihrer Racket Funktion, in dem Sie die Beispiele beschreiben.
Dann drücken Sie auf ENTER (im Zweifel mehrfach), und das Programm gibt Ihnen den vollständigen Racket-Code aus, der diese Beispiele testet.

Das erwartete Eingabeformat ist wie folgt:
;; Beispiele:
;; (pow 2.5 3)  sollte 15.625  ergeben. ;; Format fuer numerische Tests
;; (perimeter (make-square (make-posn 2 3) 4))  sollte 16 ergeben ;; Format fuer Tests mit structs als Eingabe
;; (scale (make-square (make-posn 2 3) 4) 2)  sollte (make-square (make-posn -2 -1) 8) ergeben ;; Format fuer Tests mit structs als Ausgabe
;; (sqrt -2) sollte einen Fehler "sqrt: negative Eingabe" ergeben ;; Format fuer Tests mit Fehlermeldungen
;; (sqrt 2) sollte 1.41 ergeben (+- 0.01) ;; Format fuer naeherungsweises pruefen (check-within)
;; Ein Kommentar darf auch Zeilen enthalten, die keinen Test beschreiben. Diese werden ignoriert.
;; Beispiele duerfen nicht ueber mehrere Zeilen gehen. Jedes Beispiel muss in einer eigenen Zeile stehen. 
"""

REGEX_FUNCTION_CALL_TO_TEST = r'(\(.*\))[ \t\n]*sollte'
REGEX_EXPECTED_RESULT = r'sollte[ \t\n]*(.*?)[ \t\n]*ergeben'
REGEX_EXPECTED_ERR_MSG = r'einen Fehler[ \t\n]*("[^"]*")'
REGEX_CHECK_WITHIN_ERROR_MARGIN = r'ergeben[ \t\n]*\(\+\-[ \t\n]*([0-9\.]*)\)'

from re import search # re version 2.2.1
try: # copy2clipboard is used as an add-on
    from pyperclip import copy as copy2clipboard # pyperclip version 1.8.2
    COPY2CLIPBOARD_AVAILABLE = True
except ModuleNotFoundError:
    COPY2CLIPBOARD_AVAILABLE = False

def process_single_line(line: str) -> str:
    """Given a single line of comment, 
    return the racket code that implements the example described in that line.
    If the line contains no example input, return the original line."""

    # remove leading and trailing whitespaces
    line = line.strip()
    
    # skip empty lines
    if not line: return ''
    
    # skip uncommented lines
    if not line.startswith(';'):
        return f';; Achtung: Die Eingabe enthielt an dieser Stelle eine Zeile, \
            die kein Kommentar war, naemlich: "{line}"'
    
    # replace header line ";; Beispiele:" with ";; Tests:"
    if line[line.rfind(';')+1:].strip() == "Beispiele:":
        return ";; Tests:"

    # extract the function call to be tested
    function_call_to_test = search(REGEX_FUNCTION_CALL_TO_TEST, line)
    if not function_call_to_test: return line # skip lines that do not include a function call
    function_call_to_test = function_call_to_test.group(1)

    # extract the expected test result
    expected_result = search(REGEX_EXPECTED_RESULT, line)
    if not expected_result: # a function call to be tested without an expected test result is probably a mistake in the input
        return f';; Achtung: Die Eingabe enthielt an dieser Stelle eine Zeile, \
            in der kein Testergebnis identifiziert werden konnte, naemlich: "{line}"'
    expected_result = expected_result.group(1)

    # check if the line contains an error margin indication (if so, check-within should be used)
    check_within_error_margin = search(REGEX_CHECK_WITHIN_ERROR_MARGIN, line)

    # generate racket code
    if check_within_error_margin:
        # generate check-within code
        check_within_error_margin = check_within_error_margin.group(1).strip()
        if not check_within_error_margin: # the +- notation without a valid error bound is probably a mistake in the input
            return f';; Achtung: Die Eingabe enthielt an dieser Stelle eine Zeile, \
                in der keine gueltige Fehlerschranke fuer check-within identifiziert werden konnte, \
                    naemlich: "{line}"'
        corresponding_racket_code = f'(check-within {function_call_to_test} \
            {expected_result} {check_within_error_margin})'
    elif expected_result.startswith("einen Fehler"):
        # generate check-error code
        expected_error_msg = search(REGEX_EXPECTED_ERR_MSG, expected_result)
        if not expected_error_msg:
            return f';; Achtung: Die Eingabe enthielt an dieser Stelle eine Zeile, \
                in der keine erwartete Fehlermeldung identifiziert werden konnte, naemlich: "{line}"'
        expected_error_msg = expected_error_msg.group(1)
        corresponding_racket_code = f'(check-error {function_call_to_test} {expected_error_msg})'
    else:
        # generate check-expect code
        corresponding_racket_code = f'(check-expect {function_call_to_test} {expected_result})'
    return corresponding_racket_code

def generate_racket_code_from_comment(comment_explaining_examples):
    """Given a multiline comment explaining one example per line,
    generate the racket code testing all those examples
    
    by processing the input line by line"""
    
    input_lines = comment_explaining_examples.split('\n')
    output_racket_code = ""
    for single_line_comment in input_lines:
        output_racket_code += process_single_line(single_line_comment) + '\n'
    return output_racket_code

def read_multiline_input(end_marker = ''):
    """read multiline input from the console
    
    until an input line is equal to end_marker
    (by default, this is the empty line)."""
    multiline_input = ""
    while True:
        line = input()
        if line == end_marker: break
        multiline_input += line + '\n'
    return multiline_input

def main():
    """read a multiline comment explaining one example per line,
    then generate and print the racket code testing those examples.
    
    if access to the clipboard is available, the output is copied 
    to the clipboard."""
    print(HELP)
    while True:
        
        # read the comment explaining the examples as input
        print("Eingabe (Kommentar, der die Beispiele beschreibt):")
        comment_explaining_examples = read_multiline_input()

        # generate racket code from the comments
        racket_code = generate_racket_code_from_comment(
            comment_explaining_examples
        )

        # print the racket code as output
        print("Ausgabe (Racket code, der diese Beispiele testet):")
        print(racket_code)

        # if possible, copy the output to the clipboard
        if COPY2CLIPBOARD_AVAILABLE:
            copy2clipboard(racket_code)
            print("(Die Ausgabe wurde in Ihre Zwischenablage kopiert.)")
        print('\n'*5)

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: pass

    # If an error is encountered during the execution of the program,
    # log it to the console and safely terminate the program.
    except Exception as excp:
        print('\n' * 10 + ('#'*80+'\n')*2 + 
              "Bei der Ausfuehrung des Programms ist leider ein Fehler aufgetreten.\n" + 
              "Druecken Sie ENTER um das Programm zu schliessen und starten Sie es dann erneut.\n" + 
              ('#'*80+'\n')*2 + '\n'*6 +
              "Debugging Information: Der folgende Fehler ist aufgetreten:\n" +
              str(excp))
        
        # try to log the exception traceback to the console
        try:
            from traceback import print_exc
            from sys import stdout
            traceback_available = True
        except: traceback_available = False
        if traceback_available:
            print_exc(file = stdout)
        