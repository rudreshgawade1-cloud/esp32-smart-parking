# Third-party material

| Item | Where | Notes |
|---|---|---|
| three.js r128 (+ GLTFLoader, OrbitControls, RoomEnvironment) | `web/libs/` | MIT licence, https://threejs.org |
| Parking lot model | `web/models/parking.glb` | Supplied by the project author |
| Electronics models (ESP32 board, LEDs, resistor, SG90 servo, capacitor/diode kit) | `web/models/esp32.glb`, `led_*.glb`, `resistor.glb`, `servo.glb`, `parts.glb` | Supplied by the project author. Check their licences too. They were decimated and re-compressed for the web. |
| Car models (Ferrari LaFerrari, McLaren MP4/5 and Senna GTR, Hoonicorn, Mercedes-AMG GT3, Aston Martin AMR23, BMW M4, Alpine A480) | `web/models/*.glb` | Downloaded from vecarz.com / other sources. **Check each model's licence before publishing this repository.** They were also decimated and re-compressed for the web. |

If a model's licence does not allow redistribution, delete its `.glb` file (or uncomment the
`web/models/*.glb` line in `.gitignore`) and put your own models there. The names the app
expects are listed in `MODEL_NAMES` in `web/js/scene.js`.
