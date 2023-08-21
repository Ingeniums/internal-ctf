#!/bin/bash

docker run -d -p 1336:1336 --privileged $(docker build -q .)
