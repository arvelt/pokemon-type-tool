#!/bin/bash

export PYTHONPATH='/Users/arvelt/PycharmProjects/GAE_SDK/google_appengine':$PYTHONPATH
export PYTHONPATH='/Users/arvelt/PycharmProjects/GAE_SDK/google_appengine/lib/yaml/lib':$PYTHONPATH
py.test $1 front/tests/*
