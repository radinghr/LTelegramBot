#!/bin/bash
mkdir -p logs
rm twistd.pid
supervisord -c /app/config/supervisord.conf