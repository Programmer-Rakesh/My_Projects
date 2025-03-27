
#define enA 10 // Enable1 L298 Pin enA
#define in1 9  // Motor1 L298 Pin in1
#define in2 8  // Motor1 L298 Pin in2
#define in3 7  // Motor2 L298 Pin in3
#define in4 6  // Motor2 L298 Pin in4
#define enB 5  // Enable2 L298 Pin enB

// IR Sensor Pins
#define L_O A0 // Left Outer Sensor
#define L_I A1 // Left Inner Sensor
#define R_I A2 // Right Inner Sensor
#define R_O A3 // Right Outer Sensor

void setup()
{
    pinMode(L_O, INPUT);
    pinMode(L_I, INPUT);
    pinMode(R_I, INPUT);
    pinMode(R_O, INPUT);
    pinMode(enA, OUTPUT);
    pinMode(in1, OUTPUT);
    pinMode(in2, OUTPUT);
    pinMode(in3, OUTPUT);
    pinMode(in4, OUTPUT);
    pinMode(enB, OUTPUT);

    // Lower motor speed for thin lines
    analogWrite(enA, 120);
    analogWrite(enB, 120);
}

void loop()
{
    int lo = digitalRead(L_O);
    int li = digitalRead(L_I);
    int ri = digitalRead(R_I);
    int ro = digitalRead(R_O);

    // 1. Go straight if both inner sensors are on the line
    if (li == 0 && ri == 0)
    {
        forward();
    }
    // 2. If both left sensors detect black → Hard Right Turn
    else if (lo == 1 && li == 1)
    {
        turnHardRight();
    }
    // 3. If both right sensors detect black → Hard Left Turn
    else if (ro == 1 && ri == 1)
    {
        turnHardLeft();
    }
    // 4. If left inner detects black → Slight right correction
    else if (li == 1)
    {
        turnSoftRight();
    }
    // 5. If right inner detects black → Slight left correction
    else if (ri == 1)
    {
        turnSoftLeft();
    }
    // 6. Stop if outer sensors detect black
    else if (lo == 1 || ro == 1)
    {
        Stop();
    }

    delay(5); // Small delay for stability
}

// ===== Motor Control Functions =====
void forward()
{
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
}

void turnSoftRight()
{
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
}

void turnSoftLeft()
{
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
}

void turnHardRight()
{
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
}

void turnHardLeft()
{
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
}

void Stop()
{
    digitalWrite(in1, LOW);
    digitalWrite(in2, LOW);
    digitalWrite(in3, LOW);
    digitalWrite(in4, LOW);
}