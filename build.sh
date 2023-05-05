#!/bin/bash
tbnf -lang esdl -be python-lark esdl.tbnf
sed -i 's/.esdl_/esdl_/g' esdl_parser.py
sed -i 's/.esdl_/esdl_/g' esdl_construct.py
