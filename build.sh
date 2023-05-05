#!/bin/bash
tbnf -lang esdl -be python-lark esdl.tbnf

# don't know why @thautwarm uses a really complicated "relative" import.
# setting up that seems to need much effort, so simply do some dirty dirty sed.
sed -i 's/.esdl_/esdl_/g' esdl_parser.py
sed -i 's/.esdl_/esdl_/g' esdl_construct.py
