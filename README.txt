Malwareswaldo: C.J. May, Nick Sanford

New to Project 7:
    - Fixed various issues with code generator. Now implements everything
        except for those noted below.
    - Created test programs to test features of the flair language.

Known Bugs:
    - Status stack pointer implementation is hard-coded in each function that is
        generated because it is handled by Python instead of TM.

Features Not Implemented:
    - Compiler doesn't track which line of code an error occurred on.
    - Can't pass a function call as an argument to another function call.

Optimizations:
    - Scanner: We combined multiple states when possibly reading a word reserved
        by the flair language. We did this by keeping a list of remaining
        letters and popping off letters from that list as they were read. This
        reduces the number of if/elif checks and the length of the overall
        scanner file.
    - Analyzer: The analyze function for the AST nodes annotates node types and
        builds the symbol table simultaneously. This way the AST only needs to be
        traversed once for analysis, and each node is only visited once (except
        for function nodes while building the initial symbol table).

How To Run:
    To test the scanner, use one of these three ways:
        - call flairs from the command line, passing in an argument for a flair
            program (ex. $ flairs /path/to/program.flr )
        - call scantest.py from from the command line, passing in an argument
            for a flair program (ex. $ scantest.py /path/to/program.flr )
        - call scantest.py with python3 from the command line, passing in an
            argument for a flair program
            (ex. python3 scantest.py /path/to/program.flr )

    To test the validity of a program with the parser, use one of these three ways:
        - call flairf from the command line, passing in an argument for a flair
            program (ex. $ flairf /path/to/program.flr )
        - call parsetest.py from from the command line, passing in an argument
            for a flair program (ex. $ parsetest.py /path/to/program.flr )
        - call parsetest.py with python3 from the command line, passing in an
            argument for a flair program
            (ex. python3 parsetest.py /path/to/program.flr )

    To test the AST of a program with the parser, use one of these three ways:
        - call flairp from the command line, passing in an argument for a flair
            program (ex. $ flairp /path/to/program.flr )
        - call parsetest_ast.py from from the command line, passing in an argument
            for a flair program (ex. $ parsetest_ast.py /path/to/program.flr )
        - call parsetest_ast.py with python3 from the command line, passing in an
            argument for a flair program
            (ex. python3 parsetest_ast.py /path/to/program.flr )

    To do semantic analysis on a program with the analyzer, use one of these three ways:
        - call flairv from the command line, passing in an argument for a flair
            program (ex. $ flairv /path/to/program.flr )
        - call analyzertest.py from from the command line, passing in an argument
            for a flair program (ex. $ analyzertest.py /path/to/program.flr )
        - call analyzertest.py with python3 from the command line, passing in an
            argument for a flair program
            (ex. python3 analyzertest.py /path/to/program.flr )

    To compile a program with the generator, use one of these three ways:
        - call flairc from the command line, passing in an argument for a flair
            program (ex. $ flairc /path/to/program.flr )
        - call generatortest.py from from the command line, passing in an argument
            for a flair program (ex. $ generatortest.py /path/to/program.flr )
        - call generatortest.py with python3 from the command line, passing in an
            argument for a flair program
            (ex. python3 generatortest.py /path/to/program.flr )
