Malwareswaldo: C.J. May, Nick Sanford

Known Bugs:
    -

Features Not Implemented:
    -

Optimizations:
    - Scanner: We combined multiple states when possibly reading a word reserved
        by the flair language. We did this by keeping a list of remaining
        letters and popping off letters from that list. This reduces the number
        of if/elif checks and the length of the overall scanner file.

How To Run:
    To test the scanner, execute the scantest.py file in the tests/ directory
    using one of these two ways:
        - give scantest.py execute permissions on a UNIX operating system, and
            call it from the command line, passing in an argument for a flair
            program to scan (ex. $ scantest.py /path/to/program.flr )
        - call scantest.py with python3 from the command line, passing in an
            argument for a flair program to scan
            (ex. python3 scantest.py /path/to/program.flr )
