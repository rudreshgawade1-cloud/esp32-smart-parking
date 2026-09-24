# ESP32 Smart Parking: virtual prototype

An interactive 3D simulation of an **IoT smart parking system** built around an ESP32.
Cars drive in, IR sensors detect them, the ESP32 assigns a slot, the LEDs flip from green to red,
and the entrance display and a phone app update live. No hardware needed to try it.

![Overview](docs/overview.png)

## Features

- 3D parking lot with 8 slots, IR slot sensors and green/red LEDs, entry and exit barriers
- Control station at the entrance: ESP32, 20x4 LCD, OLED slot map, breadboard, servos, wires
- Full flow: sensor -> ESP32 -> slot assigned -> barrier -> car reverses in -> sensor confirms -> LED red -> display updates. Exit reverses it.
- **Drag & drop** cars into slots, double-click a car to send it out
- **Phone app** widget: alerts, your slot, *Find my car*, *Exit now*, hold a slot, trip log
- **Tap the control station** to zoom in, **tap the ESP32** to open the full firmware code
- Live status panel, serial monitor, flow strip, day / night mode, white theme
- Real Arduino firmware in [`firmware/smart_parking`](firmware/smart_parking/smart_parking.ino)

![Code window](docs/code-window.png)

## Run it on localhost

**Windows:** double-click **`start.bat`**. It starts a small local server and opens your browser.

**macOS / Linux:** `./start.sh`

Any other way: `python serve.py` (or `python -m http.server` inside the `web` folder) and open http://localhost:8000.

You need [Python 3](https://www.python.org/downloads/) (tick *Add python.exe to PATH* on Windows).
The page has to be served over `http://` because the browser blocks loading the 3D models from `file://`.

## Controls

| Action | How |
|---|---|
| Car enters / exits | **Car enters** / **Car exits** buttons |
| Park a car yourself | **Drag a car in**, then drag it onto a blue (free) slot |
| Move a parked car | Drag it to another free slot |
| Send a car out | Double-click it, or the **Exit** button in the table |
| Zoom to the electronics | Tap the control station; tap the ESP32 for the code |
| Phone | Tap the small phone (top right) |
| Camera | Drag to orbit, scroll to zoom, presets at the bottom |

## Project structure

```
esp32-smart-parking/
|-- start.bat            Windows launcher (localhost)
|-- start.sh             macOS / Linux launcher
|-- serve.py             tiny static web server (standard library only)
|-- firmware/
|   `-- smart_parking/
|       `-- smart_parking.ino   ESP32 Arduino sketch
|-- web/
|   |-- index.html
|   |-- css/style.css
|   |-- js/
|   |   |-- scene.js         renderer, lights, model loading, slots, gates, cables
|   |   |-- station.js       3D control station, LCD and OLED drawing
|   |   |-- simulation.js    paths, cars, sensors, ESP32 logic (entry / exit tasks)
|   |   |-- interaction.js   phone app, drag & drop
|   |   `-- ui.js            panels, firmware listing, cameras, main loop
|   |-- libs/                three.js r128 and helpers
|   `-- models/              parking lot and car models (.glb)
`-- docs/                    screenshots
```

## Hardware (if you build it for real)

| Part | ESP32 pin |
|---|---|
| IR sensor, slots A01-A08 | GPIO 32, 33, 25, 26, 27, 14, 34, 35 |
| IR sensor, entry / exit | GPIO 36 / 39 |
| Servo, entry / exit barrier | GPIO 18 / 19 |
| 2x 74HC595 (8 green + 8 red LEDs) | DATA 23, CLOCK 4, LATCH 5 |
| LCD 20x4 (0x27), OLED (0x3C), DS3231 | I2C: SDA 21, SCL 22 |
| ESP32-CAM (plate reader) | UART2: RX 16, TX 17 |

Arduino libraries: LiquidCrystal_I2C, Adafruit SSD1306, ESP32Servo, RTClib, PubSubClient, ArduinoJson.
Set `WIFI_SSID`, `WIFI_PASS` and `MQTT_HOST` at the top of the sketch. The sketch has not been
tested on real hardware, so check pins and libraries for your boards.

## Credits

3D models and libraries: see [THIRD_PARTY.md](THIRD_PARTY.md).
