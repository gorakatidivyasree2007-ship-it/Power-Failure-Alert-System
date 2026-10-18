int supplySignal = 2;
int alarm = 8;

void setup() {
  pinMode(supplySignal, INPUT_PULLUP);
  pinMode(alarm, OUTPUT);
}

void loop() {
  bool supplyPresent = digitalRead(supplySignal);
  digitalWrite(alarm, supplyPresent ? LOW : HIGH);
}
