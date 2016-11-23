#!/bin/bash

export PYTHONPATH=/src:$PYTHONPATH
py.test $1 tests/*
