#!/bin/bash

### 安裝服務

readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

ln -fs ${SCRIPT_DIR}/joy_detection_demo.service /lib/systemd/system/weather_tts.service
systemctl daemon-reload
systemctl enable weather_tts.service

