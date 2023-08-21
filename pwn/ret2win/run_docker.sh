#!/bin/bash

docker run -d -p 1337:1337 --privileged $(docker build -q .)
