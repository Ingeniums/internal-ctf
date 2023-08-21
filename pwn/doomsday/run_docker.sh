#!/bin/bash

docker run -d -p 1341:1341 --privileged $(docker build -q .)
