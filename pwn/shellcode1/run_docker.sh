#!/bin/bash

docker run -d -p 1339:1339 --privileged $(docker build -q .)
