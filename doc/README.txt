Malwareswaldo: C.J. May, Nick Sanford

Known Bugs:

Features Not Implemented:
    - Compiler doesn't track which line of code an error occurred on.

Optimizations:
    - Scanner: We combined multiple states when possibly reading a word reserved
        by the flair language. We did this by keeping a list of remaining
        letters and popping off letters from that list as they were read. This
        reduces the number of if/elif checks and the length of the overall
        scanner file.

How To Run:
    To test the scanner, use one of these three ways:
        - call flairs from the command line, passing in an argument for a flair
            program to scan (ex. $ flairs /path/to/program.flr )
        - call scantest.py from from the command line, passing in an argument
            for a flair program to scan (ex. $ scantest.py /path/to/program.flr )
        - call scantest.py with python3 from the command line, passing in an
            argument for a flair program to scan
            (ex. python3 scantest.py /path/to/program.flr )

    To test the parser, use one of these three ways:
        - call flairf from the command line, passing in an argument for a flair
            program to scan (ex. $ flairf /path/to/program.flr )
        - call parsetest.py from from the command line, passing in an argument
            for a flair program to scan (ex. $ parsetest.py /path/to/program.flr )
        - call parsetest.py with python3 from the command line, passing in an
            argument for a flair program to scan
            (ex. python3 parsetest.py /path/to/program.flr )
