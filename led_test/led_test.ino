
#include <FastLED.h>
#define LED_PIN 2
#define NUM_LEDS 200

CRGB leds[NUM_LEDS];


void setup() {

  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setMaxPowerInVoltsAndMilliamps(5, 500);
  FastLED.clear();
  FastLED.show();
  Serial.begin(9600);
  
}

void loop() {
    startup(1);
    delay(5000);
    sheathe(1);
    delay(5000);

}

void startup(int delayTime) {
  for (int n = 0; n < NUM_LEDS; n++) {
    leds[n]= CRGB::Blue;
    FastLED.show();
    delay(delayTime);
  }
}

void sheathe(int delayTime) {
  for (int n = NUM_LEDS; n >= 0; n--) {
    leds[n]= CRGB::Black;
    FastLED.show();
    delay(delayTime);
  }
}
