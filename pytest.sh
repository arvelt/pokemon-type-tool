#!/bin/bash

export PYTHONPATH=/src:$PYTHONPATH
py.test tests/*
