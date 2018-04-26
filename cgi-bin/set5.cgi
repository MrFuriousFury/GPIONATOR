#!/bin/bash

gpio -p write 205 1

echo "Status: 204 No Content"
echo "Content-type: text/plain"
echo ""