#!/usr/bin/bash

git clone https://github.com/thautwarm/Typed-BNF
mv Typed-BNF/_tbnf .
rm -rf Typed-BNF

pip install lark
