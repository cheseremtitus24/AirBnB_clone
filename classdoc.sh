#!/usr/bin/env bash
python3.9 -c "print(__import__(\"$1\").$2.__doc__)"
