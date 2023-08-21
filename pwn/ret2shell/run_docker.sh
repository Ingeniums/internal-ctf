#!/bin/bash

docker run -d -p 1338:1338 --privileged $(docker build -q .)
