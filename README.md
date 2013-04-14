DEATHGRIP
=========================
-------------------------


What is Deathgrip
-------------------------

Deathgrip is a Python script which is used to encrypt and decript plain text messages by converting letters to numbers and using a unique conversation salt.

Usage
-------------------------

Deathgrip is ran in either encoder (-e) or decoder (-d) mode. You must specify an input file. You can optionally specify an output file. To encode "foo.txt" you could use:

    deathgrip -e -f foo.txt

As it would by default send that output to "output.txt", you would decode the output with:

    deathgrip -e -f output.txt -o bar.txt

Since we specified an output file for the decoder, the decoded message can be seen by opening "bar.txt"
    
A complete list of command line arguments can be seen with 

	deathgrip --help
    

Authors
------------------------

Joseph Ko and Nathan Weber
