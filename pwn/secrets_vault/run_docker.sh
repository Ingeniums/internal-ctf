#!/bin/bash

docker run -d -p 1335:1335 --privileged $(docker build -q .)
