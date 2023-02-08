#!/usr/bin/env bash
python3.9 -c "print(__import__(\"$1\").__doc__)" | wc -l
