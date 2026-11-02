#ifndef myoptions_h
#define myoptions_h

#define DSP_MODEL DSP_ST7789
#define DSP_HSPI true // HSPI (SCK-14, MISO-12, MOSI-13)
#define TFT_CS 15
#define TFT_DC 2
#define TFT_RST -1
#define BRIGHTNESS_PIN 21
#define PLAYER_FORCE_MONO true

// --- Configuración I2S para P1 (TX) y CN1 ---
#define I2S_DOUT 1      // Pin TX en cabezal P1
#define I2S_BCLK 22     // Pin IO22 en conector CN1
#define I2S_LRC 27      // Pin IO27 en conector CN1
#define DBUG_SERIAL 0   // Desactiva logs serie para evitar ruido en TX (GPIO 1)

// --- Panel táctil y sensores integrados CYD ---
#define TS_MODEL TS_MODEL_XPT2046
#define TS_CS 33
#define TS_SPIPINS 25, 39, 32 /* SCK, MISO, MOSI */
#define LIGHT_SENSOR 34
#define AUTOBACKLIGHT_MAX 1024

//#define SD_HSPI false // VSPI (SCK-18, MISO-19, MOSI-23)
//#define SDC_CS 5

#endif
