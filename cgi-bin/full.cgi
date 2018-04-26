#!/bin/bash

gpio -p write 200 1
gpio -p write 201 1
gpio -p write 202 1
gpio -p write 203 1
gpio -p write 204 1
gpio -p write 205 1
gpio -p write 206 1
gpio -p write 207 1

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""