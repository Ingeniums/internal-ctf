#!/bin/bash

docker run -d -p 1340:1340 --privileged $(docker build -q .)
