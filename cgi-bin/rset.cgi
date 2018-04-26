#!/bin/bash

gpio -p write 200 0
gpio -p write 201 0
gpio -p write 202 0
gpio -p write 203 0
gpio -p write 204 0
gpio -p write 205 0
gpio -p write 206 0
gpio -p write 207 0

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""